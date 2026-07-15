from solution_blog_auto.workflows.blog import BlogWorkflow
from solution_blog_auto.workflows.graph import create_blog_graph
from solution_blog_auto.workflows.nodes import WriterNode


class FakeContractSelector:
    """Always return a fixed contract name for deterministic tests."""

    def next_contract(self) -> str:
        """Return the fixed contract name."""
        return "01_story.md"


class FakeContractLoader:
    """Return fixed contract content for any requested name."""

    def load(self, name: str) -> str:
        """Return the fixed contract content."""
        return f"[Contract:{name}]"


def test_blog_graph_runs_all_nodes(monkeypatch) -> None:
    """Blog graph should run research, writing, and publishing nodes."""
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    writer_node = WriterNode(selector=FakeContractSelector(), loader=FakeContractLoader())
    graph = create_blog_graph(writer_node=writer_node)

    result = graph.invoke({"topic": "ETF"})

    assert result["topic"] == "ETF"
    assert result["research"] == "[OpenAI] Dummy Response"
    assert result["article"] == "[OpenAI] Dummy Response"
    assert result["contract_name"] == "01_story.md"
    assert result["publish_result"] == "게시 완료"


def test_blog_graph_records_contract_name(monkeypatch) -> None:
    """Writer node should record the selected contract name into state."""
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    writer_node = WriterNode(selector=FakeContractSelector(), loader=FakeContractLoader())
    graph = create_blog_graph(writer_node=writer_node)

    result = graph.invoke({"topic": "ETF"})

    assert result["contract_name"] == "01_story.md"


def test_blog_workflow_returns_result_without_printing(monkeypatch, capsys) -> None:
    """Blog workflow should return the result without printing progress."""
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    workflow = BlogWorkflow()

    result = workflow.run("ETF")

    assert result["publish_result"] == "게시 완료"
    assert "contract_name" in result
    assert capsys.readouterr().out == ""
