import os
from openai import OpenAI
import dotenv
from src.prompts import generate_testcases_prompt

dotenv.load_dotenv()

client = OpenAI(api_key=os.environ.get("OPEN_API_KEY"))


def generate_testcases(test_scenario: str | None, requirement: str) -> str:
    prompt = generate_testcases_prompt.format(test_scenario=test_scenario, requirement=requirement)
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "You are a helpful QA assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    content = response.choices[0].message.content
    if content is None or not content.strip():
        raise ValueError("OpenAI API returned empty response")
    return content
