from flask import Flask, render_template
from monitoring import get_cpu_usage, get_memory_usage, get_disk_usage

app = Flask(__name__)

@app.route('/')
def index():
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()

    data = {
        'cpu': cpu_usage,
        'memory': memory_usage,
        'disk': disk_usage
    }

    return render_template('index.html', **data)
