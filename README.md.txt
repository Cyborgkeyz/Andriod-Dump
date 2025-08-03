# 📱 Android Remote Media Access (Educational)

A Python + Flask proof-of-concept project that enables secure, remote access to photos and videos from an Android device with user permission. Designed strictly for **educational purposes** — this project demonstrates how to use HTTP APIs and Python to interact with Android storage over the internet or local network.

> ⚠️ This tool is **not intended for unauthorized use**. Only use it on devices you own or have explicit permission to access. Misuse could violate privacy laws or mobile platform terms of service.

---

## 🔧 Features

- 🖼️ List and download media from the Android `/sdcard/DCIM/Camera` folder
- 🌐 Flask-based web server runs directly on the Android device (via Termux or QPython)
- 🔄 Python client downloads media files over HTTP
- 👨‍💻 Educational REST API design and mobile data access principles

---

## 📦 Requirements

### On the Android Device

- [Termux](https://f-droid.org/packages/com.termux/) or [QPython](https://play.google.com/store/apps/details?id=org.qpython.qpy)
- Python 3
- Flask

```bash
pip install flask
