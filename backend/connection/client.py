import socket
import os

host = os.getenv('HOST', 'localhost')
port = int(os.getenv('PORT', 12345))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((host, port))
    s.send(b'Hello, server!')
    data = s.recv(1024)
    print('Received:', repr(data))
finally:
    s.close()