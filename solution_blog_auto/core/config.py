from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    llm_provider: str = "openai"

    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    openrouter_api_key: str = ""
    openrouter_model: str = "deepseek/deepseek-chat-v3-0324:free"

    glm_api_key: str = ""
    glm_model: str = "glm-4-flash"

    gemini_api_key: str = ""
    gemini_model: str = "gemini-2.0-flash"

    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.2"
