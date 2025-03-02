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
    'LOSAN': 'https://t.me/rfice220',
    'MIAMI': 'https://t.me/obmenca_miami',
    'NEWYORK': 'https://t.me/obmenka_newyork',
    'CHCG': 'https://t.me/Chicago_obmenca',
    'ORANGE_COUNTY': 'https://t.me/oc_obmenca',
    'obmenca_la_ca': 'https://t.me/obmen_la_ca/'
}

template_text = {
    'LOSAN': (f'📍 <a href="{telegram_links.get('LOSAN')}">Офис в Los Angeles - Sherman Oaks</a>'
              f'\n🔥 Free Parking для клиентов\n\n☎️ Позвонить: 888 702 4827\n'),
    'MIAMI': f'📍 <a href="{telegram_links.get('MIAMI')}">Miami - Sunny Isles</a>',
    'NEWYORK': f'📍 <a href="{telegram_links.get('NEWYORK')}">New York - Brooklyn</a>\n',
    'CHCG': f'📍 <a href="{telegram_links.get('CHCG')}">Chicago - Des Plaines</a>\n',
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
                f'\n• $10,000 -> 0%\n• $5,000 -> 1.0%'
                f'\n• $1,500 -> 1.5%\n• $500 -> 2.5%'
                f'\n• $100 -> 4.0%\n• Zelle +1%</b></blockquote>'
                f'\n<blockquote><b>Обмен $ (наличные) на USDT:'
                f'\n• $10,000 -> 5%\n• $5,000 -> 5.5%'
                f'\n• $1,500 -> 6%\n• $500 -> 7.0%'
                f'\n• $100 -> 7.5%\n• Zelle +1%</b></blockquote>'
                )

usdt_text_Chicago = (f'<blockquote><b>Обмен USDT на $ (наличные):'
                     f'\n• $10,000 -> 0%\n• $5,000 -> 1.0%'
                     f'\n• $1,500 -> 1.5%\n• $500 -> 3.5%'
                     f'\n• $100 -> 4.0%\n• Zelle +1%</b></blockquote>'
                     f'\n<blockquote><b>Обмен $ (наличные) на USDT:'
                     f'\n• $10,000 -> 4%\n• $5,000 -> 4.5%'
                     f'\n• $1,500 -> 5%\n• $500 -> 6.0%'
                     f'\n• $100 -> 6.5%\n• Zelle +1%</b></blockquote>'
                     )

commission_in_city = {
    'LOSAN': f'\n• LA -> Москва (от $5000) | 3%\n• Москва -> LA (от $5000) | 3%',
    'NEWYORK': f'\n• LA -> Москва (от $5000) | 3%\n• Москва -> LA (от $5000) | 3%',
    'CHCG': f'\n• Chicago -> Москва (от $5000) | 4%\n• Chicago -> LA (от $5000) | 1,5%',
    'ORANGE_COUNTY': f'\n• LA -> Москва (от $5000) | 3%\n• Москва -> LA (от $5000) | 3%'
}


footer_text = (f'\n\n<a href="{telegram_links.get('LOSAN')}">Также обменяем</a> 🇺🇦 UAH  '
               f'🇰🇿 KZT  🇦🇲 AMD  🇬🇪 GEL и другие валюты - курс договорной.'
               f'\n\n✅ Наши гарантии:'
               f'\n<a href="{telegram_links.get('obmenca_la_ca')}17">Отзывы в США</a>'
               f'\n<a href="https://searchengines.guru/ru/forum/899662">Отзывы за 10 лет работы в России</a>'
               f'\n\n➕ Личная встреча в офисе со счетной машинкой'
               f'\n🏦 Наши офисы:'
               f'\n<a href="{telegram_links.get('obmenca_la_ca')}">Los Angeles - Sherman Oaks</a>'
               f'\n<a href="{telegram_links.get('NEWYORK')}">New York - Brooklyn</a>'
               f'\n<a href="{telegram_links.get('MIAMI')}">Miami - Sunny Isles</a>'
               f'\n<a href="{telegram_links.get('ORANGE_COUNTY')}">Orange - County</a>'
               f'\n<a href="{telegram_links.get('CHCG')}">Chicago - Des Plaines</a>'
               f'\n\n⚡️ Полезная информация:'
               f'\n<a href="{telegram_links.get('obmenca_la_ca')}416">Система скидок!</a>'
               f'\n<a href="{telegram_links.get('obmenca_la_ca')}4">Как происходит обмен?</a>'
               f'\n<a href="{telegram_links.get('obmenca_la_ca')}6">Как приготовиться к обмену?</a>'
               f'\n<a href="{telegram_links.get('obmenca_la_ca')}7">Как поменять наличные между Россией и США?</a>'
               f'\n<a href="https://t.me/creditshark">Улучшение кредитной истории</a>'
               )
footer_text_miami = (
    f'\n💸 Переводы наличных'
    f'\n• Майами -> Москва (от $5000) | 4%'
    f'\n• Москва -> Майами (от $5000) | 4%'
    f'\n\nТакже обменяем и другие валюты - курс договорной.'
    f'\n\n✅ Наши гарантии:'
    f'\n<a href="https://t.me/obmen_la_ca/17">Отзывы в США</a>'
    f'\n<a href="https://searchengines.guru/ru/forum/899662">Отзывы за 10 лет работы в России</a>'
    f'\n\n⚡️ Полезная информация:'
    f'\n<a href="https://t.me/obmenca_miami/16">Как происходит обмен?</a>'
    f'\n<a href="https://t.me/obmenca_miami/26">Как приготовиться к обмену?</a>'
    f'\n<a href="https://t.me/obmenca_miami/24">Как поменять наличные между Россией и США?</a>'
    f'\n\n  🏦Наши офисы:'
    f'\n<a href="https://t.me/obmenca_miami">Miami - Sunny Isles</a>'
    f'\n<a href="https://t.me/obmen_la_ca">Los Angeles - Sherman Oaks</a>'
    f'\n<a href="https://t.me/obmenka_newyork">New York - Brooklyn</a>'
    f'\n<a href="https://t.me/oc_obmenca">Orange - County</a>'
    f'\n<a href="https://t.me/Chicago_obmenca">Chicago - Des Plaines</a>'
    f'\n\n<b><a href="https://t.me/miami_obmenca">✈️ Написать оператору</a></b>'
)
