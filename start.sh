#!/bin/bash

# Navigate to the project directory
cd /home/oem/green-elm-title-page || exit

# Correct the permissions of the private key file
chmod 600 /home/oem/.ssh/id_rsa || exit

# Pull the latest changes from the repository
git pull || exit

# Install the required Python packages
/home/oem/green-elm-title-page/venv/bin/python -m pip install -r requirements.txt || exit

# Run the Flask application
/home/oem/green-elm-title-page/venv/bin/python green-elm-title-app.py || exit


