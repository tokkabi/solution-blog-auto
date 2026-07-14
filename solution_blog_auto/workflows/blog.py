from solution_blog_auto.workflows.graph import create_blog_graph
from solution_blog_auto.workflows.state import BlogState


class BlogWorkflow:
    """Run the blog automation workflow."""

    def run(self, topic: str) -> BlogState:
        """Execute the blog workflow and return the result."""
        graph = create_blog_graph()
        return graph.invoke({"topic": topic})
