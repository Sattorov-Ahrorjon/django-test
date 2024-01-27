FROM python:3.10.12

WORKDIR /root/main

COPY . /root/main/

RUN pip install -r /root/main/requirements.txt

RUN python /root/main/manage.py makemigrations

RUN python /root/main/manage.py migrate
