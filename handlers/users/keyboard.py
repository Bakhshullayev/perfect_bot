from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove

import keyboards
from keyboards.default.new_keyboard import python_button
from keyboards.default.replay import menu
from loader import dp


@dp.message_handler(Command("menu"))
async def menu_keyboard(message: types.Message):
    await message.answer(f"Salom,{message.from_user.full_name}", reply_markup=menu)

@dp.message_handler(text="Python")
async def python(message: types.Message):
    await message.answer(f"Python dasturlash asoslari https://python.sariq.dev/", reply_markup=python_button)

@dp.message_handler(text="Telegram asoslari")
async def telegram_asoslari(message: types.Message):
    await message.answer("Mukammal telegram bot https://mohirdev.uz/courses/telegram/lesson/tugmalar-keyboards/")

@dp.message_handler(text="#00 Kirish")
async def boshiga(message: types.Message):
    await message.answer("https://python.sariq.dev/",reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text="Boshiga")
async def boshiga(message: types.Message):
    await message.answer(" Kurslarni tanlang", reply_markup=menu)
