import os

class Config():
    roomID = None
    createProgress = False
    chatProgress = False
    knowledgePath = f"{os.getcwd()}/repository"
    ADMIN_TOKEN = "REDACTED"