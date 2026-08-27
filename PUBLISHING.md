# Publishing mechanics — sree.riteangle.dating

Where the editorial rules in [STYLE.md](STYLE.md) say *what* to write, this is
*how it gets from a draft to a live URL*. Learned by getting each of these
wrong first — see `pocket-dating-coach/src/lib/blog/README.md` for the
canonical build-level reference if this ever drifts from it.

## Where a post lives

- File: `pocket-dating-coach/src/lib/blog/posts/<slug>.md`. The filename
  (minus `.md`) is the URL segment and the permanent slug — see STYLE.md's
  rule about never renaming one after publishing.
- Frontmatter:

  ```yaml
  ---
  title: <two-clause title per STYLE.md>
  date: YYYY-MM-DD
  summary: <one or two lines, per STYLE.md's three-beat abstract>
  tags: [tag-one, tag-two]
  draft: true
  cover: /og/blog/<slug>.png
  ---
  ```

  `title` and `date` are required; the build fails loudly if either is
  missing or `date` isn't `YYYY-MM-DD`. Everything else is optional but
  `summary`, `tags`, and `cover` should be filled in for anything meant to go
  live.

## The draft workflow

1. Write the file with `draft: true`.
2. Preview locally with `npm run dev` at `http://localhost:5173/blog` — drafts
   render there and nowhere else.
3. Get it reviewed (by Sree, in chat) before removing the flag.
4. Remove `draft: true`, commit, push. It's live once the deploy finishes
   (roughly 90–160 seconds; poll rather than assuming).

**`draft: true` 404s in production and looks exactly like a broken deploy** —
this has caused a real misdiagnosis before (checked build logs, compared
commits, suspected a Vercel failure) when the actual cause was six posts still
carrying the flag. Before concluding anything about a failed deploy, check
for stray drafts:

```bash
grep -l '^draft: true' pocket-dating-coach/src/lib/blog/posts/*.md
```

`formatting-reference.md` is the one intentional permanent exception — a
dev-only rendering reference that's never meant to go live.

## Never push straight to production without asking

Pushing to the repo's main branch deploys. Per this agent's own operating
rules (not specific to this blog): publishing or modifying public content
needs an explicit go-ahead in chat first, every time, even for a `draft:
true` post — a draft that's committed can still be un-drafted by anyone with
push access later, and pushing at all touches shared repo state. Write and
commit locally; ask before the push that puts it in front of the deploy
pipeline, and ask again separately before removing `draft: true`.

## Tag naming

**Never start a tag with `ai-`.** The label-rendering helper only capitalizes
the first word, so `ai-guardrails` renders on the page as "Ai guardrails."

Tags in current use: `agent-architecture`, `agentic-architecture`,
`agent-evals`, `context-engineering`, `guardrails`, `decision-systems`,
`data-platform`, `operations`, `marketing`, `advertising`, `meta`, plus
`riteangle` reserved for posts specifically about that product. There's no
enforced taxonomy beyond "don't start with `ai-`" — reuse an existing tag
where the topic genuinely matches one, rather than minting a near-duplicate.

## Share cards (OG images)

```bash
python3 pocket-dating-coach/scripts/blog-og-card.py <slug>
```

Generates `static/og/blog/<slug>.png` at 1200×630 and prints the `cover:`
line to paste into the post's frontmatter. Run this for every post meant to
go live — without a `cover:`, a post falls back to the generic product logo,
which is off-brand and identical on every share.

For a post with a genuine pipeline (roughly a third of posts fit this), a
richer pipeline-shaped card is available:

```bash
python3 pocket-dating-coach/scripts/blog-og-card.py <slug> \
  --flow "Stage|sub||Stage|Model name|ai||Stage|sub" \
  --loop "label under the retry arc"
```

`||` separates stages; `|` separates label/sub/kind within a stage. Kind
`ai` fills the box in the accent color (the one visual distinction still
legible at thumbnail size — use it to mark which stages actually run a
model, and name the real model in the sub-label). The plain title card is
the better default for posts without a clear pipeline shape.

**LinkedIn ignores an `og:image` with no declared width/height, silently** —
it falls back to the default card with no error reported anywhere, so a
missing dimension is invisible until you notice the wrong card. The site's
`Seo.svelte` component already emits `og:image:width`/`height`/`type`/`alt`
for every post — don't remove them, and don't skip generating a `cover:` for
a new post assuming the fallback is fine.

