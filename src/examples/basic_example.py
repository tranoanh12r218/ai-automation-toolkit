"""Basic example for AI Automation Toolkit."""

from ai_automation.text import clean_text, truncate_text
from ai_automation.utils import chunk_text, utc_timestamp


def main() -> None:
    text = """
    AI automation helps developers build faster workflows
    and reduce repetitive tasks.
    """

    cleaned = clean_text(text)

    print("AI Automation Toolkit")
    print("-" * 30)
    print(f"UTC time: {utc_timestamp()}")
    print(f"Cleaned text: {cleaned}")
    print(f"Short version: {truncate_text(cleaned, 50)}")

    chunks = chunk_text(cleaned, chunk_size=40)

    print("\nText chunks:")
    for index, chunk in enumerate(chunks, start=1):
        print(f"{index}. {chunk}")


if __name__ == "__main__":
    main()
