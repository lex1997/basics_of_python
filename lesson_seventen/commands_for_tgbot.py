import os
import requests
import datetime
from consts import *
from aiogram import Bot, Dispatcher, types, executor

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start_command(msg: types.Message):
    await msg.answer('Привет я сообщаю погоду в городе, просто введи название города')

@dp.message_handler()
async def get_weather(msg: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Ясно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }
    # try:
    r = requests.get(f"https://{WEATHER_API}/data/2.5/weather?q={msg.text}&appid={WEATHER_API_Key}&units=metric")
    data = r.json()
    print(data)
    city = data['name']
    cur_weather = data['main']['temp']
    weather_description = data['weather'][0]['main']
    if weather_description in code_to_smile:
        wd = code_to_smile[weather_description]
    else:
        wd = 'Глянь в окно сам'
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
    sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
    length_of_the_day = sunset_timestamp - sunrise_timestamp
    wind = data['wind']['speed']
    await msg.answer(f'***{datetime.datetime.now().strftime("%d.%m.%Y %H:%M")}***\n'
                     f'Погода в городе: {city}\nТемпература: {cur_weather}С {wd}\n'
                     f'Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} М/с\n'
                     f'Продолжительность дня: {length_of_the_day}')
    # except Exception as e:
    #     print(e)
    #     await msg.reply('ПРоверь название города')

if __name__ == '__main__':
    executor.start_polling(dp)

