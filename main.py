from flask import Flask, jsonify, send_file, abort, request
import os
import mimetypes
from functools import wraps

app = Flask(__name__)

PHOTO_DIR = "/sdcard/DCIM/Camera"
USERNAME = "admin"
PASSWORD = "changeme"  # Change this to a strong password

def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return jsonify({"error": "Authentication required"}), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/photos", methods=["GET"])
@requires_auth
def list_photos():
    if not os.path.exists(PHOTO_DIR):
        return jsonify({"error": "Photo directory not found"}), 404
    files = [f for f in os.listdir(PHOTO_DIR) if os.path.isfile(os.path.join(PHOTO_DIR, f))]
    return jsonify(files)

@app.route("/photo/<filename>", methods=["GET"])
@requires_auth
def get_photo(filename):
    path = os.path.join(PHOTO_DIR, filename)
    if not os.path.isfile(path):
        abort(404)
    mime_type, _ = mimetypes.guess_type(path)
    return send_file(path, mimetype=mime_type or "application/octet-stream")
from flask import Flask, jsonify, send_file, abort, request
import os
import mimetypes
from functools import wraps

app = Flask(__name__)

PHOTO_DIR = "/sdcard/DCIM/Camera"
VIDEO_DIR = "/sdcard/DCIM/Camera"  # Change if your videos are in a different folder
USERNAME = "admin"
PASSWORD = "changeme"  # Change this to a strong password

def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return jsonify({"error": "Authentication required"}), 401, {'WWW-Authenticate': 'Basic realm="Login Required"'}

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route("/photos", methods=["GET"])
@requires_auth
def list_photos():
    if not os.path.exists(PHOTO_DIR):
        return jsonify({"error": "Photo directory not found"}), 404
    files = [f for f in os.listdir(PHOTO_DIR) if os.path.isfile(os.path.join(PHOTO_DIR, f))]
    return jsonify(files)

@app.route("/photo/<filename>", methods=["GET"])
@requires_auth
def get_photo(filename):
    path = os.path.join(PHOTO_DIR, filename)
    if not os.path.isfile(path):
        abort(404)
    mime_type, _ = mimetypes.guess_type(path)
    return send_file(path, mimetype=mime_type or "application/octet-stream")

@app.route("/videos", methods=["GET"])
@requires_auth
def list_videos():
    if not os.path.exists(VIDEO_DIR):
        return jsonify({"error": "Video directory not found"}), 404
    video_extensions = (".mp4", ".avi", ".mov", ".mkv")
    files = [
        f for f in os.listdir(VIDEO_DIR)
        if os.path.isfile(os.path.join(VIDEO_DIR, f)) and f.lower().endswith(video_extensions)
    ]
    return jsonify(files)

@app.route("/video/<filename>", methods=["GET"])
@requires_auth
def get_video(filename):
    path = os.path.join(VIDEO_DIR, filename)
    if not os.path.isfile(path):
        abort(404)
    mime_type, _ = mimetypes.guess_type(path)
    return send_file(path, mimetype=mime_type or "application/octet-stream")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=true)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=true)