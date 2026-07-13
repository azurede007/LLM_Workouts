from openai import OpenAI

# Explicitly pass the API key as a parameter
client = OpenAI(
    api_key="",
    max_retries=2
)

try:
    response = client.chat.completions.create(
        model="gpt-3o-mini",
        messages=[
            {"role": "user", "content": "Explain quantum computing in one sentence.", "role": "system", "content": "Role: Act as a data architect. Rules: Generate max of 100 keywords"
             }
            ],
        temperature=0.4,
        top_p=0.9,
        presence_penalty=0.0,
        frequency_penalty=0.0,
        stop=[";"],
        seed=1234

    )
    print(response.choices[0].message.content)

except Exception as e:
    print(f"\nAn error occurred: {e}")