"""Sanity checks for documentation files and navigation."""

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent.parent


def _navigation_pages(value):
    if isinstance(value, str):
        if value.endswith(".md"):
            yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from _navigation_pages(child)
    elif isinstance(value, list):
        for child in value:
            yield from _navigation_pages(child)


def test_repository_documentation_files_exist():
    assert (ROOT / "README.md").is_file()
    assert (ROOT / "mkdocs.yml").is_file()
    assert (ROOT / "docs").is_dir()


def test_navigation_pages_exist():
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    docs_root = ROOT / config.get("docs_dir", "docs")

    for page in _navigation_pages(config["nav"]):
        assert (docs_root / page).is_file(), f"Missing navigation page: {page}"
