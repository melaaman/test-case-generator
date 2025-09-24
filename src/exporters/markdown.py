from src.utils import process_requirement


def display_requirement(requirement: str, test_scenario: str | None) -> None:
    """Print a requirement and its generated test cases as a Markdown table."""
    table_rows = process_requirement(1, requirement, test_scenario)
    if table_rows:
        _print_markdown_table(table_rows)


def _print_markdown_table(rows: list[list[str]]) -> None:
    """Print rows as a Markdown table (flattened: one row per step).
    Title and preconditions are only shown once per test case.
    """
    if not rows:
        return

    header, *data_rows = rows

    # Print header
    print("| " + " | ".join(header) + " |")
    print("|" + "|".join(["---"] * len(header)) + "|")

    last_title = None
    last_preconditions = None

    for row in data_rows:
        title, preconditions, step, expected = row

        # Show title/preconditions only if they change
        show_title = title if title != last_title else ""
        show_pre = preconditions if preconditions != last_preconditions else ""

        print(f"| {show_title} | {show_pre} | {step} | {expected} |")

        last_title = title
        last_preconditions = preconditions