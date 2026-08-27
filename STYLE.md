# Editorial house style — sree.riteangle.dating

Established by repeated correction across ~21+ posts (session of 2026-08-13,
plus later additions). Apply to every new post without being asked. This is
the copy of record — see [README.md](README.md) if this ever drifts from
memory notes elsewhere.

Scope note: the personal career-narrative sub-series (posts reflecting on past
roles, e.g. governance/curriculum/routing/capability-matrix pieces) closes
differently — see "Two closing conventions" near the end. Everything else
below applies to it too.

## Titles

The exemplar, called "perfect" when it landed:

> LLM-as-judge in the send path, and the human-label calibration that gives its
> score an error bar

Pattern: **[named technique] + [non-obvious placement] + "and" + [the
companion piece everyone skips] + [payoff stated in engineering terms]**

The "and" clause does the work — it says *here is the thing, and here is the
half nobody builds*. The payoff must be technical ("an error bar"), not a
benefit statement ("so you can trust it more").

Rules, in the order they were learned the hard way:

- **Terse titles fail.** "An optimiser in 512 megabytes" was rejected as
  obscure on its own.
- **Value-only titles fail.** Rewriting to "Picking an optimal cricket XI in
  four seconds" stripped the technical vocabulary — rejected for lacking
  agentic/data/model language.
- **The title must carry BOTH the mechanism and what it buys.** Name the
  actual thing: MCP, min-cost max-flow, POMDP, LLM-as-judge, NULLS FIRST, dbt
  detectors, schema-level provenance omission. Not "a smarter pipeline" —
  "min-cost max-flow" or whatever the real technique is.
- **Verbose is wanted. Long is fine.** Titles run 15–23 words routinely.
- **Leading with a failure beats leading with a feature, where honest** —
  e.g. "the accuracy headline that failed a per-class check."
- **Never rename a slug after publishing** — it breaks shared links. Titles
  can still change; slugs are the permalink and are fixed the moment a post
  is live.
- **Choose the slug for the durable topic, not the first draft's angle.** The
  title will very likely change; the slug cannot. A post published as
  `where-a-wrong-answer-gets-prevented` was retitled three times and ended up
  as a plain when-to-use-which comparison, leaving a permalink that describes
  an angle the piece no longer takes. Name the slug after the subject a reader
  would search for (`vector-sql-and-graph`), not after the argument the
  current draft happens to make. Decide it late, just before the first commit,
  once the shape has settled.

**Lead with the operational impact, not the mechanism jargon (added
2026-08-21).** A title that opens entirely in engineering vocabulary — e.g.
"A send action with no code path, and the second runtime that shares its
write path instead of a metered key" — was rejected as "too complicated" even
though it technically satisfied the mechanism-and-payoff rule above. The fix
was to restate it as **[the real-world thing being automated/impacted] +
[the one technical detail that actually matters]**: "Automating my job hunt
outreach with an agent that finds, researches, and drafts — and leaves
sending to me." Same information, reordered so a reader knows what this is
*about* before they're asked to parse a technical clause. Read the
mechanism-and-payoff rule above as: name the mechanism, but only after the
reader can place what business or operational thing it's in service of. This
matters most for posts about a personal tool or utility rather than the
riteangle product itself — revisit whether it should generalize further as
more posts confirm or complicate it.

**Frame a design constraint as agency kept, not capability denied (added
2026-08-21).** An earlier pass at the same title said the agent "structurally
cannot hit send" — technically accurate, rejected as reading negative. The
same fact reframes as something the human still owns rather than something
the machine is denied. Prefer "leaves sending to me," "keeps the send with a
person," "I still send everything myself" over "cannot," "is unable to," "is
blocked from." Say what the human keeps, not what the machine is denied — the
underlying design point survives the reframe untouched.

**Plainness beats verbosity when the two conflict (added 2026-08-25).** Two
titles were rejected in one session on the same post, and the pattern is worth
stating outright because the rules above actively push toward the failure. The
first, "One agent, three databases, and how to decide whether a question
belongs to a vector index, a SQL store or a graph," was called *diluted* — it
described the article's contents without making its claim. The second,
"Tabular won because humans read tables, and the vector index and graph that
follow when the reader is an agent paying by the token," satisfied every rule
above (two clauses, named mechanisms, a real thesis, 24 words) and was rejected
as *convoluted, hard to infer what it's saying, a bit abstract.* It reads as a
sentence fragment the reader has to reassemble.

What landed: "When to use a vector database, when a SQL table, and when a
graph, and what it costs to pick wrong."

The test that separates them is whether a reader knows what the article *is*
on one pass, at reading speed, without re-parsing. A title can name real
mechanisms and still fail that test if the grammar makes them work for it.
Where a clever construction and a plain one carry the same information, take
the plain one. "Verbose is wanted" above means *do not be terse*; it does not
license a clause the reader has to unpick. Watch particularly for a second
clause that continues the first grammatically rather than standing on its own,
which is what broke the rejected title.

