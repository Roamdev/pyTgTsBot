import os
import telebot
from dotenv import load_dotenv

from exchange_api import get_exchange_rate_for_currency_pair

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)
    print(message.text)
    print(message.chat.id)


result = get_exchange_rate_for_currency_pair('368', '568', "CHICAGO", 1000, 1)

print(result)

if result == None:
    result = 'something went wrong'


if __name__ == '__main__':
    bot.infinity_polling()

