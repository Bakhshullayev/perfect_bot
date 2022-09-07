from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup

from keyboards.default.start import menustart
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name},!")
    await message.answer(f"Telefon va manzilingizni yuboring",reply_markup=menustart)
