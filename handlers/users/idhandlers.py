from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import dp

SUPERUSER = 941554680


# BLACKLIST =

@dp.message_handler(chat_id=SUPERUSER, text='salom')
async def send_user(message: types.Message):
    await message.answer("Salom Superuser")
