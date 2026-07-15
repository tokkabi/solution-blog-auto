from typing import Any

from langgraph.graph import END, START, StateGraph

from solution_blog_auto.workflows.nodes import PublisherNode, ResearchNode, WriterNode
from solution_blog_auto.workflows.state import BlogState


def create_blog_graph(writer_node: WriterNode | None = None) -> Any:
    """Create the MVP blog workflow graph.

    Args:
        writer_node: Optional pre-built writer node, useful for injecting fakes
            in tests. When omitted, a default :class:`WriterNode` is used.
    """
    graph = StateGraph(BlogState)

    graph.add_node("research", ResearchNode())
    graph.add_node("writer", writer_node or WriterNode())
    graph.add_node("publisher", PublisherNode())

    graph.add_edge(START, "research")
    graph.add_edge("research", "writer")
    graph.add_edge("writer", "publisher")
    graph.add_edge("publisher", END)

    return graph.compile()
