# ./mcp/server.py
from fastapi import FastAPI, Query
import psycopg2
import os

app = FastAPI()

# Read DB URL from environment
DB_URL = os.getenv("DB_URL", "postgresql://admin:admin@db:5432/moneytracker")

# Connect once (you can pool connections in production)
conn = psycopg2.connect(DB_URL)

@app.get("/mcp/query")
def run_query(sql: str = Query(..., description="SQL query to execute")):
    """
    MCP endpoint that executes SQL queries.
    """
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    return {"result": rows}

@app.get("/mcp/health")
def health_check():
    return {"status": "ok"}