## The summary field is an abstract, not a contents list

It renders as the subtitle and is the first thing read after the title. A
rejected complaint about a bad one: *"it sounds very vanilla… the value is not
being shown upfront."*

Three beats, in this order:

1. **The stake** — what breaks, or why this is a problem at all.
2. **The proposition** — what was built, in one line.
3. **The distinctive result or the honest limit.**

Not: "This post covers X, Y, and Z." That's a table of contents wearing a
subtitle's clothes.

**Name the thing that was built, in plain words (added 2026-08-25).** A summary
was rejected as *"obscure… not talking about what this project is about and
what has been built here and what the goal is. It also seems very abstract.
Language needs to be simpler and to the point."* The rejected version led with
an abstraction ("a filter is only as good as the caller who remembers to apply
it") and never said, in concrete terms, what the system was or what it did. The
three beats above are necessary and not sufficient: beat two has to describe a
real artifact a reader can picture — *1,100 documents split across three local
stores*, not *a structurally different approach to prevention*. If a reader
finishes the summary unable to say what was built, rewrite it, however well the
three beats are hit.

**Open the summary on a scene, and state the limit directly (added 2026-08-27).**
A summary was rejected twice in one sitting — first as *"so confusing to read,"*
then, after a structural fix, as *"sounds so abstract."* Two specific failures,
both from the LangGraph post's original summary:

- **Machinery described in abstract nouns.** "A one-line merge rule letting both
  write the same list without a collision" names the feature but shows nothing.
  What landed instead was a two-sentence scene with named actors and a visible
  failure: *"Say your pipeline has a threat-scoring agent and a coalition-modelling
  agent, and both append their findings to the same warnings list… both read the
  old list, both write their own copy back, and one agent's findings silently
  vanish."* The Openings rule ("a situation, something happening") applies to the
  summary too, not just the first paragraph.
- **A caveat phrased as a negated abstraction.** *"What it does not buy you is a
  reason to reach for any of this when your pipeline is honestly a straight line"*
  forces the reader to parse the non-purchase of a reason. State the limit as a
  direct instruction with a concrete instance of the excluded case: *"If your
  pipeline is honestly a straight line — fetch, then compute, then summarize —
  you have nothing to parallelize and nothing to merge; write the for-loop and
  move on."*

The test: every noun in the summary should be something the reader can picture
(an agent, a list, a run dying), and every claim should be affirmative — say what
to do and when, not what something fails to justify.

## Openings

Open on **a situation, something happening** — a person doing a thing, or an
incident. Never on a claim about a category.

Rejected openings, all rewritten before publishing: *"The prompt is not a
template with a few variables in it,"* *"Optimisation and serverless are an
awkward pair,"* *"Prompts are instructions, not constraints,"* *"Model-graded
evaluation was the loudest theme at conferences."* Each of those is a category
claim — true, but nothing is happening in it.

The model to imitate: open on a specific person being penalized for declining
to prove something, and let the general principle arrive second, after the
scene — it lands harder for having a concrete case in front of it first.

## Never use what/why/how/when/who as headings

The blog needs to answer what a thing does for a person, why the constraint
exists, when it bites, and who should care — but woven into prose and into
section headings that each state one *idea*, not literally titled "What,"
"Why," "How." A heading is a claim, not a category label.

## Examples are mandatory, on both sides

Every rule, failure mode, and abstract claim needs a worked instance with
concrete values. The recurring failure mode here was illustrating the *easy*
half of a contrast and leaving the hard half poetic — e.g. a regex example for
"phone number," paired with nothing more concrete than "impersonation lives in
pronouns" for the hard case. Both sides of any contrast get an example with
actual values in it, not just the tractable side.

Where a comparison is the point, show two artifacts side by side — two replies
differing only in who they claim to speak for; a reply scored `4` versus one
flagged `rule 6` — not a description of the difference in prose alone.

## Numbers

- Separate **configured** values from **measured** ones, and say which is
  which. A configured constant (a cap, a threshold you set) is not evidence of
  anything; presenting it as if it were is the single most common way a
  numbers claim goes wrong here.
- **Never invent a percentage.** If it hasn't been measured, don't quote a
  number for it — say it's unmeasured (and see "Do not confess" below for how
  to say that usefully).
- Re-derive a suspicious statistic before publishing. One accuracy headline in
  an earlier draft turned out to be a majority-class artifact once it was
  actually checked, not just quoted.

## Do not confess unbuilt work to the reader

*"It adds no value to the end user if I tell them something that I have not
implemented… remove such things and maybe do something better."*

