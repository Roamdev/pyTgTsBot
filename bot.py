import os
from telebot import telebot
from dotenv import load_dotenv
from datetime import date

from exchange_api import get_all_exchange_rate as exchange_rate
from exchange_api import get_chosen_city_name as chosen_city_name
from template_text import (amounts_list, header_text,
                           usdt_text, usdt_text_NY, usdt_text_Chicago, footer_text, footer_text_miami, template_text,
                           telegram_links, month_translate)
from currencies import Currencies

load_dotenv()
token = os.getenv('TOKEN')
bot = telebot.TeleBot(token)
commands = [
    "rate_LOSAN",
    "rate_MIAMI",
    "rate_NEWYORK",
    "rate_CHCG",
    "rate_ORANGE_COUNTY"
]
commands_text = '\n\n'.join([f'/{command}' for command in commands])


def rendering_rates(amounts, currency_sing_in, rates, currency_sing_out):
    # drawing a pair of currency + amount
    value = ''
    
    for i in range(len(amounts)):
        value += f'\n• {amounts[i]}{currency_sing_in} -> {rates[i]}{currency_sing_out}'
    
    return value


@bot.message_handler(commands=['help', 'start'])
def welcome(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_la = telebot.types.KeyboardButton(text="/rate_LOSAN")
    button_miami = telebot.types.KeyboardButton(text="/rate_MIAMI")
    button_ny = telebot.types.KeyboardButton(text="/rate_NEWYORK")
    button_chicago = telebot.types.KeyboardButton(text="/rate_CHCG")
    button_orange_county = telebot.types.KeyboardButton(text="/rate_ORANGE_COUNTY")
    keyboard.add(button_la, button_miami, button_ny)
    keyboard.add(button_chicago, button_orange_county)
    bot.send_message(chat_id, 'Выбери город', reply_markup=keyboard)


@bot.message_handler(commands=commands)
def send_rate(message):
    bot.send_message(message.chat.id, 'Обработка запроса 🌚')
    city = message.text[6:]
    date_month = month_translate.get(date.today().strftime('%b'))
    date_day = date.today().strftime('%d')
    
    # "if statement" is needed here because the API does not have this city, I had to improvise
    
    if city == "ORANGE_COUNTY":
        city_name = 'Orange County'
        city = 'LOSAN'
    else:
        city_name = chosen_city_name(city)

    end_text = (f'\n\n✈️ <a href="{telegram_links.get(city)}">Написать оператору</a>'
                f'\n\n!Вы можете оставить ваш отзыв в комментариях этого поста!')
    rub_sign = '₽'
    usd_sign = '$'
    rub_amounts = amounts_list.get('RUB')
    usd_amounts = amounts_list.get('USD')
    rub_to_cash_rates = exchange_rate(Currencies.CASHUSD.value, Currencies.WIRERUB.value, city)
    rub_to_zelle_rates = exchange_rate(Currencies.ZELLE.value, Currencies.WIRERUB.value, city)
    cash_usd_to_rub_rates = exchange_rate(Currencies.WIRERUB.value, Currencies.CASHUSD.value, city)
    zelle_to_rub_rates = exchange_rate(Currencies.WIRERUB.value, Currencies.ZELLE.value, city)
    
    # "if statement" is needed here because the API does not have this city, I had to improvise
    
    if city_name == "Orange County":
        city = "ORANGE_COUNTY"

    if city == 'NEWYORK':
        usdt_text_for_city = usdt_text_NY
    elif city == 'CHCG':
        usdt_text_for_city = usdt_text_Chicago
    else:
        usdt_text_for_city = usdt_text

    if city == 'MIAMI':
        finish_text = footer_text_miami
    else:
        finish_text = footer_text + end_text

    if rub_to_cash_rates and rub_to_zelle_rates and cash_usd_to_rub_rates and zelle_to_rub_rates:
        bot.send_message(
            message.chat.id,
            
            f'<b>Обмен валют в {city_name}:</b>\n\n'
            f'{template_text.get(city)}'
            f'\n✈️ Написать по обмену <a href="{telegram_links.get(city)}">Zelle online</a>'
            f'{header_text}'
            f'\n\n<b>Курсы на {date_day} {date_month.capitalize()}</b>\n'
            f'<blockquote><b>'
            f'Курсы обмена ₽ на $(наличные):'
            f'{rendering_rates(rub_amounts, rub_sign, rub_to_cash_rates, usd_sign)}'
            f'</b></blockquote>\n'
            f'<blockquote><b>'
            f'Курсы обмена $(наличные) на ₽:'
            f'{rendering_rates(usd_amounts, usd_sign, cash_usd_to_rub_rates, rub_sign)}'
            f'</b></blockquote>\n'
            f'{usdt_text_for_city}'
            f'<blockquote expandable><b>'
            f'Курсы обмена ₽ на $ (Zelle):'
            f'{rendering_rates(rub_amounts, rub_sign, rub_to_zelle_rates, usd_sign)}'
            f'</b></blockquote>\n'
            f'<blockquote expandable><b>'
            f'Курсы обмена $ (Zelle) на ₽:'
            f'{rendering_rates(usd_amounts, usd_sign, zelle_to_rub_rates, rub_sign)}'
            f'</b></blockquote>\n'
            f'{finish_text}',
            parse_mode='HTML'
        )
    else:
        bot.send_message(message.chat.id, 'sorry is None')


@bot.message_handler(content_types=['text'])
def missing_message(message):
    bot.send_message(message.chat.id, 'давай начнем с команды /help')


if __name__ == '__main__':
    bot.infinity_polling()
