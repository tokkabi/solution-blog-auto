from solution_blog_auto.core.config import Config
from solution_blog_auto.providers.base import Provider
from solution_blog_auto.providers.gemini_provider import GeminiProvider
from solution_blog_auto.providers.glm_provider import GLMProvider
from solution_blog_auto.providers.ollama_provider import OllamaProvider
from solution_blog_auto.providers.openai_provider import OpenAIProvider
from solution_blog_auto.providers.openrouter_provider import OpenRouterProvider


class ProviderFactory:
    """Create LLM provider instances from application settings."""

    @staticmethod
    def create(settings: Config) -> Provider:
        """Create a provider for the configured LLM provider name."""
        provider_name = settings.llm_provider.lower()

        providers: dict[str, type[Provider]] = {
            "openai": OpenAIProvider,
            "openrouter": OpenRouterProvider,
            "glm": GLMProvider,
            "gemini": GeminiProvider,
            "ollama": OllamaProvider,
        }

        provider_class = providers.get(provider_name)
        if provider_class is None:
            raise ValueError(f"Unsupported LLM provider: {settings.llm_provider}")

        return provider_class()
