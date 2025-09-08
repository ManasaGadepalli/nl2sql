# 🧠 NL → SQL Query Assistant (NL2SQL)

A simple full-stack project that converts **natural language questions** into **SQL queries** and executes them on a PostgreSQL database.  
Built with **FastAPI**, **React**, **Dockerized Postgres**, and **OpenAI**.

---

## 🚀 Features
- **Ask in plain English** (e.g., “What’s the average workout duration for user 1?”).
- Backend uses **OpenAI** to generate a SQL query for a defined schema.
- Executes SQL safely on a **Postgres** database running in Docker.
- Returns both the **SQL query** and the **answer with units**.
- Frontend built with **React** provides a textbox + results view.
- **CORS enabled** to allow React → FastAPI communication.

---

## 🏗️ Tech Stack
- **Backend:** FastAPI, psycopg2, SQLAlchemy (optional), python-dotenv  
- **Database:** PostgreSQL (running in Docker)  
- **Frontend:** React (Create React App)  
- **AI:** OpenAI API (`gpt-4o-mini`)  
- **Infra:** Docker Desktop for containerized Postgres  

---
