from google import genai
from google.genai import types
import os

"""
Instruction Prompting: Giving clear instruction about what to do, how to respond, rules to follow
"""
client = genai.Client(api_key="")

# Generation Parameters



response = client.models.generate_content(
    model='gemini-2.5-flash-lite',
    contents=
    """
   You are a Senior Data Engineer.
   Explain Apache Kafka for beginners.
   Summarize and give the output only in 5 bullet points.
   No additional content.
    """,
)
print(response.text)