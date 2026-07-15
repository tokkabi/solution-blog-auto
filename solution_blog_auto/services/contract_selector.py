import json
from pathlib import Path


class ContractSelector:
    """Select output contracts in a round-robin order.

    The current position is persisted in a JSON state file so that the
    selection continues across separate runs of the CLI program.
    """

    _ORDER: list[str] = [
        "01_story.md",
        "02_faq.md",
        "03_guide.md",
        "04_comparison.md",
        "05_listicle.md",
    ]

    def __init__(self, state_path: Path | None = None) -> None:
        """Initialize the selector with the path to its state file.

        Args:
            state_path: Location of the round-robin counter file. Defaults to
                ``runtime/contract_state.json`` under the project root.
        """
        project_root = Path(__file__).resolve().parents[2]
        self.state_path = state_path or project_root / "runtime" / "contract_state.json"

    def next_contract(self) -> str:
        """Return the next contract file name and advance the counter.

        When the last contract is reached, the cycle restarts from the first.

        Returns:
            The next contract file name in round-robin order.
        """
        index = self._read_index()
        name = self._ORDER[index % len(self._ORDER)]
        self._write_index(index + 1)
        return name

    def _read_index(self) -> int:
        """Read the persisted counter, defaulting to 0 when absent."""
        if not self.state_path.is_file():
            return 0

        data = json.loads(self.state_path.read_text(encoding="utf-8"))
        return int(data.get("index", 0))

    def _write_index(self, index: int) -> None:
        """Persist the counter, creating the parent directory if needed."""
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        payload = json.dumps({"index": index})
        self.state_path.write_text(payload, encoding="utf-8")
