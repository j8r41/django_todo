# Django To Do App + Aiogram3 Telegram bot

## About

To-do list and task management app. Supported many users, task compliting and discussing by multiple users, task sorting and searching, e-mail-verification. Linked with telegram bot, that send task list. [Details here.](https://github.com/j8r41/django_todo/blob/master/task.txt)

## Install

### Prerequisites:

- python 3.10+
- Docker

1. Download the repository.

```
$ git clone https://github.com/j8r41/django_todo.git
```

2. Note environment variables as in .envexample or just copy:

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



### Run Docker:

```
$ cd django_todo
$ docker compose build
$ docker compose up
$ docker compose exec telegram-bot bash
$ alembic revision -m "create accounts table"
$ alembic upgrade head
```
