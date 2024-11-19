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

telegram_links = {
    'LOSANGELES': 'https://t.me/rfice220',
    'MIAMI': 'https://t.me/obmenca_miami',
    'NEWYORK': 'https://t.me/NY_obmenka',
    'CHICAGO': 'https://t.me/Chicago_obmenca',
    'ORANGE_COUNTY': 'https://t.me/obmenca_oc'
}

template_text = {
    'LOSANGELES': (f'📍 <a href="{telegram_links.get('LOSANGELES')}">Офис в Los Angeles - Sherman Oaks</a>'
                   f'\n🔥 Free Parking для клиентов\n\n☎️ Позвонить: 888 702 4827\n'),
    'MIAMI': f'📍 <a href="{telegram_links.get('MIAMI')}">Miami - Sunny Isles</a>',
    'NEWYORK': f'📍 <a href="{telegram_links.get('NEWYORK')}">New York - Brooklyn</a>\n',
    'CHICAGO': f'📍 <a href="{telegram_links.get('CHICAGO')}">Chicago - Des Plaines</a>\n',
    'ORANGE_COUNTY': f'📍 <a href="{telegram_links.get('ORANGE_COUNTY')}">Orange County</a>'
}


header_text = (
    f'\n\nОставить заявку на <a href="https://obmenca.com/">сайте</a> '
    f'или в нашем <a href="https://t.me/Obmen_cabot">боте</a>'
)

usdt_text = (f'<blockquote><b>Обмен USDT на $ (наличные):'
             f'\n• $10,000 -> 1.0%\n• $5,000 -> 2.0%'
             f'\n• $1,500 -> 2.5%\n• $500 -> 3.5%'
             f'\n• $100 -> 6.0%\n• Zelle +1%</b></blockquote>'
             f'\n<blockquote><b>Обмен $ (наличные) на USDT:'
             f'\n• $10,000 -> 2.5%\n• $5,000 -> 2.0%'
             f'\n• $1,500 -> 3.0%\n• $500 -> 3.5%'
             f'\n• $100 -> 6.0%\n• Zelle +1%</b></blockquote>'
             )

usdt_text_NY = (f'<blockquote><b>Обмен USDT на $ (наличные):'
                f'\n• $10,000 -> 1.0%\n• $5,000 -> 2.0%'
                f'\n• $1,500 -> 2.5%\n• $500 -> 3.5%'
                f'\n• $100 -> 6.0%\n• Zelle +1%</b></blockquote>'
                f'\n<blockquote><b>Обмен $ (наличные) на USDT:'
                f'\n• $10,000 -> 5%\n• $5,000 -> 5.5%'
                f'\n• $1,500 -> 6%\n• $500 -> 7.5%'
                f'\n• $100 -> 12.5%\n• Zelle +1%</b></blockquote>'
                )

footer_text = (f'Тяни вниз и увидишь все курсы ☝️'
               f'\n\n💸 Переводы наличных'
               f'\n• LA -> Москва (от $5000) | 3%'
               f'\n• Москва -> LA (от $5000) | 3%'
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
               f'\n<a href="https://t.me/creditshark">Улучшение кредитной истории</a>')
