import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 12345
s.connect((host, port))
s.send(b'Hello, server!')
data = s.recv(1024)
print('Received:', repr(data))
s.close()
