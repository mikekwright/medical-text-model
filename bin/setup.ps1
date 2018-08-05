echo "Creating virtual environment"

python -m venv .venv

echo "Activating virtual environment"

.venv\Scripts\activate

echo "Enabling Jupyter Extension"

jupyter contrib nbextension install --user

echo "Enabling the vim extension"

jupyter nbextension enable select_keymap/main

echo "If you would like to add more extension navigate to localhost:8888/nbextensions when notebook is running"
