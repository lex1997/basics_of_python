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


async def set_default_commands(bot: Bot):
    return await bot.set_my_commands(
        commands=[
            BotCommand('menu', 'Вывести меню'),
            BotCommand('help', 'Помощь'),
            BotCommand('support', 'Поддержка'),
        ],
        scope=BotCommandScopeDefault()
    )


@dp.message_handler(AdminFilter(), CommandStart())
async def admin_start(message: types.Message):
    await message.reply('Комманды установлены')
    await set_default_commands(message.bot)


def get_menu():
    menu_kb = InlineKeyboardMarkup(row_width=2)
    pizza_button = InlineKeyboardButton(text='Пицца', callback_data='pizza_cat')
    snacks_button = InlineKeyboardButton(text='Закуски', callback_data='snacks_cat')
    menu_kb.insert(pizza_button)
    menu_kb.insert(snacks_button)
    return menu_kb


@dp.message_handler(commands='menu')
async def menu_bot(message: types.Message):
    await message.answer('Добро пожаловать в доставку пиццы', reply_markup=get_menu())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)