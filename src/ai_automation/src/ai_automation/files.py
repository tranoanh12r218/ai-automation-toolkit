"""File utilities for automation workflows."""

from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Read a UTF-8 text file and return its contents."""
    return Path(path).read_text(encoding=encoding)


def write_text(
    path: str | Path,
    content: str,
    encoding: str = "utf-8",
) -> None:
    """Write text content to a file."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(content, encoding=encoding)


def list_files(
    directory: str | Path,
    pattern: str = "*",
) -> list[Path]:
    """Return files matching a pattern in a directory."""
    directory_path = Path(directory)

    if not directory_path.exists():
        raise FileNotFoundError(f"Directory not found: {directory}")

    return sorted(
        path for path in directory_path.glob(pattern)
        if path.is_file()
    )
