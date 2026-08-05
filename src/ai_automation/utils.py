"""General utility functions for AI automation workflows."""

from datetime import datetime, timezone
from typing import Any


def utc_timestamp() -> str:
    """Return the current UTC time in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def ensure_string(value: Any, default: str = "") -> str:
    """Convert a value to a clean string."""
    if value is None:
        return default

    return str(value).strip()


def chunk_text(
    text: str,
    chunk_size: int = 1000,
) -> list[str]:
    """Split text into chunks of approximately equal size."""
    if chunk_size < 1:
        raise ValueError("chunk_size must be greater than 0")

    text = text.strip()

    if not text:
        return []

    return [
        text[index:index + chunk_size]
        for index in range(0, len(text), chunk_size)
    ]
