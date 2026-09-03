"""The pool is append-only and provenance-carrying; these are the rules that matter."""
from __future__ import annotations

import subprocess

import pytest

from blog_pool.pool import (
    PoolError,
    append_idea,
    repo_facts,
    slugify,
    summarise,
    write_resource,
)

IDEAS_SEED = """# Candidate post angles — sree.riteangle.dating

Running list of blog angles drawn from ingested resources.

## 2026-08-27

_From [older](resources/older.md)
(public podcast — external reference only):_

- [ ] **An existing angle**
"""


@pytest.fixture
def pool(tmp_path):
    d = tmp_path / "topic-pool"
    (d / "resources").mkdir(parents=True)
    (d / "IDEAS.md").write_text(IDEAS_SEED)
    return d


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "code"
    r = root / "agent-ready-data"
    r.mkdir(parents=True)
    (r / "README.md").write_text("x")
    def run(*a):
        subprocess.run(["git", "-C", str(r), *a], capture_output=True, check=True)

    run("init", "-q", "-b", "main")
    run("config", "user.email", "t@example.com")
    run("config", "user.name", "T")
    run("add", "-A")
    run("commit", "-qm", "Add freshness metadata to the catalog output")
    return root


def test_slug_cuts_on_a_word_boundary():
    s = slugify("Freshness metadata as a first-class column output for agent readers")
    assert s == "freshness-metadata-as-a-first-class-column-output-for-agent"
    assert len(s) <= 60
    assert not s.endswith("-")


def test_records_provenance_from_the_repo(pool, repo):
    facts = repo_facts("agent-ready-data", repo)
    path = write_resource(facts, title="Freshness as a column",
                          angle="Freshness metadata belongs in the output",
                          pool_dir=pool, today="2026-09-03")
    body = path.read_text()
    assert path.name == "2026-09-03-freshness-as-a-column.md"
    assert f"source: repo:agent-ready-data@{facts.sha}" in body
    assert "type: own-work" in body
    assert "Add freshness metadata to the catalog output" in body


def test_stores_a_pointer_not_a_payload(pool, repo):
    """Commit subjects, never a diff -- the detail is pulled at draft time."""
    facts = repo_facts("agent-ready-data", repo)
    body = write_resource(facts, title="T", angle="A", pool_dir=pool).read_text()
    assert "diff" not in body.lower()
    assert "Pulling the detail" in body


def test_fails_closed_on_a_folder_that_is_not_a_checkout(tmp_path):
    root = tmp_path / "code"
    (root / "scratch").mkdir(parents=True)
    with pytest.raises(PoolError, match="not a git checkout"):
        repo_facts("scratch", root)


def test_missing_repo_is_an_error(tmp_path):
    with pytest.raises(PoolError, match="no such repo"):
        repo_facts("nope", tmp_path)


def test_never_silently_overwrites(pool, repo):
    facts = repo_facts("agent-ready-data", repo)
    kw = {"title": "Same", "angle": "A", "pool_dir": pool, "today": "2026-09-03"}
    write_resource(facts, **kw)
    with pytest.raises(PoolError, match="already exists"):
        write_resource(facts, **kw)
    write_resource(facts, force=True, **kw)      # explicit is fine


def test_new_date_section_goes_above_the_previous_one(pool, repo):
    facts = repo_facts("agent-ready-data", repo)
    res = write_resource(facts, title="T", angle="A", pool_dir=pool, today="2026-09-03")
    append_idea(res, angle="A new angle", facts=facts, pool_dir=pool, today="2026-09-03")
    text = (pool / "IDEAS.md").read_text()
    assert text.index("## 2026-09-03") < text.index("## 2026-08-27")
    assert "- [ ] **A new angle**" in text
    assert "- [ ] **An existing angle**" in text      # the old section survives


def test_second_angle_same_day_joins_that_section(pool, repo):
    facts = repo_facts("agent-ready-data", repo)
    for n in ("One", "Two"):
        res = write_resource(facts, title=n, angle=n, pool_dir=pool, today="2026-09-03")
        append_idea(res, angle=n, facts=facts, pool_dir=pool, today="2026-09-03")
    text = (pool / "IDEAS.md").read_text()
    assert text.count("## 2026-09-03") == 1
    body = text.split("## 2026-09-03")[1].split("## 2026-08-27")[0]
    assert "**One**" in body and "**Two**" in body


def test_summarise_counts_open_and_used(pool, repo):
    facts = repo_facts("agent-ready-data", repo)
    res = write_resource(facts, title="T", angle="A", pool_dir=pool, today="2026-09-03")
    append_idea(res, angle="A", facts=facts, pool_dir=pool, today="2026-09-03")
    s = summarise(pool)
    assert s["open"] == 2 and s["used"] == 0
    assert s["resources"] == ["2026-09-03-t.md"]
