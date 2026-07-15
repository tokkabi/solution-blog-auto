import json
from pathlib import Path

from solution_blog_auto.services.contract_selector import ContractSelector


def test_contract_selector_starts_from_first_when_no_state(tmp_path: Path) -> None:
    """Contract selector should start at index 0 when no state file exists."""
    selector = ContractSelector(state_path=tmp_path / "contract_state.json")

    name = selector.next_contract()

    assert name == "01_story.md"


def test_contract_selector_cycles_round_robin(tmp_path: Path) -> None:
    """Contract selector should cycle through all contracts and restart."""
    selector = ContractSelector(state_path=tmp_path / "contract_state.json")

    names = [selector.next_contract() for _ in range(7)]

    assert names == [
        "01_story.md",
        "02_faq.md",
        "03_guide.md",
        "04_comparison.md",
        "05_listicle.md",
        "01_story.md",
        "02_faq.md",
    ]


def test_contract_selector_creates_runtime_directory(tmp_path: Path) -> None:
    """Contract selector should create the runtime directory if it does not exist."""
    state_path = tmp_path / "runtime" / "contract_state.json"
    selector = ContractSelector(state_path=state_path)

    selector.next_contract()

    assert state_path.is_file()


def test_contract_selector_persists_index(tmp_path: Path) -> None:
    """Contract selector should persist the counter across instances."""
    state_path = tmp_path / "contract_state.json"

    ContractSelector(state_path=state_path).next_contract()
    name = ContractSelector(state_path=state_path).next_contract()

    saved = json.loads(state_path.read_text(encoding="utf-8"))
    assert saved["index"] == 2
    assert name == "02_faq.md"
