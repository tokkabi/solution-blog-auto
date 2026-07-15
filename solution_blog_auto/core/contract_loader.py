from pathlib import Path


class ContractLoader:
    """Load output contract templates from the project contracts directory."""

    def __init__(self, contracts_dir: Path | None = None) -> None:
        """Initialize the loader with the project contracts directory."""
        project_root = Path(__file__).resolve().parents[2]
        self.contracts_dir = contracts_dir or project_root / "contracts"

    def load(self, name: str) -> str:
        """Load a contract template as raw text.

        Args:
            name: Contract file name, e.g. ``01_story.md``.

        Returns:
            The full markdown content of the contract.

        Raises:
            FileNotFoundError: When the contract file does not exist.
        """
        contract_path = self.contracts_dir / name

        if not contract_path.is_file():
            raise FileNotFoundError(f"Contract file not found: {name}")

        return contract_path.read_text(encoding="utf-8")
