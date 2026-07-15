from solution_blog_auto.agents.research_agent import ResearchAgent
from solution_blog_auto.research.input import ResearchInput


class FakeLLMService:
    """Return a fixed response and record the last prompt for assertions."""

    last_prompt: str | None = None

    def generate(self, prompt: str) -> str:
        """Return the canned research output."""
        self.__class__.last_prompt = prompt
        return "fake research result"


def test_research_agent_passes_all_fields_to_prompt() -> None:
    """ResearchAgent should forward all ResearchInput fields into the prompt."""
    research_input = ResearchInput(
        topic="ETF",
        purpose="블로그 글 작성을 위한 핵심 정보 조사",
        audience="일반 독자",
        content_direction="정확하고 이해하기 쉬운 정보 중심",
        must_include=["정의"],
        avoid=["광고성 표현"],
    )
    agent = ResearchAgent(llm_service=FakeLLMService())

    result = agent.run(research_input)

    assert result == "fake research result"
    assert "ETF" in FakeLLMService.last_prompt
    assert "블로그 글 작성을 위한 핵심 정보 조사" in FakeLLMService.last_prompt
    assert "일반 독자" in FakeLLMService.last_prompt
    assert "정확하고 이해하기 쉬운 정보 중심" in FakeLLMService.last_prompt
    assert "정의" in FakeLLMService.last_prompt
    assert "광고성 표현" in FakeLLMService.last_prompt
