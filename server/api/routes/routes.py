from flask import Flask
from api import app

@app.route('/')
def hello_world():
  return 'Hello, World!'
