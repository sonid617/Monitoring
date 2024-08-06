from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    data = {
        'cpu': cpu_usage,
        'memory': memory_info.percent,
        'disk': disk_usage.percent
    }
    
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

