from flask import Flask
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode="threading", debug=True)

from api import controller
