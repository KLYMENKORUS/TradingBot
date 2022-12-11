import time

from aiogram import Bot, types, executor, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold
from config import TOKEN_API
from test import get_data


bot = Bot(TOKEN_API, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_button = KeyboardButton('Start')
start_keyboard.add(start_button)


async def on_startup(_):
    print('Bot at work')


@dp.message_handler(commands='start')
async def get_command_start(message: types.Message):
    await bot.send_sticker(message.from_user.id,
                           sticker='CAACAgIAAxkBAAEGYktjbln34lkeFfHTOwfnziWnVufXOAACLgADRA3PF9utQcM3nS2YKwQ')
    await message.answer(f'Hello {hbold(message.from_user.first_name)}, \n'
                         f'I am a bot that simulates paper trading for you.\n'
                         f'Click the button to start 🚀', reply_markup=start_keyboard)


@dp.message_handler(Text(equals='Start'))
async def get_start_trade(message: types.Message):
    await message.reply(f'Ok, {hbold(message.from_user.first_name)}.\nWrite trading pair!')


@dp.message_handler()
async def get_command_message(message: types.Message):
    await message.reply("Wait a minute 🙏, I'm making a request...")

    get_data(message.text)

    with open('media/image.png', 'rb') as file:
        src = file.read()

    await bot.send_photo(message.from_user.id, photo=src, caption=f'Here is your trading result {message.text}')
    time.sleep(3)
    await message.answer(f'Press the button {hbold(message.from_user.first_name)} again to trade 🚀',
                         reply_markup=start_keyboard)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)