# Topic pool — sree.riteangle.dating

A holding area for raw material and candidate post angles for the blog. Filled
and read by the `/blog-topics` command (see
`../.claude/commands/blog-topics.md`).

## Layout

- `resources/` — one Markdown file per ingested resource (transcript, article,
  note, link). Each carries frontmatter (`title`, `source`, `type`, `ingested`)
  plus a short summary and a faithful capture of the material.
- `IDEAS.md` — the running list of candidate post angles. Each item links back
  to the resource it came from and carries a checkbox status (`[ ]` open,
  `[x]` drafted/used).

## How it's used

- **Ingest:** `/blog-topics <paste | URL | file>` — or "log this" — captures the
  resource into `resources/` and appends candidate angles to `IDEAS.md`. It does
  not draft anything.
- **Suggest:** `/blog-topics` (no args) — reads the whole pool and proposes a
  shortlist of the strongest angles, shaped to the house style in `../STYLE.md`,
  then asks which to draft.
- **List:** `/blog-topics list` — prints what's in the pool.

Candidate angles are meant to seed posts *in this blog's voice*: tied to Sree's
own engineering/AI work, centered on a concrete mechanism and payoff — not
generic commentary. See `../STYLE.md` before drafting, and `../SAFETY.md` for
handling other people's material (like third-party transcripts) safely.
