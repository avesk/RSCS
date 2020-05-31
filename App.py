from flask import Flask, render_template, Response, request
app = Flask(__name__)

import cv2 as cv
import importlib
import sys
import time

from VideoCapture import VideoCapture

Camera = VideoCapture()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    fps = 0
    frames_sample = 30
    counter = frames_sample
    start = time.time()
    while True:
        jpg = camera.capture(fps)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpg.tobytes() + b'\r\n')
        
        # Keep running estimation of frame rate
        counter -= 1
        if counter == 0:
            end = time.time()
            seconds = end - start
            fps = frames_sample / seconds
            print(f"FRAME RATE: {fps}")
            counter = frames_sample
            start = time.time()

@app.route('/video-feed')
def video_feed():
    return Response(gen(Camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/post/command', methods=['GET', 'POST'])
def command():
    json_data = request.get_json()
    print(json_data['cmd'])
    return Response(json_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
