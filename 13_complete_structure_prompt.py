from google import genai
from google.genai import types
import sys

"""
Structured Prompting: Defining the output format
"""
client = genai.Client(api_key="")

# Generation Parameters


user_prompt = sys.argv[1]
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=
    f"""
    Role:
     You are a MySQL SQL Generator.
    
    Context:
        Table: sales_data
        Columns:
        region, sales_amount, order_date
    
    Task:
        {user_prompt}
    
    Constraints:
        - Use only SELECT query
        - Use LIMIT 5
    
    Output Format:
        SQL only
    """,
)
print(response.text)