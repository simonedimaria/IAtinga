from config import Config
import os, uuid, subprocess

def readFile(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except:
        return None

def getRepository(topic):
    for suffix in ['', '.md']:
        repoFile = f"{Config.knowledgePath}/{topic}{suffix}"
        print(repoFile)
        if os.path.exists(repoFile):
            return readFile(repoFile)
    return None

def cleanup(filename):
    try:
        os.remove(filename)
    except:
        pass