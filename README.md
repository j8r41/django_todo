# Django Do App

## About

To-do list and task management app. Supported many users.

## Install

### Prerequisites:

- python 3.9+
- pip


1. Download the repository.
```
$ git clone https://github.com/j8r41/django_todo.git 
```

2. Activate enviroment.
```
$ cd django_todo
$ python3 -m venv venv

#Linux, Mac:
$ source venv/bin/activate 

#Windows
$ source venv/Scripts/activate 
```

3. Install requirements.
```
(venv) $ pip install -r requirements.txt
```

4. Note environment variables as in .envexample or just copy:
```
$ touch .env
$ nano .env
```
```
SECRET_KEY=Your-Secret-Key
POSTGRES_ENGINE = django.db.backends.postgresql_psycopg2
POSTGRES_DB=postgres
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```
5. Ruun code.
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py collectstatic
$ python3 manage.py runserver
```

### Docker:
```
$ cd django_library
$ docker compose build
$ docker compose up
```

