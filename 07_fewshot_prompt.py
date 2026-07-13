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
    Text: "I love this phone."
    Sentiment: Positive

    Text: "This movie is terrible."
    Sentiment: Negative
    
    Text: "The service was excellent."
    Sentiment: Positive

    Text: "The food was neither good nor bad."
    Sentiment:

    """,
)

print(response.text)