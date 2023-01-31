FROM ubuntu:22.04

#MAINTAINER buho_team "sistemas@buho.media"

ENV PYTHONIOENCODING=utf-8


ADD deploy.sh /

# Setup apt
RUN apt-get update && apt-get install -y -u python3 curl ghostscript imagemagick openssh-server wget libpcap-dev libpq-dev python3-dev python3-setuptools git-core python3-pip build-essential python3-psycopg2
#graphviz graphviz-dev
RUN apt-get update -y

# Install required packages
RUN DEBIAN_FRONTEND=noninteractive sh deploy.sh requirements-docker

#upgrade pip
RUN pip3 install --upgrade pip

#fix bug simplejson
RUN pip3 install django-realtime --upgrade
RUN python3 -m pip install pip --upgrade

#install requirements
ADD requirements.txt /inventory/requirements.txt
RUN pip3 install -r /inventory/requirements.txt

WORKDIR /inventory


