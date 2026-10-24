from backend.main import build_prompt


def test_build_prompt_mentions_fastone_and_sachin():
    prompt = build_prompt("Hello there")
    assert "FastOne" in prompt
    assert "Sachin" in prompt
    assert "first person" in prompt.lower()
