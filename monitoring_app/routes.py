from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Example user data for demonstration purposes
users = {
    "user": "password123",
    "admin": "adminpass"
}

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
