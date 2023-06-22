django-console:
	docker-compose exec django bash
telegram-bot-console:
	docker-compose exec telegram-bot bash
makemigrations:
	alembic revision -m ""
migrate:
	alembic upgrade head