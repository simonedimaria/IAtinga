from fastapi import APIRouter, Request, File, UploadFile, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Dict
import subprocess
import os
from threading import Thread
from config import Config


TASKS: Dict[str, Dict] = {}

def only_admin(request: Request):
    authorization: str = request.headers.get('Authorization')
    if authorization is None or authorization != f"Bearer {Config.boccioni_token}":
        raise HTTPException(status_code=403, detail="Unauthorized")

def update_playbooks():
    playbook_files = os.listdir("playbooks")
    for playbook_file in playbook_files:
        if playbook_file not in TASKS:
            TASKS[playbook_file] = {
                'status': 'stopped',
                'playbook': playbook_file,
            }
    return True

router = APIRouter(
    tags=["admin"],
    dependencies=[Depends(only_admin)]
)

templates = Jinja2Templates(directory="templates")

@router.get("/dashboard")
async def admin_home(request: Request):
    update_playbooks()
    return templates.TemplateResponse(
            name="admin.html", context={"request": request, "tasks": TASKS}
        )

@router.get("/tasks")
async def get_tasks():
    update_playbooks()
    return JSONResponse(content=TASKS)

@router.post("/run/{task_name}")
async def run_playbook(task_name: str):
    update_playbooks()
    task_path = os.path.join("playbooks", task_name)
    TASKS[task_name]['status'] = 'running'
    try:
        result = subprocess.run(
            ['ansible-playbook', task_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )
        TASKS[task_name]['status'] = 'completed'
        TASKS[task_name]['output'] = result.stdout
    except Exception as e:
        TASKS[task_name]['status'] = 'failed'
        TASKS[task_name]['error'] = str(e)
    return JSONResponse(content={'message': f"{task_name} is now running"}, status_code=201)

@router.get("/tasks/{task_name}")
async def get_task_status(task_name: str):
    update_playbooks()
    if task_name in TASKS:
        return TASKS[task_name]
    else:
        raise HTTPException(status_code=404, detail="Task not found")



@router.post("/upload")
async def upload_playbook(playbook: UploadFile = File(...)):
    update_playbooks()
    file_location = os.path.join("playbooks", playbook.filename)
    directory = os.path.dirname(file_location)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_location, "wb") as file:
        file.write(playbook.file.read())
    
    if playbook.filename not in TASKS:
        TASKS[playbook.filename] = {
            'status': 'stopped',
            'playbook': playbook.filename,
    }
    
    return JSONResponse(content={'message': 'Playbook uploaded successfully'}, status_code=201)

