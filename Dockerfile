# syntax=docker/dockerfile:1

FROM python:slim

WORKDIR /mnt

#COPY requirements.txt requirements.txt

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
 
RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip3 install pylint flake8
#RUN pip3 install -r requirements.txt