# syntax=docker/dockerfile:1

FROM python:3.11.0-slim

WORKDIR /python-docker

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN pip install poetry==1.2.0

RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .
ENTRYPOINT [ "uvicorn", "src.main:app", "--host", "0.0.0.0" ]