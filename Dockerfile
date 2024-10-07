FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install mysql-connector-python boto3

CMD ["python", "ingesta.py"]