LinkedIn also caches a card per URL, and **the `?v=2` query-string trick does
not work on this site** — confirmed by testing on 2026-08-25, after two rounds
of it failing to refresh a card. The reason: every post emits an `og:url` (and
a `rel=canonical`) pointing at the clean URL. LinkedIn canonicalizes to
`og:url`, so it scrapes `…/slug?v=3`, reads the clean URL out of the metadata,
and serves the cache entry it already holds for that. The query string changes
nothing it keys on.

The fix that does work is **LinkedIn Post Inspector**:

    https://www.linkedin.com/post-inspector/

Paste the clean post URL and hit Inspect. It force-refreshes the cache
immediately, and the next paste into a composer picks up the new card.

Two related traps found in the same session:

- **LinkedIn caches the image URL separately from the page.** Regenerating a
  card in place — same filename, new bytes — leaves the old image being served
  even after the page cache clears. When a card genuinely changes, write it to
  a new filename and repoint `cover:` at it, rather than overwriting.
- **Changing a post's title does not change its card** unless the card is
  regenerated, because the card bakes the title in as pixels at generation
  time. Re-run the generator after any retitle.

## Writing the LinkedIn post that carries a piece

Sree posts most pieces to LinkedIn by hand and asks for the copy. Conventions,
all from corrections on 2026-08-25:

- **Roughly 1,350–1,550 characters.** A 2,050-character draft was rejected as
  too long and cut by half. Buy space by dropping the third-best point, not by
  compressing everything into denser prose.
- **Four or five emoji, doing structural work.** Sparse and professional. They
  belong as list markers on the parallel items and one on the link line, never
  sprinkled through prose. "Sparsely and professionally" was the instruction.
- **No em dashes**, matching the outreach style rules in `job-hunt-agent`.
  Colons, periods and commas instead.
- **End on a genuine question**, also from the outreach rules. Not "thoughts?"
  — a real one the reader could answer.
- **Mind the fold.** LinkedIn truncates around 210 characters. The thesis has
  to land above it; the click-to-expand should feel earned.
- **Past tense for anything at a former employer.** "A voice agent I built,"
  never "I run."
- **Three to five hashtags on their own line at the end.** Mix reach with
  precision. More than five reads as spam. Skip hashtags for niche tools named
  in the body already — they add no discovery.
- **No company names**, Sree's or anyone else's, same as the post itself.

The strongest structure so far: thesis, then the concrete incident that proves
it, then the parallel list, then the one counter-intuitive concession that
makes it credible, then a one-line aphorism, then the link and the question.

## Diagrams

See STYLE.md's Diagrams section for when and how to draw one. Files go in
`pocket-dating-coach/static/blog/*.svg`, referenced from the post as
`![alt](/blog/name.svg)`.

## Checking an SVG before it ships

`qlmanage -t` is the only renderer on this machine (no rsvg-convert, no
cairosvg, no ImageMagick), and it renders into a **square** thumbnail, so a
portrait diagram gets cropped and the bottom third is never seen. Two arrow/label
collisions shipped past a first look this way.

To see the whole thing, render it in bands by rewriting the viewBox on a copy:

```bash
sed 's|viewBox="0 0 560 800"|viewBox="0 390 560 410"|' d.svg > crop.svg
qlmanage -t -s 1400 -o . crop.svg
```

Check every band before embedding the `![alt](/blog/name.svg)` reference.

## Which branch deploys

`development` and `main` track together and both sit at the same commit; the
remote HEAD is `main`, and `main` is what deploys. Commit on `development`,
then push the same commit to both:

```bash
git push origin development
git push origin development:main
```

Always stage with explicit pathspecs — that repo's working tree is shared with
other sessions and usually has unrelated modified files and untracked scripts
sitting in it.

## Known infrastructure traps (only relevant if touching the blog's code, not its content)

- The subdomain rewrite depends on a root catch-all route
  (`src/routes/[...unmatched]/`) existing in the SvelteKit app — it looks like
  dead code and is load-bearing. Don't delete it.
- Pages are deliberately not prerendered; turning prerendering on breaks the
  subdomain rewrite.
- Concurrent sessions share one working tree and git index in that repo —
  always `git add` with explicit pathspecs, never a broad `git add -A`, or
  another session's in-progress work can get swept into your commit.

These are here for completeness; writing and publishing a post normally never
touches any of this.
