from pathlib import Path


class PromptLoader:
    """Load prompt templates from the project prompts directory."""

    def __init__(self, prompts_dir: Path | None = None) -> None:
        """Initialize the loader with the project prompts directory."""
        project_root = Path(__file__).resolve().parents[2]
        self.prompts_dir = prompts_dir or project_root / "prompts"

    def load(self, name: str, **values: str) -> str:
        """Load a prompt template and replace placeholders with values."""
        prompt_path = self.prompts_dir / name

        if not prompt_path.is_file():
            raise FileNotFoundError(f"Prompt file not found: {name}")

        template = prompt_path.read_text(encoding="utf-8")
        return template.format(**values)
