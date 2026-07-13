from google import genai
from google.genai import types
import os

"""
One-shot Prompting: Teach the LLM using one example before asking to perform the task
"""
client = genai.Client(api_key="")

# Generation Parameters



response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=
    """
    Translate English to French:
    Example:
    English: Good Morning
    French: Bonjour
    English: Good Evening
    French:
    """,
)

print(response.text)