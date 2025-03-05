import socket
import threading
import time
import server

def start_server():
    threading.Thread(target=server.__name__, daemon=True).start()
    time.sleep(1)

def test_server_response():
    start_server()
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 12345))
    message = "qiniso: Hello, Everyone!"
    client.sendall(message.encode())
    response = client.recv(1024).decode()
    assert response == message
    client.close()
