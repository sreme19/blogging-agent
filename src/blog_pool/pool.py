"""Write side of the topic pool: resources/ and IDEAS.md.

Deliberately a *capture* tool, not a writing one. It records that work happened
and where, so a later blogging-agent session can pull the detail and draft it
against STYLE.md and SAFETY.md. Nothing here reads those files, and nothing here
produces prose -- keeping the judgment in the session is the entire reason the
blog rules live in this folder rather than in each work repo.

What it stores is a **pointer, not a payload**: repo, commit sha, commit
subjects. Never a diff, never code. The pool stays readable, and the detail is
fetched at draft time from the repo itself, which by then may have moved on --
the sha is what makes that fetch honest.
"""
from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DEFAULT_POOL = Path(__file__).resolve().parents[2] / "topic-pool"
DEFAULT_CODE_ROOT = Path("~/Desktop/Code").expanduser()
MAX_SUBJECTS = 30


class PoolError(Exception):
    """Anything that should stop the write with a readable message."""


@dataclass
class RepoFacts:
    name: str
    sha: str
    last_commit: str
    subjects: list[str]


def slugify(text: str, limit: int = 60) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if len(s) <= limit:
        return s
    # Cut on a word boundary so the slug stays readable as a filename.
    return s[:limit].rsplit("-", 1)[0]


def _git(repo: Path, *args: str) -> str:
    try:
        out = subprocess.run(["git", "-C", str(repo), *args], check=False,
                             capture_output=True, text=True, timeout=15)
    except (OSError, subprocess.SubprocessError) as exc:
        raise PoolError(f"git failed in {repo}: {exc}") from exc
    if out.returncode != 0:
        raise PoolError(f"git {' '.join(args)} failed in {repo}: {out.stderr.strip()}")
    return out.stdout.strip()


def repo_facts(name: str, code_root: Path = DEFAULT_CODE_ROOT,
               commits: str = "") -> RepoFacts:
    """HEAD sha, last commit date and the subjects in `commits`, for one repo.

    Fails closed on anything that is not a git checkout. A pool entry whose
    provenance is "some folder" is worse than no entry: the whole point of
    recording the sha is that a drafting session can go back and read the real
    change months later.
    """
    repo = (code_root / name).expanduser()
    if not repo.is_dir():
        raise PoolError(f"no such repo: {repo}")
    if not (repo / ".git").exists():
        raise PoolError(f"{name} is not a git checkout — nothing to cite as provenance")
    sha = _git(repo, "rev-parse", "HEAD")[:12]
    last_commit = _git(repo, "log", "-1", "--format=%cs")
    log_args = ["log", f"--max-count={MAX_SUBJECTS}", "--format=%h %s"]
    log_args.append(commits if commits else "-1")
    subjects = [ln for ln in _git(repo, *log_args).splitlines() if ln.strip()]
    return RepoFacts(name=name, sha=sha, last_commit=last_commit, subjects=subjects)


def resource_body(facts: RepoFacts, title: str, angle: str, commits: str,
                  note: str, today: str) -> str:
    lines = [
        "---",
        f"title: {title}",
        f"source: repo:{facts.name}@{facts.sha}",
        # `own-work` rather than transcript/article: SAFETY.md's rules for
        # handling other people's material do not apply to your own repo, while
        # its coordinates rule still does. The drafting session needs to know
        # which of the two it is looking at.
        "type: own-work",
        f"ingested: {today}",
        f"repo: {facts.name}",
        f"commits: {commits or facts.sha}",
        f"last_commit: {facts.last_commit}",
        "---",
        "",
        "## Angle",
        "",
        angle,
        "",
        "## What was done",
        "",
    ]
    lines += [f"- `{s}`" for s in facts.subjects] or ["- (no commits in range)"]
    if note:
        lines += ["", "## Note", "", note]
    lines += [
        "",
        "## Pulling the detail",
        "",
        (f"This is a pointer, not a capture. Read the real change at "
         f"`{facts.name}` @ `{commits or facts.sha}` when drafting; the working "
         f"tree will have moved on, the sha will not."),
        "",
    ]
    return "\n".join(lines)


def write_resource(facts: RepoFacts, *, title: str, angle: str, commits: str = "",
                   note: str = "", pool_dir: Path = DEFAULT_POOL,
                   today: str = "", force: bool = False) -> Path:
    today = today or datetime.now().astimezone().date().isoformat()
    res_dir = pool_dir / "resources"
    res_dir.mkdir(parents=True, exist_ok=True)
    path = res_dir / f"{today}-{slugify(title)}.md"
    if path.exists() and not force:
        raise PoolError(f"{path.name} already exists — use a different --title, or --force")
    path.write_text(resource_body(facts, title, angle, commits, note, today))
    return path


def append_idea(resource: Path, *, angle: str, facts: RepoFacts,
                pool_dir: Path = DEFAULT_POOL, today: str = "") -> Path:
    """Add one `- [ ]` angle under today's heading, creating the heading if new.

    Sections are newest-first, so a new date goes immediately above the most
    recent one rather than at the end of the file. The existing structure --
    intro prose, then dated sections, each with a `_From [...]_` provenance line
    -- is preserved rather than reformatted: this file is read by a person and by
    the /blog-topics command, and both expect that shape.
    """
    today = today or datetime.now().astimezone().date().isoformat()
    ideas = pool_dir / "IDEAS.md"
    if not ideas.exists():
        raise PoolError(f"{ideas} is missing — the pool is not set up here")
    text = ideas.read_text()
    rel = f"resources/{resource.name}"
    entry = (f"_From [{resource.stem}]({rel})\n"
             f"(own work — {facts.name} @ {facts.sha}):_\n\n"
             f"- [ ] **{angle}**\n")

    heading = f"## {today}"
    lines = text.splitlines(keepends=True)
    if heading in text:
        # Append at the end of today's section, before the next `## ` or EOF.
        start = next(i for i, ln in enumerate(lines) if ln.rstrip("\n") == heading)
        end = next((i for i in range(start + 1, len(lines))
                    if lines[i].startswith("## ")), len(lines))
        while end > start + 1 and not lines[end - 1].strip():
            end -= 1
        lines.insert(end, "\n" + entry)
    else:
        first = next((i for i, ln in enumerate(lines) if ln.startswith("## ")), len(lines))
        lines.insert(first, f"{heading}\n\n{entry}\n")
    ideas.write_text("".join(lines))
    return ideas


def summarise(pool_dir: Path = DEFAULT_POOL) -> dict:
    ideas = pool_dir / "IDEAS.md"
    text = ideas.read_text() if ideas.exists() else ""
    res_dir = pool_dir / "resources"
    resources = sorted(p.name for p in res_dir.glob("*.md")) if res_dir.is_dir() else []
    return {
        "open": text.count("- [ ]"),
        "used": text.count("- [x]"),
        "resources": resources,
    }
