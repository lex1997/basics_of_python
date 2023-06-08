import logging
from random import randint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, CommandStart
from aiogram.types import BotCommand, BotCommandScopeDefault
from aiogram.utils.callback_data import CallbackData
from aiogram.dispatcher.filters.state import State, StatesGroup

from config import *
from filters import AdminFilter
from keyboards import *

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

available_food_names = [
    'суши',
    'спагетти',
    'хачапури'
]

available_food_sizes = [
    'маленькая',
    'средняя',
    'большая'
]


class OrderFood(StatesGroup):
    waiting_for_food_name = State()
    waiting_for_food_size = State()


async def food_start(msg: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_food_names:
        keyboard.add(name)
    await msg.answer('Выберите блюдо:', reply_markup=keyboard)
    await OrderFood.waiting_for_food_name.set()


async def food_chosen(msg: types.Message, state: FSMContext):
    if msg.text.lower() not in available_food_names:
        await msg.answer('Выберите блюдо используя клавиатуру ниже')
        return
    await state.update_data(chosen_food=msg.text.lower())
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in available_food_sizes:
        keyboard.add(size)
    await msg.answer('Теперь выберите размер порции:', reply_markup=keyboard)
    await OrderFood.next()


async def food_size_chosen(msg: types.Message, state: FSMContext):
    if msg.text.lower() not in available_food_names:
        await msg.answer('Выберите размер порции используя клавиатуру ниже')
        return
    user_data = await state.get_data()
    await msg.answer(f'Вы заказали {msg.text.lower()} порцию {user_data["chosen_food"]}.\n',
                     reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_food(dp: Dispatcher):
    dp.register_message_handler(food_start, commands='food', state='*')
    dp.register_message_handler(food_chosen, state=OrderFood.waiting_for_food_name)
    dp.register_message_handler(food_size_chosen, state=OrderFood.waiting_for_food_size)


async def cmd_start(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(
        f'Выберите блюда которые хотите заказать',
        reply_markup=types.ReplyKeyboardRemove()
    )


async def cmd_cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(
        f'Действие отменено',
        reply_markup=types.ReplyKeyboardRemove()
    )


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(cmd_cancel, commands='cancel', state="*")
    dp.register_message_handler(cmd_cancel, Text(equals='отмена', ignore_case=True), state=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
