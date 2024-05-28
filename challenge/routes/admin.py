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
    #authorization: str = request.headers.get('Authorization')
    #if authorization is None or authorization != f"Bearer {Config.boccioni_token}":
    #    raise HTTPException(status_code=403, detail="Unauthorized")
    pass

router = APIRouter(
    tags=["admin"],
    dependencies=[Depends(only_admin)]
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def admin_home(request: Request):
    return templates.TemplateResponse(
            name="admin.html", context={"request": request, "tasks": TASKS}
        )

@router.get("/tasks")
async def get_tasks():
    return JSONResponse(content=TASKS)

@router.post("/tasks")
async def create_task(request: Request, playbook: str):
    task_id = str(len(TASKS) + 1)
    TASKS[task_id] = {
        'status': 'pending',
        'playbook': playbook
    }

    def run_playbook(task_id):
        TASKS[task_id]['status'] = 'running'
        try:
            result = subprocess.run(['ansible-playbook', playbook], capture_output=True, text=True)
            TASKS[task_id]['status'] = 'completed'
            TASKS[task_id]['output'] = result.stdout
        except Exception as e:
            TASKS[task_id]['status'] = 'failed'
            TASKS[task_id]['error'] = str(e)

    Thread(target=run_playbook, args=(task_id,)).start()

    return JSONResponse(content={"request": request, 'task_id': task_id}, status_code=201)

@router.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    if task_id in TASKS:
        return TASKS[task_id]
    else:
        raise HTTPException(status_code=404, detail="Task not found")



@router.post("/upload")
async def upload_playbook(playbook: UploadFile = File(...)):
    file_location = os.path.join("playbooks", playbook.filename)
    directory = os.path.dirname(file_location)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(file_location, "wb") as file:
        file.write(playbook.file.read())
        
    TASKS[playbook.filename] = {
        'status': 'stopped',
        'playbook': playbook.filename,
    }
    
    return JSONResponse(content={'message': 'Playbook uploaded successfully'}, status_code=201)

