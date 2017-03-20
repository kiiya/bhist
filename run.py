from flask import Flask, render_template, url_for, redirect
from datetime import datetime
import subprocess
import os


app = Flask(__name__)

@app.route('/')
def index():
    history = []
    commands = {}
    with open('/home/dev/.bash_history', 'r') as f:
        for line in f.readlines():
            line.strip('') 
            if line.startswith('#'):
                cmd_unix_date = line.replace("#", "")
                cmd_date = datetime.fromtimestamp(int(cmd_unix_date)).strftime('%Y-%m-%d %H:%M:%S')
                continue
            commands = {
                "date": cmd_date,
                "cmdd": line
            }
            history.append(commands)
    return render_template('index.html', history=history)


@app.route('/clear')
def clear_history():
    subprocess.Popen(['/bin/bash', '-c', 'cat /dev/null > ~/.bash_history && history -c && exit'])
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")