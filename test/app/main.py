from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import app.task_manager as task_manager

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    tasks = task_manager.get_tasks()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.post("/add_task", response_class=HTMLResponse)
async def add_task(request: Request, task_name: str = Form(...)):
    task_manager.add_task(task_name)
    tasks = task_manager.get_tasks()
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks})

@app.get("/task_output/{task_id}", response_class=HTMLResponse)
async def task_output(request: Request, task_id: int):
    output = task_manager.get_task_output(task_id)
    return templates.TemplateResponse("index.html", {"request": request, "output": output})
