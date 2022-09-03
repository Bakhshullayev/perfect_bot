from aiogram import types
from aiogram.dispatcher.filters import Text

from loader import dp


@dp.message_handler(Text(equals="salom", ignore_case=True))
# @dp.message_handler(Text(contains="salom", ignore_case=True))
async def contains(msg: types.Message):
    await msg.reply("Assalom Aleykum yaxshimisiz")
