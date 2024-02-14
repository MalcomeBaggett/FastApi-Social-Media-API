# How to setup a virtual environment

The command to create a virtual environment in windows is py -m venv <name> for example "py -m venv venv"

# How to select the python interpeter path in a virtual environment

press ctrl + shift + p, then look for the python interpeter and select the one that points to your virtual environment

# How to activate the venv

venv\Scripts\activate.bat

# How to start the server

uvicorn main:app --reload
