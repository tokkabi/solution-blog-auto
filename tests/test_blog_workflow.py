from solution_blog_auto.workflows.blog import BlogWorkflow
from solution_blog_auto.workflows.graph import create_blog_graph


def test_blog_graph_runs_all_nodes(monkeypatch) -> None:
    """Blog graph should run research, writing, and publishing nodes."""
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    graph = create_blog_graph()

    result = graph.invoke({"topic": "ETF"})

    assert result == {
        "topic": "ETF",
        "research": "[OpenAI] Dummy Response",
        "article": "[OpenAI] Dummy Response",
        "publish_result": "게시 완료",
    }


def test_blog_workflow_returns_result_without_printing(monkeypatch, capsys) -> None:
    """Blog workflow should return the result without printing progress."""
    monkeypatch.setenv("LLM_PROVIDER", "openai")
    workflow = BlogWorkflow()

    result = workflow.run("ETF")

    assert result["publish_result"] == "게시 완료"
    assert capsys.readouterr().out == ""
