from flask import Flask
import os
import subprocess
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    username = os.getenv("USER", "codespace")
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <pre>
    Name: Manish Mukhia
    Username: {username}
    Server Time (IST): {server_time}
    TOP Output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
