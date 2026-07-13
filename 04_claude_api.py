from anthropic import Anthropic

# 1. Initialize the client and pass the API key directly
client = Anthropic(
    api_key="",
    max_retries=2
)

try:
    # 2. Make your request using the messages.create endpoint
    message = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Explain quantum computing in one sentence."}
        ]
    )

    # 3. Extract the text from the response object
    print(message.content[0].text)

except Exception as e:
    print(f"\nAn error occurred: {e}")