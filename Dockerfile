FROM python:3.11.6

WORKDIR /app


COPY requirements.txt .
RUN pip install -r /app/requirements.txt

COPY ./src /app/