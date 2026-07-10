from solution_blog_auto.agents.research_agent import ResearchAgent
from solution_blog_auto.agents.writer_agent import WriterAgent
from solution_blog_auto.workflows.state import BlogState


class ResearchNode:
    """Create research content for the blog topic."""

    def __call__(self, state: BlogState) -> BlogState:
        """Mark the research step as complete."""
        state["research"] = ResearchAgent().run(state["topic"])
        return state


class WriterNode:
    """Create article content from the research result."""

    def __call__(self, state: BlogState) -> BlogState:
        """Mark the writing step as complete."""
        state["article"] = WriterAgent().run(state["topic"], state["research"])
        return state


class PublisherNode:
    """Publish the completed article."""

    def __call__(self, state: BlogState) -> BlogState:
        """Mark the publishing step as complete."""
        state["publish_result"] = "게시 완료"
        return state
