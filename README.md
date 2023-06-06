# Django Library App

## О приложении

 Веб-интерфейс для сотрудников библиотеки. Возможности: регистрация книг, авторов, читателей, маркировка книг и отслеживание их статуса, просмотр задолженности. Настроен API для взаимодействия со сторонними приложениями.

## Установка

### Prerequisites:

- python 3.9+
- pip


1. Скачайте репозиторий.
```
$ git clone https://github.com/j8r41/django_library.git
```

2. Активируйте виртуальное окружение.
```
$ cd django_library
$ python3 -m venv venv

#Linux, Mac:
$ source venv/bin/activate 

#Windows
$ source venv/Scripts/activate 
```

3. Установите requirements.
```
(venv) $ pip install -r requirements.txt
```

4. Укажите переменные среды.
```
$ touch .env
$ nano .env
```
```
SECRET_KEY=django-insecure-...
```
5. Запустите код.
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

### Docker:
```
$ cd django_library
$ docker compose build
$ docker compose up
```

## Разработчики:

- [j8r41](https://github.com/j8r41)
