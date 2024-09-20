import os
import telebot
from dotenv import load_dotenv


from exchange_api import get_all_exchange_rate as exchange_rate
from template_text import *

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def send_rate(message):
    rub_to_cash = exchange_rate('535', '568', "CHICAGO", 1)
    rub_to_zelle = exchange_rate('535', '578', "CHICAGO", 1)
    cash_usd_to_rub = exchange_rate('568', '535', "CHICAGO", 1)
    zelle_to_rub = exchange_rate('578', '535', "CHICAGO", 1)
    bot.send_message(message.chat.id, f'{header_message}\n\n{rub_to_usd}:\n'
                                      f'\n{rub_to_cash[0]} / {rub_to_zelle[0]} от 10000₽'
                                      f'\n{rub_to_cash[1]} / {rub_to_zelle[1]} от 50000₽'
                                      f'\n{rub_to_cash[2]} / {rub_to_zelle[2]} от 150.000₽'
                                      f'\n{rub_to_cash[3]} / {rub_to_zelle[3]} от 500.000₽'
                                      f'\n{rub_to_cash[4]} / {rub_to_zelle[4]} от 1 млн ₽'
                                      f'\n\n{usd_to_rub}'
                                      f'\n{cash_usd_to_rub[0]} / {zelle_to_rub[0]} от 100$'
                                      f'\n{cash_usd_to_rub[1]} / {zelle_to_rub[1]} от 500$'
                                      f'\n{cash_usd_to_rub[2]} / {zelle_to_rub[2]} от 1500$'
                                      f'\n{cash_usd_to_rub[3]} / {zelle_to_rub[3]} от 5000$'
                                      f'\n{cash_usd_to_rub[4]} / {zelle_to_rub[4]} от 10000$'
                                      f'\n\n{footer_text}'
                     )


if __name__ == '__main__':
    bot.infinity_polling()
