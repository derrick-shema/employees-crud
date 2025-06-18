from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os 
import sqlite3

DB_PATH = 'employees.db'

@asynccontextmanager
async def lifespan(app: FastAPI):
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT NOT NULL,
                  last_name TEXT NOT NULL,
                  title TEXT NOT NULL
            )
        """)

        conn.commit()
        conn.close()
    
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

# get all employees
@app.get('/api/employees')
def employees():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    query = 'SELECT first_name, last_name, title FROM employees'
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    employees = [{"first_name": row[0], "last_name": row[1], "title": row[2]} for row in rows]
    return employees