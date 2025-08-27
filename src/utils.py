from src.generators.testcases import generate_testcases


def load_requirements(path: str = "qa_requirements.txt") -> str:
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return "\n".join(line for line in content.splitlines() if line.strip())


def process_requirement(req_idx: int, requirement: str, test_scenario: str | None):
    """Generate and parse test cases for a requirement, printing header info."""
    print("=" * 60)
    print(f"Requirement {req_idx}: {requirement.strip()}")
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
    return [
        [c.strip() for c in line.strip("|").split("|")]
        for line in md_table.splitlines()
        if line.strip().startswith("|") and not line.strip().startswith("|---")
    ]