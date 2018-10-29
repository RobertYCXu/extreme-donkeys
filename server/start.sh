#!/usr/bin/env bash

# Activate the virtual environment
if [ ! -f pip-selfcheck.json ]; then
  virtualenv .
fi

source bin/activate
pip install -r requirements.txt

# Start server
python run.py
