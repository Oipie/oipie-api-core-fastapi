# syntax=docker/dockerfile:1

FROM python:3.10.8-slim

WORKDIR /python-docker

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN pip install poetry==1.2.2

RUN poetry config virtualenvs.create false
RUN poetry install --only main

COPY . .
ENTRYPOINT [ "uvicorn", "src.main:app", "--host", "0.0.0.0" ]