Convert every confession into guidance. "Our block rate is unmeasured" becomes
"track block rate, set a floor alert, a week at zero means go find out which."
A closing table of unmeasured quantities becomes four numbers in build order,
each with how to get it and what it tells you once you have it.

This does not mean hiding real limitations. Honest **design** trade-offs stay
in — same-family judging, a fail-open choice, a deliberately narrow filter
dimension. Those are properties of the architecture and belong in the post.
The line is between "here's a trade-off I chose and why" (keep) and "here's a
thing I never got around to measuring, sorry" (convert to an instruction for
the reader instead).

## Every post generalizes

A section near the end — titled to name what's being generalized away from
(a dating app, a clinic, a routing engine, a cricket squad, a job search) —
that contains:

- A pull-quote stating the pattern abstractly, in one or two sentences.
- An industry table, **5–6 rows**, mapping the pattern to other settings a
  reader in a different field would recognize.
- **3 transferable design choices**, each in a bold-led paragraph (bold the
  instruction, then explain it), not a bare bullet list.

Three rows is not enough; six is the target, five is the floor.

## Register

- Use the field's actual technical vocabulary. Don't dilute into plain English
  so far that it stops sounding like an engineer wrote it.
- **Never cite code identifiers in prose** — no file names, function names, CLI
  flag names, variable names, line numbers. *"None, not even me, can
  understand it."* Describe the mechanism in words a reader with no access to
  the repo could follow: not "`draft.py` calls `_read_exemplars()`," but "the
  drafting step reads a small file of user-confirmed good examples before
  writing anything."
- Average sentence length 15–18 words; break up anything past ~35. Headings
  state one idea, not a qualified clause with a comma in it.
- Long comma-runs become lists.

## Two closing conventions

**Technical architecture posts** (the default — anything documenting how a
system is built) close with the generalization section above, followed by a
full reference architecture: every component and every real technology named,
as the implementation takeaway, followed by the handful of things that are
cheap to build in now and expensive to retrofit later.

**The personal career-narrative sub-series** (first-person reflection on a
past role or engagement, not a currently-running system) closes instead with
a "What I never measured" honesty table — because the honest failure in that
sub-series usually is an unmeasured claim about a past engagement, and forcing
an industry table onto a personal story reads as padding. If you're not sure
which this is: a post about software you built and can still point at is the
first kind; a post about a job you no longer hold is the second kind.

## References

Split **Papers / Tooling / Talks** where there's more than one kind. Inline
the citation where the concept first appears *and* list it again in a closing
References section.

**Only cite a URL that was actually fetched and read.** Never construct one
from a guess at what it should be. Where a reference is an approximation
rather than a direct source, say so explicitly (e.g., citing the
machine-translation ancestor of a concept because no canonical source for the
LLM-era version exists).

If a post has no real external sourcing — nothing was actually looked up — it
gets no References section. An invented one is worse than none.

## Diagrams (optional, used on roughly a third of posts)

Hand-authored inline SVG, saved to `pocket-dating-coach/static/blog/*.svg`,
referenced as `![alt](/blog/name.svg)`. Not required for every post — reach
for one when a state machine, a pipeline, or a before/after is genuinely
easier to show than to narrate.

- **Portrait, ~560px wide.** The blog is read mobile-first; a landscape
  diagram becomes unreadable at phone width. (OG/share cards are the one
  exception — those are landscape 1200×630.)
- Light-theme tokens are hardcoded, since figures never render in dark mode:
  paper `#fcfbf8`, card `#ffffff`, ink `#17161b`, muted `#6e6a63`, rule
  `#e8e3d8`, accent `#b4541e`, accent-soft `#f6ece4`, green `#2f6b46`.
- Fonts: headings in `'Iowan Old Style', Palatino, Georgia, serif`; labels and
  body text in `system-ui, -apple-system, sans-serif`.
- `role="img"` with a `<title>` and `<desc>` wired via `aria-labelledby` — the
  `<desc>` carries the entire argument in words, for screen readers and for
  anyone scanning the raw file.
- **Animate connectors** with marching dashes: `stroke-dasharray` plus a
  `stroke-dashoffset` keyframe advancing exactly one dash period per cycle,
  wrapped in `@media (prefers-reduced-motion: no-preference)`. A diagram with
  no directional flow (a bar chart, a layer stack, a plain table) stays
  static — don't animate something that isn't showing movement.
- **Name the actual technology inside the diagram** — a specific model name,
  a specific database, a specific protocol — not a generic box labeled
  "model" or "database."

## Check what's already published before choosing an angle

Grep the posts folder before drafting. A post on the three-store retrieval
layer was nearly written as a straight duplicate of an existing 9,000-word
piece that already covered the same split, the same router, and the same eval
table — caught only by reading the other post's headings partway through
drafting.

