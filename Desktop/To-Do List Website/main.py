from fastapi import FastAPI
from fastapi import Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import date
import sqlite3




app = FastAPI()
templates = Jinja2Templates(directory="templates")
DB_NAME = "tasks.db"
app.mount("/static", StaticFiles(directory="static"), name="static")


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_description TEXT NOT NULL,
            task_priority TEXT,
            task_due_date TEXT,
            task_state BOOLEAN DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()
init_db()

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
async def read_root(request: Request):
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/create_task")
async def create_task_endpoint(request: Request, task_description: str = Form(...), task_priority: str = Form(...), task_due_date: date = Form(...)):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (task_description, task_priority, task_due_date, task_state) VALUES (?, ?, ?, ?)",
        (task_description, task_priority, task_due_date, False)
    )
    conn.commit()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})

@app.post("/update_task_status")
async def update_task_status_endpoint(request: Request, task_id: int = Form(...)):
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET task_state = ? WHERE task_id = ?", (True, task_id ))
    conn.commit()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})

@app.post("/update_task_priority")
async def update_task_priority_endpoint(request: Request, task_id: int = Form(...), task_priority: int = Form(...)):
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET task_priority = ? WHERE task_id = ?", (task_priority, task_id))
    conn.commit()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})
    
@app.post("/update_task_due_date")
async def update_task_due_date_endpoint(request: Request, task_id: int = Form(...), task_due_date: date = Form(...)):
    conn = get_db_connection()
    conn.execute("UPDATE tasks SET task_due_date  = ? WHERE task_id = ?", (task_due_date, task_id))
    conn.commit()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})
    
@app.post("/delete_task")
async def delete_task_endpoint(request: Request):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE task_state = 1")
    conn.commit()
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})
