---
title: "Token factory" — a podcast interview on making inference tokens as cheap as possible
source: pasted (YouTube transcript; podcast interview with an inference-infra founder)
type: transcript
ingested: 2026-08-27
---

> Third-party public material. Angles below are for posts *about Sree's own
> engineering work*, using this interview only as a public reference point.
> Per SAFETY.md, get an explicit go-ahead before publishing anything that
> quotes or leans on it.

## Summary

- Founder of an inference company framing it as a "token factory": one API,
  open-source LLMs, goal is the **lowest cost per token in the industry**, plus
  hosted long-running "sandbox" VMs for agents that run for hours/days/weeks.
- Core thesis: the future of agentic inference is **long-horizon background
  tasks**, not low-latency chat. "The best latency is no latency" — agents work
  overnight on human timescales; you check in daily/weekly, not every 5 minutes.
  Predicts ~50/50 background vs real-time this year moving to ~90/10 background.
- **Throughput vs latency is a foundational hardware tradeoff.** GPUs are happy
  when fed large batches (throughput); chat forced everyone into latency
  optimization. Bus-vs-private-car analogy. Background agents let you optimize
  for throughput instead.
- **The frontier of intelligence is jagged**: a small model (e.g. Haiku) finds
  bugs a large model misses and vice versa, so security work samples across many
  models. "Security has become proof of work" — how secure your software is ≈
  how many dollars of inference were spent trying to break it.
- **Verifiable tasks + self-grading = recipe for self-improvement.** Data's next
  phase is RL environment "gyms," not more internet text ("a one-time subsidy").
  "The environment becomes the data." Non-verifiable tasks (taste, art, writing
  quality) are explicitly left to humans.
- **Cost is a hidden dollar tax on every task.** Long-horizon answers are moving
  from millions → thousands → possibly tens of dollars. KV cache is called the
  biggest inefficiency: "nowhere near earning its keep," compressible by an
  order of magnitude or two.
- **Scavenger strategy**: buy any chip anywhere for any duration (AMD, TPUs,
  Trainium, Cerebras/Groq as accelerators), pair a fast-memory chip with a
  high-capacity one, and run in many small (~1 MW, ~8 fridge-sized racks)
  distributed data centers on intermittent/renewable power — tolerating even
  95% or 80% uptime because background agents don't care about P99 latency, only
  average throughput. Requires a robust control plane to move failed work.
- Hiring: looks for **curiosity and love of performance engineering**, not CUDA
  years ("a red herring"). Open vs closed: labs pay a premium to be 3–6 months
  ahead; open source never disappears; capability diffusion is unstoppable
  ("latent distillation" via AI-generated GitHub code).

## Captured content (trimmed: ad reads and music cues removed)

**The product / thesis.** An inference company selling tokens from open-source
LLMs at an unbeatable price, plus long-running agent sandboxes in the cloud.
Theme: *abundance* — deliver intelligence as a commodity to as many people as
possible at a sustainable cost. "Whenever you make something 10x cheaper it's a
new product category." North star: lowest cost per token, by a mile. Tokens
aren't the final unit — the direction after tokens is *outcomes*, where an agent
self-administers a token budget and however many tokens it uses is a dependent
variable of the task.

**Why background agents.** "I don't want you to be waiting on it. I want it in
the background." Humans are the bottleneck in prompt-wait loops; agents should
operate on human time scales (you don't manage colleagues every 5 minutes).
Test-time compute scaling — more time → better answer — became bettable only
recently as average task length grew from minutes toward an hour. Background is
"unbounded": no human attention cap on how many tokens can be consumed. Best
examples: deep research over 10,000+ sources; building/monitoring an index over
the whole internet; cyber-security agents that pen-test and patch software.

**Jagged frontier / security as proof of work.** Running many models (Fable,
Haiku, etc.) against every line of code, looking for memory / business-logic /
network bugs in 20 different ways, in real environments rather than one static
source-code pass. No model is a superset of another's bugs — encourages diverse
sampling. "How secure is it?" ≈ "how many dollars did you spend trying to break
it."

**Speculative upside.** Proactive personal agents (a Siri that reads all your
mail/texts overnight and surfaces your next action); a dollar cost on any
verifiable problem — most software, math proofs, scientific discovery — coming
"within view" at thousands, maybe hundreds/tens of dollars. Unlock is *cheap
intelligence* + willingness to spend tokens with no promise of return.
Non-verifiable "human taste" is left to people.

**Hardware.** Software first: build the whole LLM stack around peak GPU
efficiency, squeeze more tokens per chip via kernels ("we write kernels on the
whiteboard" — describe the strategy in natural language, let a model implement).
NVIDIA background: tensor cores earned die area (~5–10% at first) against the
graphics teams; "speed of light" ethos — chase 100% of what the hardware can do,
absolute numbers not relative. Throughput-vs-latency: batching does net more
work, so any one request rides slower (bus vs car). NVLink is great but mandatory
mainly for *low-latency* tensor parallelism; for throughput you can use other
parallelism (expert/pipeline) and cheaper high-FLOP/$ chips that lack fast
interconnect.

**Memory.** SRAM (on-die, tiny, ~PB/s, Cerebras maximizes it across a whole
wafer) vs DRAM/HBM (off-die, huge capacity, must refresh every ~50 ms). Cerebras
/ Groq → treat as accelerators paired with a high-capacity GPU: MLP (compute-
bound, weights) on the fast-memory chip, attention (memory-bound, KV cache,
grows unboundedly with use) on the GPU. "The original sin of transformers" is
putting a memory-bound layer right next to a compute-bound one. KV cache: an
exact representation of all prior tokens; models trained mostly at short context
degrade at long context; the biggest current inefficiency, compressible by
~1–2 orders of magnitude (DeepSeek publishing progress).

**Transformers / data.** Attention lets the model dynamically reweight the
sequence and represent any pairwise relationship; transformers scale with
compute ("great sponges"), the link from millions → trillions of params.
Karpathy's overfit-then-compress: compression is how you get generalization.
Internet text = a one-time subsidy (~30T–300T tokens, already seen many times);
next phase is model self-improvement via verifiable RL gyms — "the environment
becomes the data"; labs now spend more on RL environments than on data.

**Data centers / power / market.** Diseconomy of scale — a 1 GW site is far
harder than many 1 MW sites; training assumed one big cluster, inference suits
distributed small ones. Scavenger strategy: aggregate (never concentrated)
supply of cheap chips + cheap intermittent power; tolerate low uptime because a
robust control plane reroutes failed work and background agents only feel an
occasional extra minute of latency, not a broken SLA. "Average throughput
competitive, P99 uncontrolled, in return unbeatable economics." Investor worry
(semis at ~20% of S&P): argues inference spend, unlike the dot-com networking
buildout or 2023–24 training spend, is *not speculative* — tokens are used
immediately, so inference spend monotonically increases. Biggest supply
bottleneck to attack: HBM. Contrarian take: perf/watt gap between process nodes
and between vendors (even losing TSMC) is smaller than the discourse assumes.
