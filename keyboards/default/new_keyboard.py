from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

python_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#00 Kirish"),
            KeyboardButton(text="#01 Kerakli dastular"),
            KeyboardButton(text="#02 Hello World"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],
    ],resize_keyboard=True
)