from pathlib import Path

from ai_automation.files import list_files, read_text, write_text


def test_write_and_read_text(tmp_path: Path):
    file_path = tmp_path / "hello.txt"

    write_text(file_path, "Hello AI Automation")

    assert read_text(file_path) == "Hello AI Automation"


def test_write_text_creates_parent_directory(tmp_path: Path):
    file_path = tmp_path / "data" / "output.txt"

    write_text(file_path, "Automation works")

    assert file_path.exists()
    assert read_text(file_path) == "Automation works"


def test_list_files(tmp_path: Path):
    write_text(tmp_path / "one.txt", "1")
    write_text(tmp_path / "two.txt", "2")
    write_text(tmp_path / "notes.md", "3")

    files = list_files(tmp_path, "*.txt")

    assert len(files) == 2
    assert all(file.suffix == ".txt" for file in files)
