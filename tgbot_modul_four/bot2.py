import logging
from random import randint

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.callback_data import CallbackData

from config import *
from keyboards import *

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# @dp.message_handler(commands=['inline_url'])
# async def process_cmd_inline_url(message: types.Message):
#     buttons = [
#         types.InlineKeyboardButton('Яндекс', url='https://www.yandex.ru'),
#         types.InlineKeyboardButton(text='оф.канал Телеграмма', url='tg://resolve?domain=telegram')
#     ]
#     keyboard = types.InlineKeyboardMarkup(row_width=1)
#     keyboard.add(*buttons)
#     await message.reply('Кнопки-ссылки', reply_markup=keyboard)


# @dp.message_handler(commands='random')
# async def cmd_random(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard.add(types.InlineKeyboardButton(text='Получить рандомное число от 1 до 10', callback_data='random_value'))
#     await message.answer('Случайная функция', reply_markup=keyboard)
#
#
# @dp.callback_query_handler(text='random_value')
# async def send_random_value(call: types.CallbackQuery):
#     await call.message.answer(str(randint(1, 10)))
#     await call.answer(text='спасибо что воспользовались нашим ботом', show_alert=True)


user_data = {}
callback_numbers = CallbackData('fabnum', 'action')


# button = types.InlineKeyboardButton('Лайк', callback_data=cb.new(id=5, action='like'))

# @dp.callback_query_handler(cb.filter())
# async def callbacks(call: types.CallbackQuery, callback_data: dict):
#     post_id = callback_data['id']
#     action = callback_data['action']


def get_keyboard():
    """Генерация клавиатуры"""
    buttons = [
        types.InlineKeyboardButton(text='-1', callback_data=callback_numbers.new(action='decr')),
        types.InlineKeyboardButton(text='+1', callback_data=callback_numbers.new(action='incr')),
        types.InlineKeyboardButton(text='Подтвердить', callback_data=callback_numbers.new(action='finish'))
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


async def update_num_text(message: types.Message, new_value: int):
    """Общая функция для обновления текста с отправкой той же клавиатурой"""
    await message.edit_text(f'Укажите число: {new_value}', reply_markup=get_keyboard())


@dp.message_handler(commands='numbers')
async def cmd_numbers(message: types.Message):
    user_data[message.from_user.id] = 0
    await message.answer('Укажите число: 0', reply_markup=get_keyboard())


@dp.callback_query_handler(callback_numbers.filter(action=['incr', 'decr']))
async def callbacks_num(call: types.CallbackQuery, callback_data: dict):
    user_value = user_data.get(call.from_user.id, 0)
    action = callback_data['action']

    if action == 'incr':
        user_data[call.from_user.id] = user_value + 1
        await update_num_text(call.message, user_value + 1)
    elif action == 'decr':
        user_data[call.from_user.id] = user_value - 1
        await update_num_text(call.message, user_value - 1)

    await call.answer()


@dp.callback_query_handler(callback_numbers.filter(action=['finish']))
async def callbacks_num_finish(call: types.CallbackQuery):
    user_value = user_data.get(call.from_user.id, 0)
    await call.message.edit_text(f'Итого: {user_value}')
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
