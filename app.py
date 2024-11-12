from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
@app.route('/htop')
def htop():
    name = "Gunjan"
    username = os.getenv("USER", "Unknown User")  # Safer username retrieval
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
    try:
        top_output = subprocess.getoutput("ps aux")  # Alternative to `top`
    except OSError as e:
        top_output = f"OS error occurred: {e}"
    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre><strong>Top Output:</strong>\n{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000 , debug=True)
