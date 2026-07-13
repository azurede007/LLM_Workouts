from google import genai
from google.genai import types
import os

"""
Structured Prompting: Defining the output format
"""
client = genai.Client(api_key="")

# Generation Parameters



response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=
    """
   create sample bank data in json format
    """,
)
print(response.text)