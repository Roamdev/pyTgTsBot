import os
from dotenv import load_dotenv
import telebot
import requests

# from modules import get_rates

load_dotenv()


token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)
api_login = os.getenv('API_LOGIN')
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
method_name = 'get_directions'
endpoint = base_url + method_name
query_headers = {'API-LOGIN': api_login, 'API-KEY': api_key}


@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)
    print(message.text)
    print(message.chat.id)

response = requests.post(endpoint, headers=query_headers)
data = response.json().get('data')


def get_give_id(filter_name, filter_item, data_list):
    filtered_give_id = [item for item in data_list if item[filter_item] == str(filter_name)]
    return filtered_give_id


result_get_id = get_give_id(568, 'currency_give_id', data)
print(result_get_id) #получаем все пары с использованием "Наличные" USD



if __name__ == '__main__':
    bot.infinity_polling()

