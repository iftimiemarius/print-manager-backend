FROM python:3.8.3-slim-buster

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY main.py /src
