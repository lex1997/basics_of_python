import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import sqlite3

from aiogram.utils import executor

TOKEN = '6265398487:AAF9v30HjApTxhvVQfYO8_0FtZUbTerkkZk'
BASE_URL = 'https://api.telegram.org/bot'
ADMINS_ID = [489153473, ]

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)


def create_table():
    conn = sqlite3.connect('user_db')
    cur = conn.cursor()
    cur.execute("""CREATE TABLE users(
            userid INT PRIMARY KEY,
            username TEXT,
            message TEXT);
        )
        """)
    conn.commit()
    cur.close()
    conn.close()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет!\nНапиши мне что нибудь")


@dp.message_handler(commands=['help'])
async def proccess_help_command(message: types.Message):
    await message.reply("Напиши что либо, я верну это в ответ!")


# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(text='БД')
async def echo(message: types.Message):
    conn = sqlite3.connect('user.db')
    cur = conn.cursor()
    user = cur.execute(f"""SELECT * FROM users WHERE userid = {message.chat.id}""").fetchone()
    if not user:
        data = (message.chat.id, message.chat.username)
        cur.execute("""INSERT INTO users(userid, username) VALUES (?,?)""", data)
        conn.commit()
        conn.close()
        await message.answer('Вы добавлены в БД')
    else:
        id, username = user[0]
        await message.answer(f'Вы уже есть в БД. Ваш id = {id}, username = {username}')


# @dp.message_handler(commands='block')
# async def cmd_block(message: types.Message):
#     await asyncio.sleep(10.0)
#     await message.reply('Вы заблокированы')


# async def main():
#     await dp.start_polling(bot)


if __name__ == '__main__':
    create_table()
    executor.start_polling(dp, skip_updates=True)
