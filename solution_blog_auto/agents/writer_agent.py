from pathlib import Path

from solution_blog_auto.services.llm_service import LLMService


class WriterAgent:
    """Create article output from research content."""

    def __init__(self, llm_service: LLMService | None = None) -> None:
        """Initialize the writer agent."""
        self.llm_service = llm_service or LLMService()

    def run(self, topic: str, research: str) -> str:
        """Run article writing through the LLM service."""
        template = Path("prompts/writer.md").read_text(encoding="utf-8")
        prompt = template.format(topic=topic, research=research)
        return self.llm_service.generate(prompt)
