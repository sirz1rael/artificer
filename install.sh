echo "Welcome to setup of Artificer! version 0.2"
echo "Python version: " && python --version
python -m venv env

source ./env/bin/activate

pip install -U termcolor pyinstaller

pyinstaller --onefile --contents-directory "." artificer.py
sudo cp ./dist/artificer //usr/bin/
