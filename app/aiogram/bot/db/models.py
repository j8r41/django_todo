from sqlalchemy import Column, Integer

from .base import Base


class TelegramUser(Base):
    __tablename__ = "telegram_users"

    user_id = Column(
        Integer, primary_key=True, unique=True, autoincrement=False
    )
    telegram_auth_key = Column(Integer, unique=True)
