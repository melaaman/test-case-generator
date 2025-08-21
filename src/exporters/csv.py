import csv
from src.utils import process_requirement


def export_to_csv(requirements, test_scenario, filename="output/testcases.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        for idx, req in enumerate(requirements, start=1):
            table_rows = process_requirement(idx, req, test_scenario)
            if not table_rows:
                continue

            writer.writerow(table_rows[0])  # Header
            writer.writerows(table_rows[1:])  # Remaining rows
