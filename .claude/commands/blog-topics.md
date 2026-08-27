---
description: Ingest a resource into the blog topic pool, or draw new post ideas from it
argument-hint: [paste text | URL | file path | "suggest" | "list"]  — omit to suggest
---

You maintain a **topic pool** for the blog **sree.riteangle.dating** (Sree's
personal engineering blog). The pool lives in `topic-pool/` inside this
`blogging-agent` folder:

- `topic-pool/resources/` — one Markdown file per ingested resource (raw
  material: transcripts, articles, notes, links). Each has frontmatter and the
  captured content.
- `topic-pool/IDEAS.md` — the running list of candidate post angles, each
  linking back to the resource(s) it came from and tagged with a status.
- `topic-pool/README.md` — how the pool works (read it if unsure).

Before generating or judging topics, read `STYLE.md` (house style),
`SAFETY.md` (what never gets published, handling others' material), and skim
`topic-pool/IDEAS.md` so you don't repeat an angle already in the pool.

## Decide the mode from `$ARGUMENTS`

**INGEST** — arguments contain a resource (pasted text, a URL, a file path), or
the user's phrasing is "log this", "add this", "ingest", "save this":

1. If it's a URL, fetch it. If it's a file path, read it. If it's pasted text,
   use it directly.
2. Create `topic-pool/resources/<YYYY-MM-DD>-<short-slug>.md` with frontmatter:
   ```
   ---
   title: <human title of the source>
   source: <URL or "pasted" or original file path>
   type: <transcript | article | note | thread | paper | other>
   ingested: <YYYY-MM-DD>   # use today's date from context
   ---
   ```
   Followed by: a 3–6 bullet **summary** of the material, then the captured
   content (for long transcripts/articles, a trimmed but faithful capture is
   fine — keep the substance, drop filler like ad reads and music cues).
3. Extract **candidate blog angles**: ideas from this resource that could seed a
   post *in this blog's voice* — i.e. tied to Sree's own engineering/AI work,
   with a concrete mechanism and payoff (per STYLE.md), not generic hot-takes.
   Append each to `topic-pool/IDEAS.md` under a dated section, in this form:
   ```
   - [ ] **<working angle, one line>** — <why it fits an engineering post; the
     mechanism it would center on> · from [<resource slug>](resources/<file>.md)
   ```
4. Report back: the resource file created, and the candidate angles added.
   Do not draft a post — this command only fills the pool.

**SUGGEST** — no arguments, or arguments are "suggest" / "new topics" /
"what should I write":

1. Read every file in `topic-pool/resources/` and the open (`[ ]`) items in
   `IDEAS.md`.
2. Propose a shortlist (aim for 3–6) of the strongest post angles, each with:
   a STYLE.md-shaped working title, one line on the mechanism it would center
   on, and the resource(s) it draws from. Prefer angles that connect a resource
   to Sree's own projects (use the `job-hunt-agent projects` commands in the
   root `CLAUDE.md` if you need to ground an angle in a real project).
3. Flag anything that would trip SAFETY.md (other people's material, private
   data) so it's handled before drafting.
4. End by asking which one to draft — drafting is a separate step, not part of
   this command.

**LIST** — arguments are "list" / "pool" / "status": print the pool contents —
resources on file and the open candidate angles in `IDEAS.md` — as a compact
overview. No new ingestion, no new suggestions.

If the pool directory doesn't exist yet, create it (with a `resources/` subdir,
an empty-ish `IDEAS.md`, and the `README.md`) before proceeding.
