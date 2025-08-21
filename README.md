# Test Case Generator

A tool to automatically generate structured test cases from requirements.

## Setup

1. Clone the repository
2. Copy `.env_example` to `.env`
3. Add your OpenAI API key to `.env`
4. Create a file named qa_requirements.txt to the root of the project
5. Install dependencies (Python 3.7+ required)

## Usage
1. Add your requirements to `qa_requirements.txt`. Each requirement should be written in free text format.

2. Run the application:
   ```bash
   # Generate test cases and print to console
   python -m src.main

   # Generate test cases and save to CSV file
   python -m src.main --csv

   # Generate test cases with a test scenario name
   python -m src.main --test-scenario "My test scenario"

   # Generate test cases with scenario and save to CSV
   python -m src.main --test-scenario "My test scenario" --csv
   ```

The generated test cases will include:
- Unique ID (TC001, TC002, etc.)
- Test case title
- Preconditions
- Test steps
- Expected results

