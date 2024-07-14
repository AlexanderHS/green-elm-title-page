import psutil
from flask import Flask, render_template, request

app = Flask(__name__)

def get_disk_usage():
    try:
        disk_usage = psutil.disk_usage('/home')
    except FileNotFoundError:
        disk_usage = psutil.disk_usage('/')
    total = disk_usage.total // (2**30)  # Convert bytes to gigabytes
    used = disk_usage.used // (2**30)
    free = disk_usage.free // (2**30)
    percent = disk_usage.percent
    return {'total': total, 'used': used, 'free': free, 'percent': percent}

@app.route('/')
def index():
    disk_usage = get_disk_usage()
    return render_template('index.html', disk_usage=disk_usage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
