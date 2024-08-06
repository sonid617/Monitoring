from flask import render_template
from app import app
from app.monitoring import get_system_metrics, get_disk_usage

@app.route('/')
def index():
    cpu, memory = get_system_metrics()
    disk = get_disk_usage()
    return render_template('index.html', cpu=cpu, memory=memory, disk=disk)
