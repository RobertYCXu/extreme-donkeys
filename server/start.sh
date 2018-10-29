#!/usr/bin/env bash

# Activate the virtual environment
source bin/activate
pip install -r requirements.txt

# Start server
python run.py
