from solution_blog_auto.agents.research_agent import ResearchAgent
from solution_blog_auto.agents.writer_agent import WriterAgent
from solution_blog_auto.core.contract_loader import ContractLoader
from solution_blog_auto.research.input import ResearchInput
from solution_blog_auto.services.contract_selector import ContractSelector
from solution_blog_auto.workflows.state import BlogState


class ResearchNode:
    """Create research content for the blog topic."""

    def __call__(self, state: BlogState) -> BlogState:
        """Build ResearchInput from state and run research."""
        research_input = ResearchInput(
            topic=state["topic"],
            purpose="블로그 글 작성을 위한 핵심 정보 조사",
            audience="일반 독자",
            content_direction="정확하고 이해하기 쉬운 정보 중심",
            must_include=[],
            avoid=[],
        )
        state["research"] = ResearchAgent().run(research_input)
        return state


class WriterNode:
    """Create article content from the research result and output contract."""

    def __init__(
        self,
        selector: ContractSelector | None = None,
        loader: ContractLoader | None = None,
    ) -> None:
        """Initialize the writer node with its contract dependencies.

        Args:
            selector: Round-robin contract selector. Defaults to a
                :class:`ContractSelector` backed by the runtime state file.
            loader: Contract template loader. Defaults to a
                :class:`ContractLoader` reading from the project contracts dir.
        """
        self.selector = selector or ContractSelector()
        self.loader = loader or ContractLoader()

    def __call__(self, state: BlogState) -> BlogState:
        """Select a contract, write the article, and record the contract name."""
        contract_name = self.selector.next_contract()
        contract = self.loader.load(contract_name)
        state["contract_name"] = contract_name
        state["article"] = WriterAgent().run(
            state["topic"], state["research"], contract
        )
        return state


class PublisherNode:
    """Publish the completed article."""

    def __call__(self, state: BlogState) -> BlogState:
        """Mark the publishing step as complete."""
        state["publish_result"] = "게시 완료"
        return state
