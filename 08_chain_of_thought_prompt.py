from google import genai
from google.genai import types
import os

"""
few-shot Prompting:Learning from few example before answering
"""
client = genai.Client(api_key="")

# Generation Parameters



response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=
    """
    A shop has 10 apples.
    It sells 3 apples.
    Then buys 5 apples.
    How many apples now?
    Think step by step.
    """,
)

response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=
    """
    Write a program to calculate the factorial of a given number in python code.
    Give step by step info
    """)
print(response.text)