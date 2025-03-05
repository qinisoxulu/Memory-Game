import socket

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = os.getenv('HOST')
    port = int(os.getenv('PORT'))
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = client_socket.recv(1024)
        print("Received:", data.decode())
        response = b"Hello, client!"
        client_socket.sendall(response)
        client_socket.close()
except:
    print("Something went wrong will connecting to the user!")
