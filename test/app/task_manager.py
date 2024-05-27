import time
import threading

tasks = []
task_outputs = {}

class Task:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.output = None

def get_tasks():
    return tasks

def add_task(task_name):
    task_id = len(tasks) + 1
    task = Task(task_id, task_name)
    tasks.append(task)
    threading.Thread(target=execute_task, args=(task,)).start()

def execute_task(task):
    # Simulazione di un task lungo
    time.sleep(5)
    task.output = f"Output for task {task.name}"
    task_outputs[task.id] = task.output

def get_task_output(task_id):
    return task_outputs.get(task_id, "No output available")
