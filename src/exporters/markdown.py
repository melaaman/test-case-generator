from src.utils import process_requirement


def display_requirement(requirements: list[str], test_scenario: str | None) -> None:
    """Print a requirement and its generated test cases as a Markdown table."""
    for idx, req in enumerate(requirements, start=1):
        table_rows = process_requirement(idx, req, test_scenario)
        if table_rows:
            _print_markdown_table(table_rows)


def _print_markdown_table(rows: list[list[str]]) -> None:
    """Print rows as a Markdown table."""
    if not rows:
        return
    header, *data_rows = rows
    print("| " + " | ".join(header) + " |")
    print("|" + "|".join(["---"] * len(header)) + "|")
    for row in data_rows:
        print("| " + " | ".join(row) + " |")