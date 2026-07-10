from solution_blog_auto.workflows.blog import BlogWorkflow


def main() -> None:
    """Run the Solution Blog Auto MVP workflow."""
    workflow = BlogWorkflow()
    workflow.run("ETF란 무엇인가")


if __name__ == "__main__":
    main()
