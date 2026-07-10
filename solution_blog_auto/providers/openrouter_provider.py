class OpenRouterProvider:
    """Dummy OpenRouter provider for the MVP workflow."""

    def generate(self, prompt: str) -> str:
        """Return a dummy OpenRouter response."""
        return "[OpenRouter] Dummy Response"
