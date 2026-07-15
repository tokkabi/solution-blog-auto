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

    def run(self, topic: str, research: str, contract: str) -> str:
        """Run article writing through the LLM service.

        Args:
            topic: Blog topic to write about.
            research: Research content produced by the research agent.
            contract: Output contract describing the article structure.

        Returns:
            Generated article text.

        Note:
            향후 WriterRequest 객체로 통합 예정 (MVP 이후 리팩토링).
        """
        prompt = self.prompt_loader.load(
            "writer.md", topic=topic, research=research, contract=contract
        )
        return self.llm_service.generate(prompt)
