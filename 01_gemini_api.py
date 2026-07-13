from google import genai
from google.genai import types
import os

# Initialize a client (it automatically looks for the GEMINI_API_KEY environment variable)
#client = genai.Client()

# Or, if you need to pass the key directly:
client = genai.Client(api_key="")

# Generation Parameters



response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents='Explain spark and its components',
    config= types.GenerateContentConfig(
        temperature=0.7,
        top_p=0.9,
        top_k=40,
        max_output_tokens=10
    )
)

print(response.text)