#!/usr/bin/env bash

# Activate the virtual environment
virtualenv .
source bin/activate
pip install -r requirements.txt

# Start server
python run.py
