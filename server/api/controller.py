from flask import Flask, request

from models import Game, User
from api import app, socketio
import json

global games
games = {}

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/game/<key>', methods=["post"])
def join_game(key):
  debug = ""
  data = request.json

  # Get or create game
  if key not in games:
    games[key] = Game(key)
    debug += "Invalid Key! Game created \n"
  
  game = games[key]

  # Create player
  if "user" not in data:
    debug += "invalid data!"
    return debug

  user = User(data["user"])
  if not game.add_user(user):
    debug += "failed to add"
    return debug

  debug += game.serialize() + '\n'
  return debug

@socketio.on('message')
def handle_message(message):
  print('received message: ' + message)
