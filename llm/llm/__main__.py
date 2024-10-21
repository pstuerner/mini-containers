import os
from openai import OpenAI

if __name__ == "__main__":
    client = OpenAI(
        api_key=os.getenv("OPENAI_KEY")
    )

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Write a rap song about forgetting your cheese cake in the oven."}],
        model="gpt-4o-mini"
    )

    print(response.choices[0].message.content)