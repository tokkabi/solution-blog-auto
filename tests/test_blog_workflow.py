from solution_blog_auto.workflows.blog import BlogWorkflow
from solution_blog_auto.workflows.graph import create_blog_graph


def test_blog_graph_runs_all_nodes() -> None:
    """Blog graph should run research, writing, and publishing nodes."""
    graph = create_blog_graph()

    result = graph.invoke({"topic": "ETF란 무엇인가"})

    assert result == {
        "topic": "ETF란 무엇인가",
        "research": "[OpenAI] Dummy Response",
        "article": "[OpenAI] Dummy Response",
        "publish_result": "게시 완료",
    }


def test_blog_workflow_prints_progress(capsys) -> None:
    """Blog workflow should print the expected MVP progress messages."""
    workflow = BlogWorkflow()

    result = workflow.run("ETF란 무엇인가")

    assert result["publish_result"] == "게시 완료"
    assert capsys.readouterr().out.splitlines() == [
        "=== Solution Blog Auto ===",
        "Topic : ETF란 무엇인가",
        "Research Complete",
        "Writing Complete",
        "Publishing Complete",
        "Workflow Finished",
    ]
