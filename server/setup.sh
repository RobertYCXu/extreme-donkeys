#!/bin/sh
# Activate the virtual environment
if [ ! -f pip-selfcheck.json ]; then
  virtualenv .
fi

activate () {
  . ./bin/activate
}

activate


