from solution_blog_auto.workflows.graph import create_blog_graph
from solution_blog_auto.workflows.state import BlogState


class BlogWorkflow:
    """Run the blog automation workflow."""

    def run(self, topic: str) -> BlogState:
        """Execute the blog workflow and print the MVP progress result."""
        graph = create_blog_graph()
        result = graph.invoke({"topic": topic})

        print("=== Solution Blog Auto ===")
        print(f"Topic : {result['topic']}")
        print("Research Complete")
        print("Writing Complete")
        print("Publishing Complete")
        print("Workflow Finished")

        return result
