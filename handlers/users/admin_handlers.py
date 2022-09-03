from imaplib import Command

from aiogram import types
from aiogram.dispatcher import filters

from loader import dp

@dp.message_handler(filters.Command("change_photo", filters.AdminFilter()))
@dp.message_handler(commands="xarid", is_chat_admin=True)
async def admin(msg: types.Message):
    await msg.answer("di")