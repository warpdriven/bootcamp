FROM python:3.7-buster

RUN pip3 install --upgrade pip
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app/src
COPY ./requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

COPY . /app
CMD python3 main.py
