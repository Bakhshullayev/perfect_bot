from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import dp


@dp.message_handler(Command(['til', 'vaqt']))
# @dp.message_handler(commands=['til', 'vaqt'])
async def get_language(message: types.Message):
    await message.answer("Til o'zgardi")
