import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from config import *
from keyboards import *

bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет!', reply_markup=kb)


@dp.message_handler(commands=['inline'])
async def process_start_command(message: types.Message):
    await message.reply('Новая клава', reply_markup=inline_kb_full)


@dp.callback_query_handler()
async def process_callback_command(callback_query: types.CallbackQuery):
    code = callback_query.data[-1]
    if code.isdigit():
        code = int(code)
    if code == 2:
        await bot.answer_callback_query(callback_query.id, text='нажата вторая кнопка')
    elif code == 5:
        await bot.answer_callback_query(callback_query.id, text='нажата кнопка под номером 5.\n А этот текст может быть длинной до 200 символов', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f'Нажата кнопка с кодом:{code}')
    # await bot.answer_callback_query(callback_query.id)
    # await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка')


@dp.message_handler(commands=['rm'])
async def process_rm_command(message: types.Message):
    await message.reply('Убираем клавиатуру', reply_markup=ReplyKeyboardRemove())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
