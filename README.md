# Andriod-Dump
📱 Android Remote Media Access (Educational) A Python + Flask proof-of-concept project for securely accessing photos and videos from an Android device over the internet using a minimal HTTP API. This is intended strictly for educational and ethical use

📱 On Android (using Termux)
Install Termux
Download from F-Droid.
Update & Install Python and Flask
pkg update && pkg upgrade
pkg install python
pip install flask
Save the Flask server script
Create flask_server_on_android.py:

python

from flask import Flask, jsonify, send_file
import os

app = Flask(__name__)

@app.route("/photos", methods=["GET"])
def list_photos():
    photo_dir = "/sdcard/DCIM/Camera"
    files = os.listdir(photo_dir)
    return jsonify(files)

@app.route("/photo/<filename>", methods=["GET"])
def get_photo(filename):
    photo_dir = "/sdcard/DCIM/Camera"
    path = os.path.join(photo_dir, filename)
    return send_file(path, mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
Run the Flask server

python flask_server_on_android.py
⚠️ Make sure Termux has storage access:

bash
termux-setup-storage


💻 On Kali Linux
Install Python 3 and requests
sudo apt update
sudo apt install python3 python3-pip
pip3 install requests

Windows 10
Download Python
Run in cmd or PowerShell:
pip install requests
Save the client script

Create remote_android_client.py:

import requests

DEVICE_IP = "http://<ANDROID_LOCAL_IP>:5000"  # Replace with actual IP

try:
    response = requests.get(f"{DEVICE_IP}/photos")
    response.raise_for_status()
    photos = response.json()
    print(f"[+] Found {len(photos)} photo(s): {photos}")
except Exception as e:
    print(f"[!] Failed to fetch photos: {e}")
    exit()

if photos:
    first_photo = photos[0]
    download_url = f"{DEVICE_IP}/photo/{first_photo}"
    r = requests.get(download_url)
    with open(first_photo, "wb") as f:
        f.write(r.content)
    print(f"[+] Downloaded: {first_photo}")
else:
    print("[*] No photos found.")
Run the client


python3 remote_android_client.py   # Kali Linux
python remote_android_client.py    # Windows 10

🌐 Finding the Android Device IP
In Termux or phone settings:

ip a | grep wlan
OR: Check your Wi-Fi connection details.

✅ Example IP Setup
Android device IP: 192.168.1.10
Change this line in remote_android_client.py:
DEVICE_IP = "http://192.168.1.10:5000"
