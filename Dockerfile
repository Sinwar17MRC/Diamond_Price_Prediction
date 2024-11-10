FROM python:3.11.9-slim-buster

WORKDIR /Diamond-Price-app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3","app.py"]