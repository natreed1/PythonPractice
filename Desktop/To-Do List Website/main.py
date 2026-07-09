from fastapi import FastAPI
from fastapi import Form
from fastapi import Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Task():
    id = int
    task_priority: str
    task_description: str
    task_state: bool = False

tasks = []


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/create_task")
async def create_task_endpoint(request: Request, task_description: str = Form(...), task_priority: str = Form(...)):
    task = Task()
    task.id = len(tasks)
    task.task_description = task_description
    task.task_priority = task_priority
    tasks.append(task)
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})

@app.post("/update_task")
async def update_task_endpoint(request: Request, task_id: int = Form(...)):
    for task in tasks:
        if task.id == task_id:
            task.task_state = True
            break
    return templates.TemplateResponse("todo_list.html", {"request": request, "tasks": tasks})
