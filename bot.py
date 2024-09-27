import os
import telebot
from dotenv import load_dotenv

from exchange_api import get_all_exchange_rate as exchange_rate
from exchange_api import get_chosen_city_name as chosen_city_name
from template_text import header_message, rub_to_usd, usd_to_rub, footer_text
from currencies import Currencies

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)
commands = [
    "rate_LOSANGELES",
    "rate_MIAMI",
    "rate_NEWYORK",
    "rate_CHICAGO"
]


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'\n/{commands[0]}\n'
                                      f'\n/{commands[1]}\n'
                                      f'\n/{commands[2]}\n'
                                      f'\n/{commands[3]}\n'
                     )


@bot.message_handler(commands=commands)
def send_rate(message):
    bot.send_message(message.chat.id, 'Обработка запроса 🌚')
    city = message.text[6:]
    rub_to_cash = exchange_rate(Currencies.WIRERUB.value, Currencies.CASHUSD.value, city)
    rub_to_zelle = exchange_rate(Currencies.WIRERUB.value, Currencies.ZELLE.value, city)
    cash_usd_to_rub = exchange_rate(Currencies.CASHUSD.value, Currencies.WIRERUB.value, city)
    zelle_to_rub = exchange_rate(Currencies.ZELLE.value, Currencies.WIRERUB.value, city)
    if rub_to_cash and rub_to_zelle and cash_usd_to_rub and zelle_to_rub:
        bot.send_message(message.chat.id, f'{header_message}\n\n'
                                          f'Курс для города {chosen_city_name(city)}:'
                                          f'\n\n{rub_to_usd}:\n'
                                          f'\n{rub_to_cash[0]} / {rub_to_zelle[0]} от 10000₽'
                                          f'\n{rub_to_cash[1]} / {rub_to_zelle[1]} от 50000₽'
                                          f'\n{rub_to_cash[2]} / {rub_to_zelle[2]} от 150.000₽'
                                          f'\n{rub_to_cash[3]} / {rub_to_zelle[3]} от 500.000₽'
                                          f'\n{rub_to_cash[4]} / {rub_to_zelle[4]} от 1 млн ₽'
                                          f'\n\n{usd_to_rub}\n'
                                          f'\n{cash_usd_to_rub[0]} / {zelle_to_rub[0]} от 100$'
                                          f'\n{cash_usd_to_rub[1]} / {zelle_to_rub[1]} от 500$'
                                          f'\n{cash_usd_to_rub[2]} / {zelle_to_rub[2]} от 1500$'
                                          f'\n{cash_usd_to_rub[3]} / {zelle_to_rub[3]} от 5000$'
                                          f'\n{cash_usd_to_rub[4]} / {zelle_to_rub[4]} от 10000$'
                                          f'\n\n{footer_text}'
                         )
    else:
        bot.send_message(message.chat.id, 'sorry is None')


@bot.message_handler(content_types=['text'])
def missing_message(message):
    bot.send_message(message.chat.id, 'давай начнем с команды /help')


if __name__ == '__main__':
    bot.infinity_polling()
