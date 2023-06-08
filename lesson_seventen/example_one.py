import requests
from consts import *

def pulling():
    count_message = 0
    while True:
        response = requests.get(f'{BASE_URL}{TOKEN}/getUpdates').json()
        print(response)
        if count_message != len(response['result']):
            count_message = len(response['result'])
            message = response['result'][-1]
            user_id = message['message']['from']['id']
            chat_id = message['message']['chat']['id']
            requests.get(f'{BASE_URL}{TOKEN}/', json={'method': 'unbanChatMember', 'chat_id': chat_id, 'user_id': user_id})

pulling()