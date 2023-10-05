from python:3.9-slim
WORKDIR /app
copy requirements.txt requirements.txt
run apt-get update
run apt-get -y install gcc
run pip3 install -r requirements.txt
copy . .

env  FLASK_APP=hello.py

CMD [ "python3", "-m", "flask","run","--host=0.0.0.0" ]