```bash
grep -l '<topic keyword>' pocket-dating-coach/src/lib/blog/posts/*.md
grep -n '^#' pocket-dating-coach/src/lib/blog/posts/<candidate>.md
```

If an existing post covers the ground, there are two honest options and one
dishonest one. Take a genuinely different angle and cross-link to the existing
piece, or write the canonical version and accept it supersedes the other. Do
not quietly write the same post twice. Say which you're doing, in chat, before
drafting rather than after.

Note that Sree may still want the overlapping post — being told "this is
already covered" is useful, being blocked on it is not. Raise it in a sentence
and keep going.

## An architecture post has to answer why the naive thing wasn't enough

Every post describing a multi-component system needs the counterfactual stated
explicitly and early, with numbers: what would happen if you just did the
obvious simple thing instead. For a retrieval architecture that is *why not
hand the model everything?* For an optimiser it is *why not brute force?*

This came from a post that explained a three-store split in full without ever
saying why anyone would build it. The missing answer was economic — tokens cost
money and answers have to be fast — and Sree had to ask for it twice. Cost and
latency are usually the real reasons an architecture exists, and they are
usually the part an engineer writing about their own system forgets to say
because it is obvious to them.

State the ranked drivers plainly (here: cost first, speed second, and one
capability argument that is not about either), and give each one a measured
number rather than an assertion.

## Sree's own framing wins

When Sree states a thesis in conversation — "the shape of data systems has
inverted, we used to build for human legibility and now the first consumer is
an agent" — that becomes the spine of the piece, not a paragraph inside it.
Rework the opening, the pull-quote and the closing around it. Twice in one
session an angle chosen from reading the code was replaced by a sharper one
Sree supplied in a sentence.

## Read the repo's current state, don't recall it

Before writing about one of the author's own projects, read what the repo says
today. `job-hunt-agent projects show <repo>` gives its last commit date, stack,
and one-line summary from a live read of the working tree; `job-hunt-agent
projects evidence` gives the whole portfolio, most recently committed first.
Both refresh before printing.

This exists because the standing summary of the portfolio was found to be eight
repos out of date — every post drawn from memory would have described a
snapshot months old, and confidently. A post that states a project's stack, its
status, or what it does needs those facts read at drafting time. Anything the
index marks `review` is withheld deliberately; treat that as a decision, not an
obstacle, and ask before writing about it.

## Check a project's own wiki before writing from source code alone

If the project has a GitHub wiki, clone it (`git clone
https://github.com/<owner>/<repo>.wiki.git`) and read it before drafting.
Two payoffs, confirmed on the job-hunt-agent post: its wiki already describes
the system in plain language with no code identifiers (workers called "the
researcher," "the writer," a spreadsheet called "the shared notebook") —
often directly reusable prose, saving the work of stripping jargon out of
source comments by hand. It also caught a factual error a spec document
alone did not: a spec described a scheduled job as "a cron-triggered cloud
agent," but the wiki's own architecture page explained, with the reasoning,
that a cloud-hosted option was evaluated and specifically rejected because it
runs sandboxed with no access to the local file the system depends on — the
real implementation is a local scheduled task. Wikis that go to the trouble
of writing out *why* a decision was made this way and not that way tend to be
more current and more precise than a spec file's shorthand description of
the same decision.

Wiki diagrams are typically Mermaid, and this blog's build does not render
Mermaid — a fenced ` ```mermaid ` block shows up as plain monospace text, not
a diagram (see the Diagrams section above and PUBLISHING.md). Redraw the
diagram as a hand-authored SVG in this blog's house style instead of pasting
the fence in; a wiki diagram already in plain language is usually a
near-direct source for the new SVG's labels.

## Render a new diagram before embedding it

A hand-drawn SVG adapted from a wiki's flowchart won't have the same shape as
the fixed card-and-arrow layout this blog uses, so coordinate collisions are
common on the first pass — an arrow routed straight through a box it should
route around, or a branch label sitting on top of its own arrowhead. Copy the
new SVG into any project folder the Browser pane can render (its file-preview
mode works even outside that folder — it just renders as a static snapshot,
which is enough to check layout), screenshot it, and fix anything that
overlaps before embedding the `![alt](/blog/name.svg)` reference in the post.
Caught both failure modes above on the first two diagrams built this way; a
diagram nobody looked at before publishing is a diagram that ships broken.

## Third-party material

If a post describes anyone else's work (a client, a clinician, another
person's decisions), anonymize the party, invent all rates and figures,
generalize the domain enough that it isn't identifiable, omit account
identifiers and endpoints, and say so in an italic note near the top of the
post. Flag it to Sree before publishing, every time — this is not a call to
make unilaterally. See [SAFETY.md](SAFETY.md) for the hard boundaries this
runs into.
