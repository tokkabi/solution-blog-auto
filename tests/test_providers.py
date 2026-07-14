import pytest

from solution_blog_auto.core.config import Config
from solution_blog_auto.providers.factory import ProviderFactory
from solution_blog_auto.providers.openrouter_provider import OpenRouterProvider


def test_provider_factory_creates_configured_provider() -> None:
    """Provider factory should create the selected dummy provider."""
    settings = Config(llm_provider="gemini")

    provider = ProviderFactory.create(settings)

    assert provider.generate("prompt") == "[Gemini] Dummy Response"


def test_provider_factory_rejects_unknown_provider() -> None:
    """Provider factory should reject unsupported provider names."""
    settings = Config(llm_provider="unknown")

    with pytest.raises(ValueError, match="Unsupported LLM provider"):
        ProviderFactory.create(settings)


def test_provider_factory_creates_openrouter_provider() -> None:
    """Provider factory should pass OpenRouter settings to the provider."""
    settings = Config(
        llm_provider="openrouter",
        openrouter_api_key="test-key",
        openrouter_model="test-model",
    )

    provider = ProviderFactory.create(settings)

    assert isinstance(provider, OpenRouterProvider)
    assert provider.api_key == "test-key"
    assert provider.model == "test-model"
