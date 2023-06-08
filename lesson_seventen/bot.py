import asyncio
from consts import *
import logging
from aiogram import Bot, Dispatcher, types


logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет!\nНапиши мне что нибудь")


@dp.message_handler(commands=['help'])
async def proccess_help_command(message: types.Message):
    await message.reply("Напиши что либо, я верну это в ответ!")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

# @dp.message_handler(commands='block')
# async def cmd_block(message: types.Message):
#     await asyncio.sleep(10.0)
#     await message.reply('Вы заблокированы')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
