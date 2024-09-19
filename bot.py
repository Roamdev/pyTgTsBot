import os
import telebot
from dotenv import load_dotenv


from exchange_api import get_exchange_rate_for_currency_pair as exchange_rate
from template_text import template_text


token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


# @bot.message_handler(content_types=["text"])
# def repeat_all_message(message):
#     # bot.send_message(message.chat.id, message.text)
#     bot.send_message(message.chat.id, result)


result_rub_to_usd = exchange_rate('535', '578', "CHICAGO", 1000, 1)
result_usd_to_rub = exchange_rate('578', '535', "CHICAGO", 1000, 1)

print(f'rub to usd = {result_rub_to_usd} \nusd to rub = {result_usd_to_rub}')




# if __name__ == '__main__':
#     bot.infinity_polling()
