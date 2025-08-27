import argparse
from src.exporters.csv import export_to_csv
from src.exporters.markdown import display_requirement
from src.utils import load_requirements


def main() -> None:
    parser = argparse.ArgumentParser(description="Parser for test case generator.")
    parser.add_argument(
        "--csv",
        action="store_true",
        help="Save results to CSV instead of printing Markdown."
    )
    parser.add_argument(
        "--test-scenario",
        type=str,
        help="Pass test scenario to the test case generator."
    )

    args = parser.parse_args()

    requirement = load_requirements()

    if args.csv:
        export_to_csv(requirement, args.test_scenario)
    else:
        display_requirement(requirement, args.test_scenario)


if __name__ == "__main__":
    main()
