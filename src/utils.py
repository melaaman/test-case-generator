from src.generators.testcases import generate_testcases


def load_requirements(path: str = "qa_requirements.txt") -> list[str]:
    """Load requirements from a text file, separated by double newlines."""
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return [req.strip() for req in content.split("\n\n") if req.strip()]


def process_requirement(req_idx: int, requirement: str, test_scenario: str | None):
    """Generate and parse test cases for a requirement, printing header info."""
    print("=" * 60)
    print(f"Requirement {req_idx}: {requirement}")
    print("-" * 60)
    print("Generating...")

    md_table = generate_testcases(test_scenario, requirement)
    table_rows = _parse_markdown_table(md_table)

    if not table_rows:
        print("No test cases generated for this requirement.")
        return None
    print("Done")
    return table_rows

def _parse_markdown_table(md_table: str):
    """Parse a Markdown table and return a list of rows (lists of columns)."""
    rows = []
    for line in md_table.splitlines():
        line = line.strip()
        if line.startswith("|") and not line.startswith("|---"):
            cols = [c.strip() for c in line.strip("|").split("|")]
            rows.append(cols)
    return rows