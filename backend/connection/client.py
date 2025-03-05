import socket
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
port = int(os.getenv('PORT'))

try:
    if host is None or port is None:
        raise ValueError("Did you forget to set the enviroment variables for HOST or PORT?")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.send(b'Hello, server!')
        data = s.recv(1024)
        print('Received:', repr(data))
    finally:
        s.close()
except ValueError as err:
    print("Opps! ", err)
    
