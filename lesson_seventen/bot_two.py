import asyncio

from aiogram import types, Bot, Dispatcher
from aiogram.dispatcher import filters, FSMContext
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat, BotCommandScopeAllPrivateChats, \
    BotCommandScopeAllGroupChats, BotCommandScopeAllChatAdministrators

from consts import *
import logging

logging.basicConfig(level=logging.INFO)
bot = Bot(TOKEN)
dp = Dispatcher(bot)


#
# @dp.message_handler(hashtags='money')
# @dp.message_handler(cashtags=['eur', 'usd'])
# async def hashtag_example(msg: types.Message):
#     await msg.answer('Деньги')


# IMAGE_REGEXP = r'https://.+?\.(jpg|png|jpeg)'
# COMMAND_IMAGE_REGEXP = r"/image:" + IMAGE_REGEXP
#
#
# @dp.message_handler(filters.RegexpCommandsFilter([COMMAND_IMAGE_REGEXP]))
# @dp.message_handler(regexp_commands=[COMMAND_IMAGE_REGEXP])
# async def command_regexp_example(msg: types.Message):
#     await msg.answer('По вашей команде докладываю, что данная ссылка является изображением!')

# @dp.message_handler(commands='set_state')
# async def set_state(msg: types.Message, state: FSMContext):
#     """ПРисваиваем пользователю состояние для теста"""
#     await state.set_state("example_state")
#     await msg.answer('Состояние установлено')
#
#
# @dp.message_handler(commands='exit_state', state='example_state')
# async def state_example(msg: types.Message, state: FSMContext):
#     await msg.answer('Ты вышел из тестового статуса')
#     await state.finish()

# FORBIDDEN_PHRASE = (
#     'C++',
#     'Python'
# )
#
#
# @dp.message_handler(filters.Text(contains=FORBIDDEN_PHRASE))
# async def text_example(msg: types.Message):
#     await msg.reply('ОТВЕТ!!!!!!!!!!')
#
#
# async def main():
#     await dp.start_polling(bot)

# @dp.message_handler(filters.IDFilter(chat_id=ADMINS_ID))
# @dp.message_handler(chat_id=ADMINS_ID)
# async def id_filter_example(msg:types.Message):
#     await msg.answer('Привет админ')

# @dp.message_handler(commands='change_photo', is_chat_admin=True)
# @dp.message_handler(filters.Command('change_photo'), filters.AdminFilter())
# async def chat_admin_filter(msg: types.Message):
#     await msg.answer('Смена фото')


# @dp.message_handler(is_reply=True, commands='user_id')
# @dp.message_handler(filters.IsReplyFilter(True), commands='user_id')
# async def reply_example(msg: types.Message):
#     await msg.answer(msg.reply_to_message.from_user.id)


# @dp.message_handler(is_forwarded=True)
# @dp.message_handler(filters.ForwardedMessageFilter(True))
# async def forw_wxample(msg: types.Message):
#     await msg.answer('Не принимаю пересылку')


# @dp.message_handler(chat_type=types.ChatType.PRIVATE, commands='is_pm')
# @dp.message_handler(chat_type='private', commands='is_pm')
# @dp.message_handler(filters.ChatTypeFilter(types.ChatType.PRIVATE))
# async def chat_type_exmpl(msg: types.Message):
#     await msg.answer('Это личные сообщения')


async def set_default_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS = {
        'ru': [
            BotCommand('start', 'Начать заново'),
            BotCommand('get_commands', 'Получить список команд'),
            BotCommand('reset_commands', 'СБросить команды'),
        ],
        'en': [
            BotCommand('start', 'Reset bot'),
            BotCommand('get_commands', 'Retrieve commands list'),
            BotCommand('reset_commands', 'Reset commands'),
        ]
    }
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code
        )

    # return await bot.set_my_commands(
    #     commands=[
    #         BotCommand('cmd_dflt_1', 'Стандартная команда 1'),
    #         BotCommand('cmd_dflt_2', 'Стандартная команда 2'),
    #         BotCommand('cmd_dflt_3', 'Стандартная команда 3'),
    #     ],
    #     scope=BotCommandScopeDefault(),
    # )


@dp.message_handler(commands='start')
async def bot_start(message: types.Message):
    await message.reply('Hello')
    await set_default_commands(message.bot, message.from_user.id)


@dp.message_handler(commands='get_commands')
async def message_get_cmds(message: types.Message):
    no_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id))
    no_args = await message.bot.get_my_commands()
    ru_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id), language_code='ru')

    await message.reply('\n'.join(
        f'{arg}' for arg in (no_lang, no_args, ru_lang)
    ))


@dp.message_handler(commands='reset_commands')
async def user_start(message: types.Message):
    for language_code in ('ru', 'en', 'el'):
        for scope in (
            BotCommandScopeDefault(),
            BotCommandScopeAllPrivateChats(),
            BotCommandScopeAllGroupChats(),
            BotCommandScopeAllChatAdministrators(),
        ):
            await bot.delete_my_commands(scope, language_code)



@dp.message_handler(commands='cmd_dflt_3')
async def user_start(message: types.Message):
    await message.reply('Команда 3')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
