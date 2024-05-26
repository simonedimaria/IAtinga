#!/usr/bin/env python3
from os import system
from pwn import remote, context, args

context.log_level = "error"

if args.REMOTE:
    ip = args.HOST
    rpc_port = args.RPC_PORT
    tcp_port = args.TCP_PORT
    RPC_URL = f"http://{ip}:{int(rpc_port)}/"
    TCP_URL = f"{ip}:{int(tcp_port)}"
else:
    RPC_URL = "http://localhost:1337/"
    TCP_URL = "localhost:1338"


if __name__ == "__main__":
    pass
