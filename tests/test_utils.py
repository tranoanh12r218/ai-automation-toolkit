from ai_automation.utils import chunk_text, ensure_string, utc_timestamp


def test_utc_timestamp():
    timestamp = utc_timestamp()

    assert timestamp.endswith("+00:00")


def test_ensure_string():
    assert ensure_string("  Hello  ") == "Hello"
    assert ensure_string(None) == ""
    assert ensure_string(None, "default") == "default"


def test_chunk_text():
    text = "abcdefghij"

    chunks = chunk_text(text, chunk_size=4)

    assert chunks == ["abcd", "efgh", "ij"]


def test_empty_text_returns_empty_list():
    assert chunk_text("   ", chunk_size=10) == []
