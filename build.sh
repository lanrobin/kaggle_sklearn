#!/usr/bin/sh
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
    echo "creating venv."
else
    echo ".venv exists, skip creating venv."
fi

source .venv/bin/activate

pip3 install -r requirements.txt
