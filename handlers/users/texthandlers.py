from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import dp

@dp.message_handler(equals="salom", ignore_case=True)
@dp.message_handler(contains="Assalom Aleykum", ignore_case=True)
async def send_salom(message: types.Message):
    await message.reply("Vaaleykum Assalom")