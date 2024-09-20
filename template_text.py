from datetime import date
# import locale
#
#
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

month_translate = {
    'Jan': 'Января',
    'Feb': 'Февраля',
    'Mar': 'Марта',
    'Apr': 'Апреля',
    'May': 'Мая',
    'Jun': 'Июня',
    'Jul': 'Июля',
    'Aug': 'Августа',
    'Sep': 'Сентября',
    'Oct': 'Октября',
    'Nov': 'Ноября',
    'Dec': 'Декабря',
}


date_month = month_translate.get(date.today().strftime('%b'))
date_day = date.today().strftime('%d')

header_message = (f'🇺🇸 Курсы на {date_day} {date_month.capitalize()}\nАктуальные курсы и оставить заявку: '
                  f'OBMENca.com или @OBMEN_cabot')
rub_to_usd = f'Отдаете RUB ➡️ USD/Zelle\nCash / Zelle'
usd_to_rub = f'Отдаете USD Cash / Zelle ➡️ RUB\nCash / Zelle'
footer_text = (f'Отдаете USDT ➡️ Получаете USD\n 10% от 100$\n 3,5% от 500$\n 2.5% от 1500$\n 2% от 5000$\n 1% от '
               f'10000$\n\nОтдаете USD ➡️ Получаете USDT\n 10% от 100$\n 5% от 500$\n 3.5% от 1500$\n 3% от 5000$\n '
               f'2.5% от 10000$\n\nОбменяем UAH, KZT, AMD, GEL, курс договорной.\n\n\n ✅Наши гарантии:\n Отзывы в '
               f'США\n Отзывы за 7 лет работы в России\n Личная встреча в офисе\n Счетная машинка\n\nℹ️Полезная '
               f'информация:\n Система скидок!\n Как происходит обмен?\n Как приготовиться к обмену?\n Как поменять '
               f'наличные между Россией и США?\n\n  Наши офисы:\nLos Angeles - Sherman Oaks\nNew York - '
               f'Brooklyn\nMiami - Sunny Isles\nOrange - County\nChicago - Des Plaines\n\n 💬Написать по обмену:\n '
               f'Los Angeles - OBMENCA\n\n☎️ Позвонить\n 888 702 4827\n\nTelegram\nОбменка Los Angeles\nВы можете '
               f'оставить ваш отзыв в комментариях этого поста')









