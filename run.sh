pip3 install flask
pip3 install line-bot-sdk
pip3 install gunicorn

export FLASK_APP=app.py
export FLASK_DEBUG=1 
flask run --host=0.0.0.0