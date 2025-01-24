FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

COPY ./requirements.txt /
RUN pip install -r requirements.txt

COPY ./app /app
WORKDIR /app