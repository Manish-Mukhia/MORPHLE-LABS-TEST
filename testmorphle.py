from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Manish Mukhia"
    user = os.getenv("USER") or os.getenv("USERNAME") or "codespace"
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    # Run top command
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
   <p>Name: {name}</p>
   <p>User: {user}</p>
   <p>Server Time (IST): {ist_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
