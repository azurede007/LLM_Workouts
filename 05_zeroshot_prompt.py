from google import genai
from google.genai import types
import os

"""
Zero-shot Prompting: No examples provided. Direct instruction and get the output from the trained data
"""
client = genai.Client(api_key="")

# Generation Parameters



response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents='Translate English to French: Good Morning',
)

print(response.text)