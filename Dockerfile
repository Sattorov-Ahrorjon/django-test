FROM python:3.10.12

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

#CMD ["python", "manage.py", "makemigrations", "&", "migrate"]
