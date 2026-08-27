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
