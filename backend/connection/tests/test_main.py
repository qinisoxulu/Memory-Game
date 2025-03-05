import subprocess
import time

def test_main():
    process = subprocess.Popen(["python3", "main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    time.sleep(5)
    process.terminate()
    output, _ = process.communicate()
    assert "Server listening" in output
