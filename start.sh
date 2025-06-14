#!/bin/bash
cd "$(dirname "$0")"  # ensures the script runs from its own folder

# Create virtual environment if not exists
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install/update dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Run the bot
python bot/main.py