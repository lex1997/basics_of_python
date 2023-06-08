import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from config import *

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(text='Привет')
async def cmd_test1(message: types.Message):
    await message.answer(message.text)
    await message.answer(message.md_text)
    await message.answer(fmt.text('Привет,', fmt.hbold(message.text)), parse_mode=types.ParseMode.HTML)
    await message.answer(
        f"<u>Ваш текст</u>:\n\n{message.html_text}", parse_mode='HTML'
    )

#
# @dp.message_handler(content_types=["photo"])
# async def download_photo(message: types.Message):
#     await message.photo[-1].download(destination='photos')


@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def echo_document(message: types.Message):
    await message.reply_animation(message.animation.file_id)


@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def download_doc(message: types.Message):
    await message.document.download()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
