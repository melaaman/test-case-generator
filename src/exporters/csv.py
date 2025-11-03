import csv
from src.utils import process_requirement


def export_to_csv(requirement, test_scenario, filename="output/testcases.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        table_rows = process_requirement(1, requirement, test_scenario)
        if not table_rows:
            return

        writer.writerow(["Test name", "Test step", "Test data", "Expected result", "Component", "Version"]) # Header
        writer.writerows(table_rows[1:])  # Remaining rows
