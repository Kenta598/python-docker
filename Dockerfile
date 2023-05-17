# syntax=docker/dockerfile:1

FROM python:slim

WORKDIR /mnt

#COPY requirements.txt requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install pylint flake8
#RUN pip3 install -r requirements.txt