from flask import Flask, render_template, Response, request, session
from flask_session import Session

import cv2 as cv
from datetime import timedelta
import importlib
import sys
import time
import json

from VideoCapture import VideoCapture
from Commands import Commands
from command_map import command_map 
 
app = Flask(__name__)
Camera = VideoCapture()
commands = Commands()

app = Flask(__name__)

SESSION_TYPE = 'redis'
app.config.from_object(__name__)
Session(app)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=10)

@app.route('/')
def index():
    is_active = session.get('active', 'no')
    if is_active == request.remote_addr or is_active == 'no':
        return render_template('index.html')
    else:
        return render_template('bot_in_use.html') 

def gen(camera):
    fps = 0
    frames_sample = 30
    counter = frames_sample
    start = time.time()
    while True:
        jpg = camera.capture(fps)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + jpg.tobytes() + b'\r\n\r\n')
        
        # Keep running estimation of frame rate
        counter -= 1
        if counter == 0:
            end = time.time()
            seconds = end - start
            fps = frames_sample / seconds
            counter = frames_sample
            start = time.time()

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/post/command', methods=['GET', 'POST'])
def command():
    session['active'] = request.remote_addr
    json_data = json.loads(request.data)
    cmd_code = json_data['cmd']
    if cmd_code in command_map:
        cmd = command_map[f'{cmd_code}']
        getattr(commands, cmd)()

    return Response(json_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
