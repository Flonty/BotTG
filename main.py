import asyncio
import logging
import sys
import os
from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from dotenv import load_dotenv

from keyboard import main_keyboard, menu_keyboard, game_keyboard

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
dp = Dispatcher()
@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"салам родной, {html.bold(message.from_user.full_name)}!\n"
                         f"выбери действие на клавиатуре", reply_markup=main_keyboard)
@dp.message(Command("help"))
async def command_help_handler(message:Message):
    await message.answer(f"Вы используйте команду helpo \n"
                         f"доступные команды: \n"
                         f"/start для запуска \n"
                         f"/help помощь \n"
                         f"/about инфа о боте\n"
                         f"/contacs контакты \n" )
@dp.message(Command("about"))
async def command_start_handler(message: Message):
    await message.answer("Этот крутейший бот сделал иван")
@dp.message(Command("contacts"))
async def command_start_handler(message: Message):
    await message.answer("Это команда контакты")
@dp.message(F.text.lower().in_({'привет', 'здарова',"салам"}))
async def message_hello(message:Message):
    await message.answer_photo(photo="https://avatars.mds.yandex.net/i?id=c1f03981f3b9138b6ed4e063135ed120d96c3532-4297303-images-thumbs&n=13",
    caption="салам радной, как дела?")
@dp.message(F.text.lower() == 'норм')
async def message_hello(message: Message):
    photo=FSInputFile('media/8MuYPfKrX3pLX455qBb0p1LpTheb8V6iiVtAH-j691Zcc_0aSqueNM2OKjSHeHSgVTZ577_9Tn7U5VVqvZBDU37a.jpg')
    await message.answer_photo(photo=photo, caption='это дерево')
@dp.message(F.text=="Меню")
async def message_hello(message:Message):
    await message.answer("Вы попали в меню",  reply_markup=menu_keyboard)
@dp.message(F.text=="О боте")
async def message_hello(message:Message):
    await message.answer("Это крутой бот")
@dp.message(F.text=="Играть")
async def message_hello(message:Message):
    await message.answer("Выберите игру",  reply_markup=game_keyboard)
@dp.message(F.text=="О игре")
async def message_hello(message:Message):
    await message.answer("Очень крутые игры")
@dp.message()
async def echo_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())