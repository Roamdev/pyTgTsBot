from datetime import date


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
amounts_list = {
    'USD': [10000, 5000, 1500, 500, 100],
    'RUB': [1000000, 500000, 150000, 50000, 10000]
}
templates = {
    'LOSANGELES': ('📍 <a href="https://t.me/rfice220">Офис в Los Angeles - Sherman Oaks</a>'
                   '\n🔥 Free Parking для клиентов\n'
                   '\n☎️ Позвонить: 888 702 4827\n'),
    'MIAMI': '📍 <a href="https://t.me/obmenca_miami">Miami - Sunny Isles</a>',
    'NEWYORK': '📍 <a href="https://t.me/NY_obmenka">New York - Brooklyn</a>\n',
    'CHICAGO': '📍 <a href="https://t.me/Chicago_obmenca">Chicago - Des Plaines</a>\n',
    'ORANGE_COUNTY': '📍 <a href="https://t.me/oc_obmenca">Orange County</a>'
}

date_month = month_translate.get(date.today().strftime('%b'))
date_day = date.today().strftime('%d')

links_text = ''

header_text = (
    f'\n✈️ Написать по обмену <a href="https://t.me/NY_obmenka">Zelle online</a>\n'
    f'\nОставить заявку на <a href="https://obmenca.com/">сайте</a> '
    f'или в нашем <a href="https://t.me/Obmen_cabot">боте</a>\n'
    f'\n<b>Курсы на {date_day} {date_month.capitalize()}</b>\n'
    )

usdt_text = (f'<blockquote><b>Обмен USDT на $ (наличные):\n• $10,000 -> 1.0%\n• $5,000 -> 2.0%\n'
             f'• $1,500 -> 2.5%\n• $500 -> 3.5%\n• $100 -> 6.0%\n• Zelle +1%</b></blockquote>'
             f'\n<blockquote><b>Обмен $ (наличные) на USDT:\n• $10,000 -> 2.5%\n• $5,000 -> 2.0%'
             f'\n• $1,500 -> 3.0%\n• $500 -> 3.5%\n• $100 -> 6.0%\n• Zelle +1%</b></blockquote>')

footer_text = (f'Тяни вниз и увидишь все курсы ☝️'
               f'\n\n💸 Переводы наличных'
               f'\n• LA -> Москва (от $5000) | 3%'
               f'\n• Москва -> LA (от $5000) | 3%'
               f'\n\n💱 Обмен валют:'
               f'\n• LA -> Москва (от $5,000) -> 90.60₽'
               f'\n• Москва -> LA (от 500,000₽) -> $95.30'
               f'\n\n<a href="https://t.me/rfice220">Также обменяем</a> 🇺🇦 UAH  '
               f'🇰🇿 KZT  🇦🇲 AMD  🇬🇪 GEL и другие валюты - курс договорной.'
               f'\n\n✅ Наши гарантии:'
               f'\n<a href="https://t.me/obmen_la_ca/17">Отзывы в США</a>'
               f'\n<a href="https://searchengines.guru/ru/forum/899662">Отзывы за 10 лет работы в России</a>'
               f'\n\n➕ Личная встреча в офисе со счетной машинкой'
               f'\n\n⚡️ Полезная информация:'
               f'\n<a href="https://t.me/obmen_la_ca/416">Система скидок!</a>'
               f'\n<a href="https://t.me/obmen_la_ca/4">Как происходит обмен?</a>'
               f'\n<a href="https://t.me/obmen_la_ca/6">Как приготовиться к обмену?</a>'
               f'\n<a href="https://t.me/obmen_la_ca/7">Как поменять наличные между Россией и США?</a>'
               f'\n<a href="https://t.me/creditshark">Улучшение кредитной истории</a>'
               f'\n\n✈️ <a href="https://t.me/miami_obmenca">Написать оператору</a>'
               f'\n\n!Вы можете оставить ваш отзыв в комментариях этого поста!')
