FROM python:3.10.12

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "makemigrations", "&", "migrate"]
