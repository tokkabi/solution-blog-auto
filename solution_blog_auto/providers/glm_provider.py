class GLMProvider:
    """Dummy GLM provider for the MVP workflow."""

    def generate(self, prompt: str) -> str:
        """Return a dummy GLM response."""
        return "[GLM] Dummy Response"
