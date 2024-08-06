from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Example user data for demonstration purposes
users = {
    "user": "password123",
    "admin": "adminpass"
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    # Mock data for demonstration
    cpu_usage = 25  # Replace with actual function call
    memory_usage = 55  # Replace with actual function call
    disk_usage = 65  # Replace with actual function call

    data = {
        'cpu': cpu_usage,
        'memory': memory_usage,
        'disk': disk_usage
    }

    return render_template('index.html', **data)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
