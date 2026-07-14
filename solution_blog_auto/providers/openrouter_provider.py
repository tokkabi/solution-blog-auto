import httpx


class OpenRouterProvider:
    """Generate text with the OpenRouter Chat Completions API."""

    api_url = "https://openrouter.ai/api/v1/chat/completions"

    def __init__(
        self,
        api_key: str,
        model: str,
        timeout_seconds: float = 30.0,
    ) -> None:
        """Initialize the OpenRouter provider with API settings."""
        self.api_key = api_key.strip()
        self.model = model.strip()
        self.timeout_seconds = timeout_seconds

    def generate(self, prompt: str) -> str:
        """Generate text from a prompt using OpenRouter."""
        self._validate_settings()

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
        }

        try:
            with httpx.Client(timeout=self.timeout_seconds) as client:
                response = client.post(self.api_url, headers=headers, json=payload)
        except httpx.TimeoutException as exc:
            raise RuntimeError("OpenRouter request timed out. Please try again.") from exc
        except httpx.HTTPError as exc:
            raise RuntimeError(f"OpenRouter request failed: {exc}") from exc

        return self._parse_response(response)

    def _validate_settings(self) -> None:
        if not self.api_key:
            raise ValueError(
                "OpenRouter API key is missing. Set OPENROUTER_API_KEY in .env."
            )

        if not self.model:
            raise ValueError("OpenRouter model is missing. Set OPENROUTER_MODEL in .env.")

    def _parse_response(self, response: httpx.Response) -> str:
        try:
            data = response.json()
        except ValueError as exc:
            raise RuntimeError("OpenRouter returned an invalid JSON response.") from exc

        if not isinstance(data, dict):
            raise RuntimeError("OpenRouter returned an invalid JSON response.")

        error = data.get("error")
        if response.status_code >= 400:
            message = self._extract_error_message(error)
            raise RuntimeError(
                f"OpenRouter API request failed ({response.status_code}): {message}"
            )

        if error:
            message = self._extract_error_message(error)
            raise RuntimeError(f"OpenRouter API error: {message}")

        try:
            content = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError, TypeError) as exc:
            raise RuntimeError(
                "OpenRouter response did not include choices[0].message.content."
            ) from exc

        if not isinstance(content, str):
            raise RuntimeError(
                "OpenRouter response did not include choices[0].message.content."
            )

        return content

    def _extract_error_message(self, error: object) -> str:
        if isinstance(error, dict):
            message = error.get("message")
            if isinstance(message, str) and message:
                return message

        return "Unknown OpenRouter error."
