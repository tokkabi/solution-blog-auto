from pathlib import Path

import pytest

from solution_blog_auto.core.prompt_loader import PromptLoader


def test_prompt_loader_loads_from_project_root(monkeypatch, tmp_path) -> None:
    """Prompt loader should find prompts without relying on the current directory."""
    monkeypatch.chdir(tmp_path)
    loader = PromptLoader()

    prompt = loader.load("research.md", topic="ETF")

    assert "ETF" in prompt


def test_prompt_loader_replaces_multiple_values(tmp_path: Path) -> None:
    """Prompt loader should replace all provided placeholders."""
    prompts_dir = tmp_path / "prompts"
    prompts_dir.mkdir()
    (prompts_dir / "writer.md").write_text(
        "Topic: {topic}\nResearch: {research}",
        encoding="utf-8",
    )
    loader = PromptLoader(prompts_dir=prompts_dir)

    prompt = loader.load("writer.md", topic="ETF", research="Research result")

    assert prompt == "Topic: ETF\nResearch: Research result"


def test_prompt_loader_rejects_missing_file(tmp_path: Path) -> None:
    """Prompt loader should raise a clear error for missing prompt files."""
    loader = PromptLoader(prompts_dir=tmp_path)

    with pytest.raises(FileNotFoundError, match="Prompt file not found"):
        loader.load("missing.md")
