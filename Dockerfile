FROM python:3.6-slim


RUN apt-get update &&\
    apt-get -y install gcc && \
    rm -rf /var/lib/apt/lists/*

ENV PYTHONBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

RUN pip install -r requirements.txt
ADD . /code/