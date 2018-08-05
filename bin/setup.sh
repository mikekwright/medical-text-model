#!/usr/bin/env bash
#vim :set filetype=sh:

set -e

echo -e "Creating virtual environment"
python -m venv .venv

echo -e "Activating virtual environment"
source .venv/bin/acivate

echo "Enabling Jupyter Extension"
jupyter contrib nbextension install --user

echo "Enabling the vim extension"
jupyter nbextension enable select_keymap/main

echo "If you would like to add more extension navigate to localhost:8888/nbextensions when notebook is running"
