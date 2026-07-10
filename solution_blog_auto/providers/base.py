from typing import Protocol


class Provider(Protocol):
    """Common interface for LLM providers."""

    def generate(self, prompt: str) -> str:
        """Generate text from a prompt."""
