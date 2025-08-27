from src.utils import process_requirement


def display_requirement(requirement: str, test_scenario: str | None) -> None:
    """Print a requirement and its generated test cases as a Markdown table."""
    table_rows = process_requirement(1, requirement, test_scenario)
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