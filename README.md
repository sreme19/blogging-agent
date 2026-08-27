# blogging-agent

Guideline folder for writing and publishing posts to **sree.riteangle.dating**,
Sree's personal engineering blog. This folder holds no code and is not deployed
anywhere — it exists so that "write a blog post about X" has a durable, checked
set of rules to work from instead of re-deriving the house style from whatever
posts happen to be published at the time.

**Read this before writing any new post for that blog.** In order:

1. [STYLE.md](STYLE.md) — the editorial rules: titles, summaries, openings,
   examples, numbers, register, generalization, references, diagrams.
2. [SAFETY.md](SAFETY.md) — what never gets published, and how to handle
   other people's material. Check this before drafting, not after.
3. [PUBLISHING.md](PUBLISHING.md) — the mechanics: where files live, the
   frontmatter schema, the draft workflow, tag naming, the OG-card generator,
   known traps.
4. [CHECKLIST.md](CHECKLIST.md) — a pass/fail list to run against a finished
   draft before proposing it as ready.

## Where the actual blog lives

The blog itself is a subdomain of the `pocket-dating-coach` repo, not this
folder:

- Posts: `pocket-dating-coach/src/lib/blog/posts/*.md`
- Build mechanics: `pocket-dating-coach/src/lib/blog/README.md`
- Live at: `https://sree.riteangle.dating`

This folder is the editorial layer on top of that build. When the two
disagree on a mechanical detail (frontmatter fields, build behavior), the
blog's own `README.md` is authoritative — update `PUBLISHING.md` here to match
it, not the other way around. When they disagree on voice or structure, this
folder is authoritative — that's what it's for.

## How this folder came to exist

The house style was established over one long session of repeated correction
(2026-08-13) and had been living only in Claude's memory system, keyed to the
`pocket-dating-coach` project path. That worked until a session rooted
somewhere else (`job-hunt-agent`, writing a post about a different project)
had no way to find it and re-derived a shape from reading a few published
posts instead — which missed the actual rules (no code identifiers in prose,
the two-clause title pattern, the required generalization-table row count,
converting confessions into guidance) and had to be rewritten.

This folder is the fix: one place, checked into a normal directory, findable
regardless of which repo a session is rooted in. The original memory files
still exist and are cross-referenced from here where useful, but treat this
folder as the copy of record — update it directly when a rule changes, rather
than only updating memory.

## Updating this folder

When Sree corrects something about a new post (a title rejected, a section
that reads as confession, a missing example), that correction belongs in
[STYLE.md](STYLE.md) or wherever it fits — not just applied silently to the
one post in front of you. The value of this folder is that the next post
starts from the corrected rule instead of repeating the mistake.
