# What never gets published

Check this before drafting, not after. The rule that governs all of it:
**publish the shape, never the coordinates** — the mechanism and the pattern
are the post; the specific people, companies, and numbers behind them usually
are not.

## Hard no-publish zones

These come from mining `~/Desktop/Career Hacking` for the personal
career-narrative sub-series, but the underlying rule applies to any source
material, including other projects' data:

- **Any material describing real third parties' sensitive circumstances** —
  the concrete case that triggered this rule was mass-tort intake material
  involving child-safety claims. Never publishable at any level of
  redaction; this isn't a category where "generalize it enough" is a valid
  fix. If source material contains this kind of content, it doesn't get
  mined for a post at all, not even the abstracted shape of it.
- **Named individuals attached to layoff, salary-cut, or performance-review
  decisions.** Mechanism only — how a decision process worked — never who it
  was applied to.
- **Comp figures at the level of an actual payout** (a specific salary, a
  specific cut, a specific bonus). Round, redirect to a ratio, or drop
  entirely; don't publish the number.
- **Household/family financial detail** — if source material interleaves
  career strategy with personal finances (a savings target, a loan, a
  family member's income), that layer gets trimmed out before anything is
  quoted, even a dated diary entry that otherwise reads as harmless.

## PII checklist for any post about a running system

This is the relevant list for posts about active tools (job-hunt-agent,
PDC internals, any other project), not just the personal-narrative sub-series:

- No real company names being targeted or researched by a system, unless
  the post is *about* a public company's own public statement (e.g. citing a
  named conference talk someone else gave publicly).
- No real contact names, emails, phone numbers, or LinkedIn profile URLs.
- No real comp numbers, funding amounts tied to a specific deal, or specific
  dates that would let someone reconstruct which real entity is being
  discussed.
- No code identifiers per [STYLE.md](STYLE.md)'s register rule — this is
  also a mild privacy/security habit, not just a style one: a file or
  function name is a pointer into a private repo that a public reader has no
  business needing.
- Ledger/ticket/record contents (the actual rows of a spreadsheet, the actual
  text of a message someone sent) stay out. Describe what a row *contains as
  a category* ("a contact, a channel, an outcome"), never an actual row.

If a draft needs a concrete-feeling example to satisfy the "examples on both
sides" rule in STYLE.md, invent a plausible one and don't present it as real
— or use a genuinely public data point (a named conference talk, a published
paper) instead of a private one.

## Sree's own personal material is not fair game either

The rules above are about other people. This one is about Sree, and it was
learned the hard way on 2026-08-25, after a published post drew on a personal
diary that sits inside a work corpus. The instruction:

> *"Throughout the blog, try to remove the personal aspects out of the
> equation. I don't think people will be entertained or challenged by it. But
> it can be there to prove a point, not to overly showcase it — it might make
> people uncomfortable."*

So the test is not "is this Sree's to share" — legally and ethically it is. The
test is **whether the reader learns something from it that the professional
version of the same point would not teach.** Almost always they do not, and the
personal detail costs the reader's comfort for nothing.

Concretely, the draft that triggered this opened on a professional-contacts
query returning a family member, and went on to describe relationship typing
across colleagues, clinicians, family and dating contacts. Every fact was
Sree's own. It still came out. The same architectural point — that a schema can
make a wrong answer unrepresentable where a filter cannot — survived intact as
one short paragraph about work contacts and personal contacts, followed by a
table of domain examples from healthcare, fraud and recruiting.

Rules of thumb:

- **Prefer a business incident to a personal one when both prove the point.**
  The rewritten post opened on a stale metric reaching a draft instead. Better
  hook, no discomfort.
- **One clause, not a section.** If personal material genuinely sharpens an
  argument, it earns a sentence. It does not earn a worked example, a diagram,
  or a heading.
- **Never the opening.** An opening scene sets what the post is about, and a
  personal one tells the reader they are here to read about Sree's life.
- **Categories, never instances.** "Work contacts and personal contacts" is
  fine. Naming the kinds of personal contact, or a family relationship, is not.
- **Health, family, relationships, and money are out entirely**, even
  abstracted, even when Sree's own.

When in doubt, write the professional version first and see whether anything is
actually lost. Usually nothing is.

## Third-party material generally

See [STYLE.md](STYLE.md)'s "Third-party material" section for the mechanics
(anonymize, invent figures, generalize the domain, disclose in an italic
note). The gate before any of that is: flag it in chat and get an explicit
go-ahead before publishing, every time. This is not a call to make solo, and
it does not become one just because a similar post was approved before —
each instance gets its own check.

## When in doubt

If a piece of source material could plausibly identify a real person, a real
company, or a real financial figure, and there's any doubt about whether
removing it changes the point of the post — ask, rather than publish a
redacted guess. A post that's slightly less concrete because a detail was
cut is a fine outcome. A post that leaks something it shouldn't have is not
one you can undo by editing the file after the fact; readers, feed scrapers,
and search-engine caches may already have it.
