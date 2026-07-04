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
        ],
        [
            KeyboardButton(text="Меню"),
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
        ],
        [
            KeyboardButton(text="Меню"),
        ]
    ],
    resize_keyboard=True
)

syefa=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Камень"),
            KeyboardButton(text="Ножницы"),
            KeyboardButton(text="Бумага")
        ],
        [
            KeyboardButton(text="Меню"),
        ]
    ],
    resize_keyboard=True
)