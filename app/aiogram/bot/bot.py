import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from dotenv import load_dotenv
from handlers import commands
from middlewares import DbSessionMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


load_dotenv()


async def main():
    engine = create_async_engine(url=os.environ.get("DB_URL"), echo=True)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(token=os.environ.get("BOT_TOKEN"), parse_mode="HTML")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    # Setup dispatcher and bind routers to it
    dp = Dispatcher()
    dp.update.middleware(DbSessionMiddleware(session_pool=sessionmaker))
    # Automatically reply to all callbacks
    dp.callback_query.middleware(CallbackAnswerMiddleware())

    # Register handlers
    dp.include_router(commands.router)

    # Run bot
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
