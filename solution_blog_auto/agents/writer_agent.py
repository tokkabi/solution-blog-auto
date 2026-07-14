from solution_blog_auto.core.prompt_loader import PromptLoader
from solution_blog_auto.services.llm_service import LLMService


class WriterAgent:
    """Create article output from research content."""

    def __init__(
        self,
        llm_service: LLMService | None = None,
        prompt_loader: PromptLoader | None = None,
    ) -> None:
        """Initialize the writer agent."""
        self.llm_service = llm_service or LLMService()
        self.prompt_loader = prompt_loader or PromptLoader()

    def run(self, topic: str, research: str) -> str:
        """Run article writing through the LLM service."""
        prompt = self.prompt_loader.load("writer.md", topic=topic, research=research)
        return self.llm_service.generate(prompt)
