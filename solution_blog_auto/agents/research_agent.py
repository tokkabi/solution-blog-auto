from solution_blog_auto.core.prompt_loader import PromptLoader
from solution_blog_auto.services.llm_service import LLMService


class ResearchAgent:
    """Create research output for a blog topic."""

    def __init__(
        self,
        llm_service: LLMService | None = None,
        prompt_loader: PromptLoader | None = None,
    ) -> None:
        """Initialize the research agent."""
        self.llm_service = llm_service or LLMService()
        self.prompt_loader = prompt_loader or PromptLoader()

    def run(self, topic: str) -> str:
        """Run topic research through the LLM service."""
        prompt = self.prompt_loader.load("research.md", topic=topic)
        return self.llm_service.generate(prompt)
