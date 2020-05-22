from flask import Flask, render_template, Response
from camera import Camera
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

