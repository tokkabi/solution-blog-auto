from solution_blog_auto.core.prompt_loader import PromptLoader
from solution_blog_auto.research.input import ResearchInput
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

    def run(self, research_input: ResearchInput) -> str:
        """Run research through the LLM service using structured input."""
        prompt = self.prompt_loader.load(
            "research.md",
            topic=research_input.topic,
            purpose=research_input.purpose,
            audience=research_input.audience,
            content_direction=research_input.content_direction,
            must_include=research_input.must_include,
            avoid=research_input.avoid,
        )
        return self.llm_service.generate(prompt)
