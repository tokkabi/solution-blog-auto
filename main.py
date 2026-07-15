from solution_blog_auto.workflows.blog import BlogWorkflow


def main() -> None:
    """Run the Solution Blog Auto MVP workflow."""
    workflow = BlogWorkflow()
    result = workflow.run("ETF란 무엇인가?")

    print("=== Solution Blog Auto ===")
    print(f"Topic : {result['topic']}")
    print()
    print("=== Contract ===")
    print(result["contract_name"])
    print()
    print("=== Research Result ===")
    print(result["research"])
    print()
    print("=== Markdown Article ===")
    print(result["article"])


if __name__ == "__main__":
    main()
