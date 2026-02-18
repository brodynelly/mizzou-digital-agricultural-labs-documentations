"""Basic sanity checks for documentation files."""
import pathlib

ROOT = pathlib.Path(__file__).parent


def test_readme_exists():
    assert (ROOT / "README.md").exists()


def test_mkdocs_config_exists():
    assert (ROOT / "mkdocs.yml").exists()


def test_docs_directory_exists():
    assert (ROOT / "docs").is_dir()
