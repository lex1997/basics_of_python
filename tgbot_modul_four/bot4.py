import logging
from random import randint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text, CommandStart
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.utils.callback_data import CallbackData

from config import *
from filters import AdminFilter
from keyboards import *

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


def get_simple_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = KeyboardButton(text='1')
    btn2 = KeyboardButton(text='2')
    kb.add(btn1)
    kb.add(btn2)
    return kb


def get_simple_kb1():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        KeyboardButton('Вы перешли с кнопки 1')
    ).add(KeyboardButton('Закрыть'))

    return kb


def get_simple_kb2():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
        KeyboardButton('Вы перешли с кнопки 2')
    ).add(KeyboardButton('Закрыть'))

    return kb


@dp.message_handler(commands='start')
async def menu_bot(msg: types.Message):
    await msg.answer('keyboard', reply_markup=get_simple_kb())


@dp.message_handler(Text(equals='1'))
async def menu_bot(msg: types.Message):
    await msg.answer('keyboard', reply_markup=get_simple_kb1())


@dp.message_handler(Text(equals='2'))
async def menu_bot(msg: types.Message):
    await msg.answer('keyboard', reply_markup=get_simple_kb2())


@dp.message_handler(Text(equals='Закрыть'))
async def menu_bot(msg: types.Message):
    await msg.answer('keyboard closed', reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
