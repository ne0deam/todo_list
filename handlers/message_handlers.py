from aiogram import types

async def start_handler(message: types.Message):
    await message.answer(
        f"Добро пожаловать {message.from_user.full_name}, в To Do List телеграмм бот"
    )