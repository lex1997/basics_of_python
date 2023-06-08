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


def get_inliine_kb():
    inline_kb = InlineKeyboardMarkup()
    btns = [
        InlineKeyboardButton('1', callback_data='1'),
        InlineKeyboardButton('2', callback_data='2')
    ]
    inline_kb.add(*btns)
    return inline_kb


def get_inliine_kb1():
    inline_kb = InlineKeyboardMarkup()
    btns = [
        InlineKeyboardButton('вперед', callback_data='f1'),
        InlineKeyboardButton('закрыть', callback_data='back')
    ]
    inline_kb.add(*btns)
    return inline_kb


@dp.message_handler(commands='start')
async def menu_bot(msg: types.Message):
    await msg.answer('inline', reply_markup=get_inliine_kb())


@dp.callback_query_handler(Text(equals='1'))
async def btn1(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.answer('Нажата кнопка 1', reply_markup=get_inliine_kb1())


@dp.callback_query_handler(Text(equals='back'))
async def btn1(cb: types.CallbackQuery):
    await cb.answer()
    await cb.message.answer('Вы вернулись в главное меню', reply_markup=get_inliine_kb())




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
