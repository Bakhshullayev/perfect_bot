from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command

from loader import dp


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def send_video(message: types.Message):
    await message.answer("Siz video yubordingiz")  # bu handler videoni ajratadi


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def send_photo(message: types.Message):
    await message.answer("Siz rasm yubordingiz")  # bu handler rasmni ajratadi


@dp.message_handler(content_types=types.ContentType.VOICE)
async def send_voice(message: types.Message):
    await message.answer("Siz voice yubordingiz")  # bu handler voice ajratadi
