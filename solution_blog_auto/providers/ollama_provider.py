class OllamaProvider:
    """Dummy Ollama provider for the MVP workflow."""

    def generate(self, prompt: str) -> str:
        """Return a dummy Ollama response."""
        return "[Ollama] Dummy Response"
