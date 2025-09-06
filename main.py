 # Import required packages
from fastapi import FastAPI
import psycopg2

app = FastAPI()

# Establish connection between backend and Postgres DB
def get_connection():
    return psycopg2.connect(
        dbname="fitness",
        user="postgres",
        password="secret",
        host= "localhost",
        port= "5432"
    )
@app.get("/avg-duration/{user_id}")
def avg_duration(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT AVG(duration) FROM workouts WHERE user_id = %s;", (user_id,))
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {"user_id": user_id, "avg_duration": result[0]}