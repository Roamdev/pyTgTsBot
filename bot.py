import os
from dotenv import load_dotenv
import telebot

from modules import get_rates

load_dotenv()


token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)
    print(message.text)


if __name__ == '__main__':
    bot.infinity_polling()

get_rates('usd', 'usdt', 'MSK', 1239)
get_rates('usd', 'usdt', 'LA', 3123)
get_rates('usd', 'usdt', 'TLT', 25)
get_rates('usd', 'usdt', 'NY', 123123)
