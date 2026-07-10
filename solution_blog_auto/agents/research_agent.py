from pathlib import Path

from solution_blog_auto.services.llm_service import LLMService


class ResearchAgent:
    """Create research output for a blog topic."""

    def __init__(self, llm_service: LLMService | None = None) -> None:
        """Initialize the research agent."""
        self.llm_service = llm_service or LLMService()

    def run(self, topic: str) -> str:
        """Run topic research through the LLM service."""
        template = Path("prompts/research.md").read_text(encoding="utf-8")
        prompt = template.format(topic=topic)
        return self.llm_service.generate(prompt)
