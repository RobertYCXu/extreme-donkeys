from flask import Flask, request
from flask_socketio import emit, send, join_room, leave_room
from models import Game, User
from api import app, socketio
import json

global games
games = {}

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/game/<key>', methods=["post"])
def enter_game(key):
  debug = ""

  # Get or create game
  if key not in games:
    games[key] = Game(key)
    debug += "Invalid Key! Game created \n"
  
  game = games[key]

  debug += game.serialize() + '\n'
  return debug

@socketio.on('join')
def join_game(data):
  game = games[data["key"]]
  user = User(data["user"])
  
  if game.add_user(user):
    join_room(game.key)
    emit("new_user", {"user": user.name}, room = game.key)
  else:
    emit("new_user", "failed")

@socketio.on('leave')
def leave_game(data):
  game = games[data["key"]]

  if game.remove_user(data["user"]):
    leave_room(game.key)
    emit("user_left", {"user": data["user"]}, room = game.key)

    if game.num_users <= 0:
      del games[game.key]

@socketio.on('update')
def update(data):
  game = games[data["key"]]
  
  # Just bounce the data to the room for now
  emit("update", data, room = game.key)
