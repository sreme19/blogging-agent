# Pre-publish checklist

Run this against a finished draft before presenting it as ready. Each item
links back to where the rule is explained.

## Safety — check first

- [ ] No real company, contact, or third-party names that aren't already
      public information the post is directly citing ([SAFETY.md](SAFETY.md)).
- [ ] No comp figures, funding amounts, or dates specific enough to
      de-anonymize a real entity.
- [ ] No code identifiers anywhere in prose — no file names, function names,
      CLI flags, variable names ([STYLE.md](STYLE.md) Register).
- [ ] No actual ledger/record/message contents — described as categories,
      not quoted as rows.
- [ ] If describing anyone else's work: anonymized, figures invented,
      disclosed in an italic note, and flagged to Sree for a go-ahead
      ([STYLE.md](STYLE.md) Third-party material).
- [ ] No personal material about Sree beyond a single clause that genuinely
      sharpens a point — never the opening, never a worked example or heading,
      and nothing touching health, family, relationships or money
      ([SAFETY.md](SAFETY.md) "Sree's own personal material").

## Structure

- [ ] Title: two-clause, joined by "and," names an actual technique/mechanism
      AND states the payoff in engineering terms. Not terse, not value-only.
- [ ] Title is parseable on one pass at reading speed. No second clause that
      only continues the first grammatically ([STYLE.md](STYLE.md) "Plainness
      beats verbosity").
- [ ] Title leads with the real-world operational impact before the
      technical clause, not the reverse ([STYLE.md](STYLE.md) "Lead with the
      operational impact").
- [ ] No title or section frames a design choice as a capability the system
      is denied ("cannot," "unable to," "blocked from") — reframe as what the
      human keeps doing instead ([STYLE.md](STYLE.md) "Frame a design
      constraint as agency kept").
- [ ] Summary: three beats (stake, proposition, distinctive result/honest
      limit), not a contents list.
- [ ] Summary names the actual thing built, concretely enough that a reader
      finishing it can say what it is ([STYLE.md](STYLE.md) "Name the thing
      that was built").
- [ ] Opening paragraph: a situation or incident, not a category claim.
- [ ] No heading is literally "What," "Why," "How," "When," or "Who."
- [ ] Every contrast or rule has a worked example on **both** sides, with
      concrete values on the hard side too, not just the easy one.
- [ ] Any percentage or statistic is either measured-and-labeled-as-such, or
      not stated at all. No invented numbers.
- [ ] No section reads as an apology for unbuilt work — every honest gap is
      phrased as an instruction for the reader (what to measure, what to set
      up), not a confession.
- [ ] Closing convention matches the post type: technical/architecture posts
      get the generalization section + reference architecture; personal
      career-narrative posts get the "What I never measured" table instead
      ([STYLE.md](STYLE.md) Two closing conventions).
- [ ] Generalization section (if the architecture-post convention applies)
      has 5–6 rows in its industry table and exactly 3 bold-led transferable
      choices, not fewer.
- [ ] Architecture posts state the counterfactual early and with numbers: why
      not just do the obvious simple thing? Cost and latency named as the
      drivers where that's the truth ([STYLE.md](STYLE.md) "An architecture
      post has to answer why the naive thing wasn't enough").
- [ ] Any thesis Sree stated in chat is the spine of the piece — opening,
      pull-quote and closing — not a paragraph buried inside it.
- [ ] Any References section only cites URLs that were actually fetched and
      read. If there's no real external sourcing, there's no References
      section at all.

## Register

- [ ] Sentences average 15–18 words; nothing runs past ~35 unbroken.
- [ ] Technical vocabulary is intact — it reads like an engineer wrote it,
      not a press release.
- [ ] Long comma-runs converted to lists.

## Sourcing

- [ ] Existing posts grepped for overlap before the angle was chosen, and any
      substantial overlap raised in chat ([STYLE.md](STYLE.md) "Check what's
      already published").
- [ ] The project's own current state has been read, not recalled: run
      `job-hunt-agent projects show <repo>` (or `projects evidence` for the
      whole portfolio) for its last commit, stack, and one-liner, and read the
      repo's README/SPEC directly for anything the post asserts
      ([STYLE.md](STYLE.md) "Read the repo's current state, don't recall it").
- [ ] If the project has a GitHub wiki, it's been read before writing — often
      already in plain, non-code language, and sometimes corrects a stale
      claim in the spec/README ([STYLE.md](STYLE.md) "Check a project's own
      wiki").
- [ ] Any new diagram has been rendered and visually checked for overlaps
      (arrows crossing boxes, labels sitting on arrowheads) before its
      `![alt](/blog/name.svg)` reference gets embedded in the post
      ([STYLE.md](STYLE.md) "Render a new diagram before embedding it") —
      including the bottom of a portrait SVG, which `qlmanage` crops
      ([PUBLISHING.md](PUBLISHING.md) "Checking an SVG before it ships").
- [ ] A post describing a multi-component system carries both flows: how the
      thing gets built/ingested, and what happens at query time end to end,
      through to generation.

## Mechanics ([PUBLISHING.md](PUBLISHING.md))

- [ ] Frontmatter has `title`, `date` (YYYY-MM-DD), `summary`, `tags`,
      `draft: true`.
- [ ] No tag starts with `ai-`.
- [ ] Slug (filename) is final — it will become the permalink.
- [ ] Not committed/pushed without an explicit go-ahead in chat, even as a
      draft.
- [ ] Before un-drafting: OG card generated (`blog-og-card.py <slug>`) and
      `cover:` set, or a deliberate decision to accept the generic fallback.
- [ ] Card regenerated after any title change, since the title is baked into
      the card as pixels.
- [ ] If a card changed after the post was ever shared: written to a NEW
      filename with `cover:` repointed, and Sree told to re-run
      [Post Inspector](https://www.linkedin.com/post-inspector/) — the `?v=2`
      query trick does not work on this site ([PUBLISHING.md](PUBLISHING.md)).
