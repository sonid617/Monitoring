from flask import Flask

app = Flask(__name__)

from monitoring_app import routes
