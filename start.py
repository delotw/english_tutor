import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from app.modules.handlers import router

# логирование
logging.basicConfig(level=logging.INFO)


async def main():
    # загрузка констант из .env
    load_dotenv()
    # инциализация бота и диспетчера
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    logging.info("Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
