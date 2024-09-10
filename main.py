import os
import sys
import logging
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command


from handlers import start_handler

async def main():
    load_dotenv()
    bot = Bot(os.getenv("TOKEN"))
    dp = Dispatcher()
    
    dp.message.register(start_handler, Command(commands=["start", "run"]))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
