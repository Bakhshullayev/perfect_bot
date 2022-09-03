from aiogram import types
from aiogram.dispatcher.filters import Regexp

from loader import dp

phone_regex = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
mail_regex = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
qoshimcha = r"/mail:" + mail_regex


@dp.message_handler(Regexp(phone_regex))
async def regex_phone(msg: types.Message):
    await msg.answer("siz telefon raqam yubordingiz")

