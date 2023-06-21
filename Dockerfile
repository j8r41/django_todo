FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

<<<<<<< HEAD
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY /app /code
=======
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY /app /app
>>>>>>> 9a5ef340f086152afa9757715e8b004c14f396dd
