from flask import Flask
from flask import render_template
import socket

app = Flask(__name__)


@app.route("/")
def hello_world():
    return socket.gethostname()

