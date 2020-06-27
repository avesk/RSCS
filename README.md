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

## VPN Setup

### Administrator Access
Starting the VPN:
* Contact support and request Administrative access, you will have to give them your public IP address. Support will whitelist your IP and send you the `VPN URL`, `admin user name` and temporary `password`. 
* Visit the `VPN URL`/`admin` page and log in with your credentials.
* Go to User `Management > User Permissions` and select the `More settings` button next to your `admin user name`. Change your password to something secure, select `Save Settings`.
* Once the page reloads hit `Update Running Server`.
* Now, visit the `VPN URL`, and download your user locked client config file.
* Also visit the link and download the `OpenVPN Connect` for your OS.

![img](img/dl-client-config.png)
* Follow the instructions for connecting to your VPN through `OpenVPN Connect`. You will need your `VPN URL`, `user name`, and `password`.
* You now should be connected to the VPN!

### Registering Remote Operators
* For auto-login profiles: `sudo openvpn --config client.ovpn`

#### Time out of sync
Try running `sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"`

### More info:
[Connecting To Access Server With Linux](https://openvpn.net/vpn-server-resources/connecting-to-access-server-with-linux/)

