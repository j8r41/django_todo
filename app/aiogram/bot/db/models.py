from sqlalchemy import Column, Integer, VARCHAR

from .base import Base


class TelegramUser(Base):
    __tablename__ = "accounts"

    user_id = Column(
        Integer, primary_key=True, unique=True, autoincrement=False
    )
    telegram_auth_key = Column(VARCHAR, unique=True)
