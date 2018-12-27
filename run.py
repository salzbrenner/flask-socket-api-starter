from src import create_app, socketio
import os
from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit
# from gevent import monkey
# monkey.patch_all()

app = create_app(os.environ['APP_SETTINGS']).app
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app, debug=True)