import socket
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
port = int(os.getenv('PORT'))

try:
    if (host or port) is None:
        raise ValueError("HOST or PORT environment variable is not set.")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.send(b'Hello, server!')
        data = s.recv(1024)
        print('Received:', repr(data))
    finally:
        s.close()
except:
    print("Something went wrong while connecting to the servere!")
    
