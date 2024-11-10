<<<<<<< HEAD
FROM python:3.9-slim
=======
FROM python:3.10-slim-buster
>>>>>>> 85ce0e2c5d1859517d42a270631f75e357e7d9f0

WORKDIR /Diamond-Price-app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3","app.py"]
