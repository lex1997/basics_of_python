import  logging
import sqlite3

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Update

from consts import *
from db_config import Database

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
db = Database()

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    non_existing_user = 11111
    try:
        await message.answer("Неправильно закрыт <b>тег<b>")
    except Exception as err:
        await message.answer(f"Не попало в error handler. Ошибка {err}")

    try:
        await bot.send_message(chat_id=non_existing_user, text='Несуществующий пользователь')
    except Exception as err:
        await message.answer(f"Не попало в error handler. Ошибка {err}")

    await message.answer('Не существует <fff>тега</fff>')
    logging.info('Это не выполнится но бот упадет')

    await message.answer('hello')

    # name = message.from_user.full_name
    # try:
    #     db.add_user(id=message.from_user.id, name=name)
    # except sqlite3.IntegrityError as err:
    #     print(err)
    # print(db.count_users()[0])
    # count_users = db.count_users()[0]
    # await message.answer(
    #     '\n'.join([
    #         f"Привет, {message.from_user.full_name}!",
    #         'Ты был занесен в базу данных',
    #         f'В базе данных {count_users} пользователей'
    #     ])
    # )

@dp.errors_handlers()
async def errors_handler(update, exception):
    """
    Хендлер для обработки исключений
    :param update:
    :param exception:
    :return: stdout logging
    """
    from aiogram.utils.exceptions import (
        Unauthorized,
        InvalidQueryID,
        TelegramAPIError,
        CantDemoteChatCreator,
        MessageNotModified,
        MessageToDeleteNotFound,
        MessageTextIsEmpty,
        RetryAfter,
        CantParseEntities,
        MessageCantBeDeleted,
        BadRequest
    )

    if isinstance(exception, Unauthorized):
        logging.debug('Unauthorized')
        return True

    if isinstance(exception, InvalidQueryID):
        logging.debug('InvalidQueryID')
        return True

    if isinstance(exception, TelegramAPIError):
        logging.debug('TelegramAPIError')
        return True

    if isinstance(exception, CantDemoteChatCreator):
        logging.debug('CantDemoteChatCreator')
        return True

    if isinstance(exception, MessageNotModified):
        logging.debug('MessageNotModified')
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logging.debug('MessageToDeleteNotFound')
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logging.debug('MessageTextIsEmpty')
        return True

    if isinstance(exception, RetryAfter):
        logging.debug('RetryAfter')
        return True

    if isinstance(exception, CantParseEntities):
        await Update.get_current().message.answer(f'Попало в эррор хендлер CantParseEntities')
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logging.debug('MessageCantBeDeleted')
        return True

    if isinstance(exception, BadRequest):
        logging.debug('BadRequest')
        return True

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)