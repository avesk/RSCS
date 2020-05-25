from flask import Flask, render_template, Response
app = Flask(__name__)

import cv2 as cv
import importlib

Camera = cv.VideoCapture(0)

app = Flask(__name__)

def make_480p():
    Camera.set(3, 640)
    Camera.set(4, 480)

make_480p()

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        ret, frame = camera.read()
        ret, jpeg = cv.imencode('.jpg', frame)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

@app.route('/video-feed')
def video_feed():
    return Response(gen(Camera),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
