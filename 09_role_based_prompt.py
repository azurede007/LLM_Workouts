from google import genai
from google.genai import types
import os

"""
role based Prompting: Telling the LLM who it should act as. assigning specific role or identity to the LLM before asking the question
"""
client = genai.Client(api_key="")

# Generation Parameters



response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=
    """
    Consider that you are a python expert.
   write the python code to read parameter value from command line and print it
    """,
)
print(response.text)