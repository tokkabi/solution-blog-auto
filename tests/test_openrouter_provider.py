import httpx
import pytest

from solution_blog_auto.providers.openrouter_provider import OpenRouterProvider


class FakeClient:
    """Fake httpx client for OpenRouter provider tests."""

    last_timeout: float | None = None
    last_url: str | None = None
    last_headers: dict[str, str] | None = None
    last_json: dict[str, object] | None = None
    response = httpx.Response(
        200,
        json={"choices": [{"message": {"content": "Generated markdown"}}]},
    )

    def __init__(self, timeout: float) -> None:
        """Store the configured timeout."""
        self.__class__.last_timeout = timeout

    def __enter__(self) -> "FakeClient":
        """Enter the fake client context."""
        return self

    def __exit__(self, *args: object) -> None:
        """Exit the fake client context."""

    def post(
        self,
        url: str,
        headers: dict[str, str],
        json: dict[str, object],
    ) -> httpx.Response:
        """Capture the request and return the fake response."""
        self.__class__.last_url = url
        self.__class__.last_headers = headers
        self.__class__.last_json = json
        return self.__class__.response


def test_openrouter_provider_calls_chat_completions(monkeypatch) -> None:
    """OpenRouter provider should call Chat Completions with the prompt."""
    monkeypatch.setattr(httpx, "Client", FakeClient)
    provider = OpenRouterProvider(
        api_key="test-key",
        model="deepseek/deepseek-chat-v3-0324:free",
        timeout_seconds=10.0,
    )

    result = provider.generate("Write markdown")

    assert result == "Generated markdown"
    assert FakeClient.last_timeout == 10.0
    assert FakeClient.last_url == OpenRouterProvider.api_url
    assert FakeClient.last_headers == {
        "Authorization": "Bearer test-key",
        "Content-Type": "application/json",
    }
    assert FakeClient.last_json == {
        "model": "deepseek/deepseek-chat-v3-0324:free",
        "messages": [{"role": "user", "content": "Write markdown"}],
    }


def test_openrouter_provider_rejects_missing_api_key() -> None:
    """OpenRouter provider should explain missing API keys clearly."""
    provider = OpenRouterProvider(api_key="", model="test-model")

    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        provider.generate("prompt")


def test_openrouter_provider_rejects_missing_model() -> None:
    """OpenRouter provider should explain missing models clearly."""
    provider = OpenRouterProvider(api_key="test-key", model="")

    with pytest.raises(ValueError, match="OPENROUTER_MODEL"):
        provider.generate("prompt")


def test_openrouter_provider_reports_http_error() -> None:
    """OpenRouter provider should include the API error message."""
    provider = OpenRouterProvider(api_key="test-key", model="test-model")
    response = httpx.Response(
        401,
        json={"error": {"message": "Invalid API key"}},
    )

    with pytest.raises(RuntimeError, match="Invalid API key"):
        provider._parse_response(response)


def test_openrouter_provider_reports_timeout(monkeypatch) -> None:
    """OpenRouter provider should explain timeout failures."""

    class TimeoutClient(FakeClient):
        def post(
            self,
            url: str,
            headers: dict[str, str],
            json: dict[str, object],
        ) -> httpx.Response:
            raise httpx.TimeoutException("timeout")

    monkeypatch.setattr(httpx, "Client", TimeoutClient)
    provider = OpenRouterProvider(api_key="test-key", model="test-model")

    with pytest.raises(RuntimeError, match="timed out"):
        provider.generate("prompt")


def test_openrouter_provider_requires_content() -> None:
    """OpenRouter provider should require choices[0].message.content."""
    provider = OpenRouterProvider(api_key="test-key", model="test-model")
    response = httpx.Response(200, json={"choices": [{"message": {}}]})

    with pytest.raises(RuntimeError, match=r"choices\[0\]\.message\.content"):
        provider._parse_response(response)
