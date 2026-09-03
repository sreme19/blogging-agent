"""blog-pool — log work done in another repo as a candidate post angle.

No network, no credentials, no Anthropic API key. This CLI only writes into
`topic-pool/`: one resource file plus one line in IDEAS.md. It never drafts,
never publishes, and never touches the blog itself -- posts live in
`pocket-dating-coach/src/lib/blog/posts/` and getting one there is a separate,
human-gated act (see PUBLISHING.md).

Why it exists: the judgment that a piece of work is worth writing about lasts
about an hour, in the session where the work happened. The corpus can only ever
retrieve prose that somebody already wrote down. So the pointer gets pushed at
the time, and the payload gets pulled at draft time.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from blog_pool.pool import (
    DEFAULT_CODE_ROOT,
    DEFAULT_POOL,
    PoolError,
    append_idea,
    repo_facts,
    summarise,
    write_resource,
)


def cmd_add(args: argparse.Namespace) -> int:
    pool = Path(args.pool).expanduser() if args.pool else DEFAULT_POOL
    code_root = Path(args.code_root).expanduser() if args.code_root else DEFAULT_CODE_ROOT
    facts = repo_facts(args.repo, code_root, args.commits or "")
    title = args.title or args.angle
    resource = write_resource(
        facts, title=title, angle=args.angle, commits=args.commits or "",
        note=args.note or "", pool_dir=pool, force=args.force,
    )
    ideas = append_idea(resource, angle=args.angle, facts=facts, pool_dir=pool)
    print(f"resource: {resource}")
    print(f"ideas:    {ideas}")
    print(f"provenance: {facts.name} @ {facts.sha} ({len(facts.subjects)} commit(s))")
    print("\nDraft it from a session rooted here, so STYLE.md and SAFETY.md apply.")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    pool = Path(args.pool).expanduser() if args.pool else DEFAULT_POOL
    s = summarise(pool)
    print(f"{s['open']} open angle(s), {s['used']} used, {len(s['resources'])} resource(s)")
    for name in s["resources"][-10:]:
        print(f"  {name}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="blog-pool",
        description="Log work from another repo into the sree.riteangle.dating topic pool.",
    )
    # `--pool` hangs off each subcommand rather than the top level, so
    # `blog-pool add --pool ...` works. On the main parser argparse requires it
    # before the subcommand, which is not how anyone types it.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--pool", help="Topic pool directory (default: this repo's).")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add", parents=[common],
                         help="Record work from a repo as a candidate angle.")
    add.add_argument("--repo", required=True, help="Repo directory name under the code root.")
    add.add_argument("--angle", required=True, help="What the post would actually argue.")
    add.add_argument("--commits", help="Commit range, e.g. a1b2c3..d4e5f6. Defaults to HEAD.")
    add.add_argument("--title", help="Resource title; defaults to the angle.")
    add.add_argument("--note", help="Anything the commit subjects will not tell a reader.")
    add.add_argument("--code-root", help="Where the repos live (default: ~/Desktop/Code).")
    add.add_argument("--force", action="store_true", help="Overwrite an existing resource file.")
    add.set_defaults(func=cmd_add)

    ls = sub.add_parser("list", parents=[common], help="What is already in the pool.")
    ls.set_defaults(func=cmd_list)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except PoolError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
