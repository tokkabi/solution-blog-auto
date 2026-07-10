class OpenAIProvider:
    """Dummy OpenAI provider for the MVP workflow."""

    def generate(self, prompt: str) -> str:
        """Return a dummy OpenAI response."""
        return "[OpenAI] Dummy Response"
