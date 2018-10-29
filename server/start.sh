#!/bin/bash

# invoke virtualenv (need to call function in current shell context)
. ./setup.sh; activate

pip install -r requirements.txt

# Start server
python run.py
