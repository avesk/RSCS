## Running the APP
`export FLASK_APP=App.py`

For localhost:
`flask run`

For Externally Visible Server
`flask run --host=0.0.0.0`

## Installation
If OpenCV fails to install with `pip install -r requirements.txt`, try:
`pip install opencv-contrib-python==4.1.0.25 --no-cache-dir`

## Backing Up + Restoring Pi Image:
https://pimylifeup.com/backup-raspberry-pi/

## Known Issues

# Time out of sync
Try running `sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"`

