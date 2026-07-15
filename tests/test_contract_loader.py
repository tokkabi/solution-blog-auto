from pathlib import Path

import pytest

from solution_blog_auto.core.contract_loader import ContractLoader


def test_contract_loader_loads_from_project_root(monkeypatch, tmp_path) -> None:
    """Contract loader should find contracts without relying on the current directory."""
    monkeypatch.chdir(tmp_path)
    loader = ContractLoader()

    contract = loader.load("01_story.md")

    assert "스토리" in contract


def test_contract_loader_reads_exact_content(tmp_path: Path) -> None:
    """Contract loader should return the exact file content."""
    contracts_dir = tmp_path / "contracts"
    contracts_dir.mkdir()
    (contracts_dir / "01_story.md").write_text("# Story Template", encoding="utf-8")
    loader = ContractLoader(contracts_dir=contracts_dir)

    contract = loader.load("01_story.md")

    assert contract == "# Story Template"


def test_contract_loader_rejects_missing_file(tmp_path: Path) -> None:
    """Contract loader should raise a clear error for missing contract files."""
    loader = ContractLoader(contracts_dir=tmp_path)

    with pytest.raises(FileNotFoundError, match="Contract file not found"):
        loader.load("missing.md")
