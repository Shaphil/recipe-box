FROM python:3.9-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y libpython3-dev default-libmysqlclient-dev build-essential && \
    pip install -r requirements.txt

COPY . /code/
