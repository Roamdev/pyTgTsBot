import os
from dotenv import load_dotenv
import telebot


load_dotenv()


token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)
    print(message.text)


if __name__ == '__main__':
    bot.infinity_polling()


class RateFetcher:
    def fetch_rate(self, buy_rate, sell_rate, location, amount):
        requested_rate = 99.99
        return requested_rate