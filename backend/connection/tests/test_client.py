import subprocess
import time

def test_client():
    server_process = subprocess.Popen(["python3", "server.py"])
    time.sleep(1)
    client_process = subprocess.Popen(["python3", "client.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    client_process.stdin.write("qiniso\n")
    client_process.stdin.write("Hello, Everyone!\n")
    client_process.stdin.write("exit\n")
    client_process.stdin.flush()
    output = client_process.stdout.read()
    assert "qiniso: Hello, Everyone!" in output
    client_process.terminate()
    server_process.terminate()
