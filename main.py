 # Import required packages
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import psycopg2
import os
from dotenv import load_dotenv
from openai import OpenAI


# load environment variables
load_dotenv()

# Launch the FastAPI
app = FastAPI()

# Import CORS (Cross origin resource sharing)
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:3000"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

# Invoke OPENAI API key through DotENV
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Establish connection between backend and Postgres DB
def get_connection():
    return psycopg2.connect(
        dbname="fitness",
        user="postgres",
        password="secret",
        host= "localhost",
        port= "5432"
    )

"""
Convert a natural language query into a SQL query using an @ask endpoint
"""
@app.get("/ask")
def ask(question: str):
    schema= """
    Table: workouts
    Columns: id(serial), user_id= (int), duration = (int), date = (date)
    """

    prompt = f"""
    You are a SQL assistant. Given the schema and the user's natural language question, do the following:
    1. Write ONLY the SQL query to answer it. 
    2. Write the unit/type of the answer. (Ex: "minutes", "count of rows", "percentage")
    Schema: {schema}
    Question: {question}
    
    Always format your answer like this:
    SQL: <the SQL query>
    Unit: <the unit>

    Schema:
    {schema}

    Question: {question}
    """

    response= client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{'role': 'user', 'content': prompt}]
    )
    text = response.choices[0].message.content.strip()

    sql_query, unit = None, None
    if "SQL:" in text and "Unit:" in text:
        sql_query = text.split("SQL:")[1].split("Unit:")[0].strip()
        unit = text.split("Unit:")[1].strip()
    else:
        sql_query = text
        unit = "unknown"

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql_query)
    result = cur.fetchall()
    cur.close()
    conn.close()

    answer = result[0][0] if result else None

    return {
        "sql_query": sql_query,
        "answer": f"{answer} {unit}" if unit != "unknown" else str(answer),
        "unit": unit
    }