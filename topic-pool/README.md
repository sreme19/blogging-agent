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

- **Capture from a repo:** `blog-pool add --repo <name> --angle "..."`, run from
  the session where the work actually happened. Writes a `type: own-work`
  resource carrying the repo, commit sha and commit subjects — a pointer to
  follow at draft time, not the work itself. This is the one way into the pool
  that does not start here, because the judgement that something is worth
  writing about exists in the session that did it, and does not survive the wait.
- **Ingest:** `/blog-topics <paste | URL | file>` — or "log this" — captures the
  resource into `resources/` and appends candidate angles to `IDEAS.md`. It does
  not draft anything.
- **Suggest:** `/blog-topics` (no args) — reads the whole pool and proposes a
  shortlist of the strongest angles, shaped to the house style in `../STYLE.md`,
  then asks which to draft.
- **List:** `/blog-topics list` — prints what's in the pool.

A `type: own-work` resource is Sree's own repo, not somebody else's material,
so `../SAFETY.md`'s rules for third-party content do not apply to it. Its rule
about coordinates still does: a post about your own work can name a real client,
a real number or a real target company just as easily as one about someone
else's.

Candidate angles are meant to seed posts *in this blog's voice*: tied to Sree's
own engineering/AI work, centered on a concrete mechanism and payoff — not
generic commentary. See `../STYLE.md` before drafting, and `../SAFETY.md` for
handling other people's material (like third-party transcripts) safely.
