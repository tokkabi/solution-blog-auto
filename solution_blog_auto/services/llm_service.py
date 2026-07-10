from solution_blog_auto.core.config import Config
from solution_blog_auto.providers.factory import ProviderFactory


class LLMService:
    """Generate text through the configured LLM provider."""

    def __init__(self, settings: Config | None = None) -> None:
        """Initialize the service with application settings."""
        self.settings = settings or Config()

    def generate(self, prompt: str) -> str:
        """Generate text from a prompt using the selected provider."""
        provider = ProviderFactory.create(self.settings)
        return provider.generate(prompt)
