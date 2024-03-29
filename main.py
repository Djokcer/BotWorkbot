import asyncio
import logging


from aiogram import Dispatcher, types, Bot
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Регина привет!")
    kb = [
        [types.KeyboardButton(text='С пюрешкой')],
        [types.KeyboardButton(text="Без пюрешки")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

@dp.message(Command("help"))
async def pro(message: Message):
    await message.answer(text='hkhkj', reply_markup=ike)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())