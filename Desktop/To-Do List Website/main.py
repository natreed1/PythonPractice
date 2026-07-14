from fastapi import FastAPI
from fastapi import Form
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import date


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


class Task():
    id = int
    task_priority: int
    task_description: str
    task_state: bool = False

tasks = []


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/create_task")
async def create_task_endpoint(request: Request, task_description: str = Form(...), task_priority: str = Form(...), task_due_date: date = Form(...)):
    task = Task()
    task.id = len(tasks)
    task.task_description = task_description
    task.task_priority = task_priority
    task.task_due_date = task_due_date
    tasks.append(task)
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})

@app.post("/update_task_status")
async def update_task_status_endpoint(request: Request, task_id: int = Form(...)):
    for task in tasks:
        if task.id == task_id:
            task.task_state = True
            break
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})

@app.post("/update_task_priority")
async def update_task_priority_endpoint(request: Request, task_id: int = Form(...), task_priority: int = Form(...)):
    for task in tasks:
        if task.id == task_id:
            task.task_priority = task_priority
            break
        return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})
    
@app.post("/update_task_due_date")
async def update_task_due_date_endpoint(request: Request, task_id: int = Form(...), task_due_date: date = Form(...)):
    for task in tasks:
        if task.id == task_id:
            task.task_due_date = task_due_date
            break
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})
    
@app.post("/delete_task")
async def delete_task_endpoint(request: Request):
    global tasks
    tasks = [task for task in tasks if not task.task_state]
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})
