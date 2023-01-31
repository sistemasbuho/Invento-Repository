#!/bin/bash  

if [ "$*" = "requirements-docker" ] 
then
	# Install required packages
	apt-get -qq install -y -u python3 curl ghostscript imagemagick openssh-server wget libpcap-dev libpq-dev python3-dev python3-setuptools git-core python3-pip build-essential python3-psycopg2

	#upgrade pip
	pip install --upgrade pip

fi

if [ "$*" = "requirements" ] 
then
	# Install required packages
	apt-get -qq install -y -u python3 curl ghostscript imagemagick openssh-server wget libpcap-dev libpq-dev python3-dev python3-setuptools git-core python3-pip build-essential python3-psycopg2

	#upgrade pip
	sudo pip install --upgrade pip

	#install requirements
	sudo pip install -r requirements.txt

fi

if [ "$*" = "new_db" ] 
then
	python manage.py migrate ingestiondemo zero 
	python manage.py makemigration 
	python manage.py migrate 
fi

if [ "$*" = "update_db" ] 
then
	python manage.py makemigration 
	python manage.py migrate 
fi

if [ "$*" = "static" ] 
then
	python manage.py collectstatic
fi

if [ "$*" = "reset_pass" ] 
then
	python manage.py changepassword admin
fi

if [ "$*" = "postgres-dump" ] 
then
	pg_dump -h localhost -p 5432 -U ingestion_admin -F c -b -v -f /webapp/claritysocial_cancilleria/backups/cancilleria_$(date +%Y-%m-%d-%H_%M).backup -d cancilleria
fi

if [ "$*" = "postgres-restore" ] 
then
	'pg_restore -h localhost -p 5432 -U ingestion_admin -d cancilleria -v "/webapp/claritysocial_cancilleria/cancilleria-producion.backup"'
fi
