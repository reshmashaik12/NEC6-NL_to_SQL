from groq import Groq
from config import GROQ_API_KEY

# CREATE CLIENT
client = Groq(
    api_key=GROQ_API_KEY
)

def generate_sql(user_query):

    prompt = f"""
    Convert the following English question into SQL query.

    Database Table:
    employees(id, name, department, salary)

    Rules:
    - Only return SQL query
    - No explanation
    - No markdown
    - Return valid SQLite query

    Question:
    {user_query}
    """

    response = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0
    )

    sql_query = response.choices[0].message.content

    return sql_query.strip()