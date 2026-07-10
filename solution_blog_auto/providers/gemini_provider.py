class GeminiProvider:
    """Dummy Gemini provider for the MVP workflow."""

    def generate(self, prompt: str) -> str:
        """Return a dummy Gemini response."""
        return "[Gemini] Dummy Response"
