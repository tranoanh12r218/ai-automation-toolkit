from ai_automation.text import clean_text, truncate_text


def test_clean_text():
    text = "  Hello    AI   Automation  "
    assert clean_text(text) == "Hello AI Automation"


def test_truncate_text():
    text = "This is a long text for testing"
    result = truncate_text(text, 15)

    assert len(result) <= 15
    assert result.endswith("...")


def test_short_text_is_unchanged():
    text = "Hello AI"
    assert truncate_text(text, 20) == text
