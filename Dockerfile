FROM python:3.10.12

COPY . .

CMD ["python", "manage.py", "makemigrations", "&", "migrate"]
