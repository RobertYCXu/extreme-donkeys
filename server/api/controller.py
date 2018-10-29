from flask import Flask
from models import Game
from api import app

global games
games = {}

@app.route('/')
def index():
  return 'Hello, World!'

@app.route('/game/<key>')
def get_game(key):
  output = ""

  if key not in games:
    games[key] = Game(key)
    output += "Invalid Key! Game created \n"
  
  game = games[key]
  output += game.serialize() + '\n'
  return output
