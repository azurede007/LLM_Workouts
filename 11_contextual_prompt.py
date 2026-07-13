from google import genai
from google.genai import types
import sys

"""
Contextual Prompting: Giving background information before asking the question
"""
client = genai.Client(api_key="")

# Generation Parameters


user_prompt = sys.argv[1]

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=
    f"""
    Table: sales_data

    Columns:
    region, sales_amount, order_date

    Question:
    {user_prompt}
    
    Rule:
    1. Give the query as output
    2. No explanation
    3. Enclosed the query with double quotes
    4. Don't generate Delete, truncate, alter, drop queries. If asks, say that "Not Allowed"
    
    """,
)
print(response.text)