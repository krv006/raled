FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

COPY pyproject.toml poetry.lock /code/

RUN pip install --no-cache-dir poetry

ENV PATH="/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

RUN poetry install --no-dev --no-root

COPY . /code/

ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD

ENV DB_NAME $DB_NAME
ENV DB_USER $DB_USER
ENV DB_PASSWORD $DB_PASSWORD
