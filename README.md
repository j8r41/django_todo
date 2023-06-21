# Django Do App

## About

To-do list and task management app. Supported many users, task compliting and discussing by multiple users, task sorting and searching, e-mail-verification. [Details here.](https://github.com/j8r41/django_todo/blob/master/task.txt)

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
#Django:
SECRET_KEY=Your-Secret-Key
#DB
POSTGRES_ENGINE = django.db.backends.postgresql_psycopg2
POSTGRES_NAME=postgres
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
SERVER_EMAIL=example@example.com
#Email
EMAIL_HOST=smtp.example.com
EMAIL_HOST_USER=example@example.com
EMAIL_HOST_PASSWORD=password
EMAIL_PORT=587
EMAIL_SUBJECT_PREFIX=example
DEFAULT_FROM_EMAIL=example@example.com

#Aiogram3:
BOT_TOKEN = 9999999999999:sdafsdf23234-asdasdgsd-sdf124123
#DB
DB_URL=postgresql+psycopg://postgres:postgres@db-telegram-bot/postgres
```

5. Run code.

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
