from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

button_one = KeyboardButton('Привет!')
button_two = KeyboardButton('Отправить свой контакт', request_contact=True)
button_three = KeyboardButton('Отправить свою локацию', request_location=True)

kb = ReplyKeyboardMarkup()
kb.insert(button_one)
kb.insert(button_two)
kb.insert(button_three)

inline_btn_1 = InlineKeyboardButton('Первая кнопка', callback_data='button1')
inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Вторая кнопка', callback_data='button2'))
inline_btn_3 = InlineKeyboardButton('Третья кнопка', callback_data='button3')
inline_btn_4 = InlineKeyboardButton('Четвертая кнопка', callback_data='button4')
inline_btn_5 = InlineKeyboardButton('Пятая кнопка', callback_data='button5')
inline_kb_full.add(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.row(inline_btn_3, inline_btn_4, inline_btn_5)
inline_kb_full.insert(InlineKeyboardButton('query=" "', switch_inline_query=''))
inline_kb_full.insert(InlineKeyboardButton('query="qwerty"', switch_inline_query='qwerty'))
inline_kb_full.insert(InlineKeyboardButton('Inline в этом же чате', switch_inline_query_current_chat='wasd'))
inline_kb_full.insert(InlineKeyboardButton('Яндекс', url='https://www.yandex.ru'))




# kb_one = ReplyKeyboardMarkup().row(button_one, button_two, button_three)
