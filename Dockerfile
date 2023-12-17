FROM python:3.10
WORKDIR app

COPY ./insurance ./insurance
COPY ./requirements.txt .
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m venv .venv
RUN . .venv/bin/activate
RUN pip install --upgrade pip
RUN pip install -r requirements.txt