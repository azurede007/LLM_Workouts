import os
from openai import OpenAI

# Initialize the OpenAI client, but point it to Groq's servers
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key="your-groq-api-key-here",  # Or use os.environ.get("GROQ_API_KEY")
    max_retries=5
)

try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # Specify the Llama model
        messages=[
            {"role": "user", "content": "Explain quantum computing in one sentence.", "role": "system", "content": "Role: Act as a data architect. Rules: Generate max of 100 keywords"
            }
        ]
    )

    print(response.choices[0].message.content)

except Exception as e:
    print(f"\nAn error occurred: {e}")