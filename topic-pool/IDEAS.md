# Candidate post angles — sree.riteangle.dating

Running list of blog angles drawn from ingested resources. `[ ]` = open,
`[x]` = drafted or used. Each links back to the resource it came from. These are
seeds, not commitments — shape any chosen one against `../STYLE.md` before
drafting, and clear third-party material against `../SAFETY.md` first.

## 2026-08-27

_From [token-factory-inference-economics](resources/2026-08-27-token-factory-inference-economics.md)
(public podcast interview — external reference only; angles are about Sree's own work):_

- [ ] **Keeping the LLM off the critical path: why my agents compute the answer deterministically and only narrate with a model** — the interview's "agent as an expensive person you consult" is exactly the pattern the zero-API skill-driven agents (job-hunt-agent, finance-controls-agent) reject; center on the compute-first / narrate-last split (MILP/POMDP/CFR decide, Claude writes prose) and what that buys in cost and determinism. Strong fit: mechanism + payoff both concrete.
- [ ] **Designing an agent that runs on human timescales, not prompt-wait loops** — "the best latency is no latency"; the long-horizon / background-agent framing mapped onto a real project where the human checks in on a batch rather than babysitting a turn. Center on the loop structure and where the handoff points are.
- [ ] **The jagged frontier is a sampling strategy: running a small and a large model over the same input and keeping both sets of findings** — "no model finds a superset of another's bugs." Tie to any multi-model review/validation workflow; mechanism is diverse sampling + merge, payoff is coverage a single model misses.
- [ ] **A deterministic self-grader is the whole trick: verifiable tasks in the oracle projects as RL-gym-shaped environments** — "the environment becomes the data." Connect the CFR / value-iteration / MILP verifiers (got-oracle, dhurandhar-oracle, ipl-oracle) to the verifiable-task idea; mechanism is the self-grading oracle, payoff is trustworthy iteration without a human label.
- [ ] **Token budget as a first-class input: giving an agent a dollar ceiling instead of a turn count** — the "outcomes, not tokens" / self-administered budget idea, grounded in how an agent's spend is bounded in one of the running tools; mechanism is budget-aware control flow, payoff is predictable cost per task.
- [ ] **Building for 95% uptime on purpose: a control plane that reroutes failed background work** — the scavenger / low-uptime-is-fine argument, mapped to designing agent runs that are idempotent and resumable so a dropped turn costs a minute, not a job. Center on the retry/resume mechanism.

_From [graph-engineering-for-ai-agents](resources/2026-08-27-graph-engineering-for-ai-agents.md)
(public video walkthrough — external reference only; angles are about Sree's own work).
Note: the [LangGraph fan-in/reducer post](../../pocket-dating-coach/src/lib/blog/posts/langgraph-over-a-hand-wired-pipeline.md)
is already published from this session — keep new angles distinct from reducers/fan-in/gate/checkpoint:_

- [ ] **A human-approval gate is just a conditional fork plus a checkpoint — nothing new to build** — the video's "interrupt before a consequential action" mapped onto spa-claude's *existing* automated PASS/WARN/FAIL gate: the fork already exists, the checkpoint already exists, so pausing for a person for hours instead of auto-deciding is a swap at one node, not new infrastructure. Mechanism: conditional edge + state snapshot = safe pause; payoff: a person can approve before the irreversible step without holding a process open. (Partially folded into the published post; still room for a standalone piece.)
- [ ] **When NOT to reach for a graph framework: why my zero-API agents are deterministic Python, not LangGraph** — the video's "sometimes you don't need a framework at all" is the exact call job-hunt-agent and finance-controls-agent made. Center on the decision boundary: a mostly-deterministic workflow coordinating a few model steps doesn't earn a StateGraph; contrast it with the oracle projects that do. Mechanism: framework-vs-plain-code trade-off; payoff: less state, less to test, the reasoning lives in a skill not a runtime.
- [ ] **Six agent patterns, and which three my oracles actually are (and the three I skipped)** — classify got-oracle / dhurandhar-oracle / spa-claude against prompt-chaining, routing, parallelization, orchestrator-worker, evaluator-optimizer, human-in-the-loop. They are chaining + parallelization + conditional routing; they are deliberately *not* orchestrator-worker or evaluator-optimizer. Mechanism: pattern taxonomy as a design checklist; payoff: naming the shape tells you its failure modes before you hit them.
- [ ] **Hard constraints belong in the edge, not the prompt** — the video's "guard conditions in code, not buried where the model can miss them" is the same principle as keeping the oracles' optimisation deterministic and the model on narration only. Center on routing/guards as code: a constraint the model *cannot* violate because it never gets to decide it. Mechanism: guard condition as code-level route; payoff: a class of "the model ignored the rule" failures made unrepresentable.
- [ ] **Node contracts for a long decision run: timeouts, idempotent retries, and error classes that know retry from stop** — the video's production-hardening list applied to a multi-hour oracle run (dhurandhar's per-turning-point sequence). Mechanism: per-node contract + error classification (transient → retry, terminal → halt) layered on checkpoint/resume; payoff: a Monte-Carlo or POMDP run that survives a rate-limit blip instead of dying at hour two.
