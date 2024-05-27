from fastapi import APIRouter, Request, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Dict
import subprocess
import os
from threading import Thread
import config
from functools import wraps

router = APIRouter()

router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Store tasks in memory (for simplicity; consider using a real database)
tasks: Dict[str, Dict] = {}

def only_admin(func):
    @wraps(func)
    async def wrapper(request: Request, *args, **kwargs):
        # check if authorization header corresponds to admin token
        if request.headers['Authorization'] != config.ADMIN_TOKEN:
            raise HTTPException(status_code=403, detail="Unauthorized")
        return await func(*args, **kwargs)
    return wrapper


@router.get("/tasks")
@only_admin
async def get_tasks():
    return templates.TemplateResponse(
            name="tasks.html", context={"tasks": tasks}
        )

@router.post("/tasks")
@only_admin
async def create_task(playbook: str):
    task_id = str(len(tasks) + 1)
    tasks[task_id] = {
        'status': 'pending',
        'playbook': playbook
    }

    def run_playbook(task_id):
        tasks[task_id]['status'] = 'running'
        try:
            result = subprocess.run(['ansible-playbook', playbook], capture_output=True, text=True)
            tasks[task_id]['status'] = 'completed'
            tasks[task_id]['output'] = result.stdout
        except Exception as e:
            tasks[task_id]['status'] = 'failed'
            tasks[task_id]['error'] = str(e)

    Thread(target=run_playbook, args=(task_id,)).start()

    return JSONResponse(content={'task_id': task_id}, status_code=201)

@router.get("/tasks/{task_id}")
@only_admin
async def get_task_status(task_id: str):
    if task_id in tasks:
        return tasks[task_id]
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@router.post("/upload")
@only_admin
async def upload_playbook(playbook: UploadFile = File(...)):
    file_location = os.path.join("playbooks", playbook.filename)
    with open(file_location, "wb") as file:
        file.write(playbook.file.read())
    return JSONResponse(content={'message': 'Playbook uploaded successfully'}, status_code=201)

