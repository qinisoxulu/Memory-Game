import socket
import os

try:
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    print(f"Host: {host}")
    print(f"Port: {port}")
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
    print("Something went wrong while connecting to the servere")
    
