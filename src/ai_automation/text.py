"""Text utilities for automation workflows."""


def clean_text(text: str) -> str:
    """Normalize whitespace in a text string."""
    return " ".join(text.split())


def truncate_text(text: str, max_length: int = 200) -> str:
    """Truncate text to a maximum length."""
    if max_length < 1:
        raise ValueError("max_length must be greater than 0")

    text = clean_text(text)

    if len(text) <= max_length:
        return text

    return text[: max_length - 3].rstrip() + "..."
