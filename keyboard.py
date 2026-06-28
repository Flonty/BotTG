from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="О боте")
        ],
        [
            KeyboardButton(text="Играть"),
            KeyboardButton(text="О игре")
        ]
    ],
    resize_keyboard=True
)

menu_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Настройки"),
            KeyboardButton(text="Режимы")
        ],
        [
            KeyboardButton(text="Профиль"),
            KeyboardButton(text="О нас")
        ]
    ],
    resize_keyboard=True
)

game_keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стандоф"),
            KeyboardButton(text="Суефа")
        ],
        [
            KeyboardButton(text="кс2"),
            KeyboardButton(text="не кс2")
        ]
    ],
    resize_keyboard=True
)