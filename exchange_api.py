import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_login = os.getenv('API_LOGIN')
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
query_headers = {'API-LOGIN': api_login, 'API-KEY': api_key}

currency_name_to_id_mapping = {
    "568": "CASHUSD",
    "355": "ETH",
    "537": "WIREUAH",
    "578": "ZELLE",
    "539": "WIREKZT",
    "369": "USDTBEP20",
    "367": "USDTERC20",
    "385": "TRX",
    "535": "WIRERUB",
    "581": "LYUBOYBANK",
    "371": "USDCERC20",
    "368": "USDTTRC20",
    "348": "BTC"
}


def get_direction(give_id, get_id):
    # send api request get_directions with params
    method_name = 'get_directions'
    endpoint = base_url + method_name
    response = requests.post(endpoint, headers=query_headers)
    directions = response.json().get('data')
    for direction in directions:
        if direction.get('currency_give_id') == str(give_id) and direction.get('currency_get_id') == str(get_id):
            return str(direction.get('direction_id'))


def get_direction_data(direction_id):
    # send api request get_direction with params
    method_name = 'get_direction'
    endpoint = base_url + method_name
    response = requests.post(endpoint, data={'direction_id': str(direction_id)}, headers=query_headers)
    direction_data = response.json().get('data')

    return direction_data


def get_calc(direction_id, amount, action, city):
    # send api request get_calc with params
    method_name = 'get_calc'
    endpoint = base_url + method_name
    response = requests.post(endpoint,
                             data={
                                 'direction_id': str(direction_id),
                                 'calc_amount': amount,
                                 'calc_action': action,
                                 'cd': f'city={city}'
                             },
                             headers=query_headers
                             )
    request_data = response.json().get('data', {})
    course_give = request_data.get('course_give')

    if course_give == '1':
        key = 'course_get'
    else:
        key = 'course_give'
    exchange_rate = request_data.get(key)

    return exchange_rate


def get_exchange_rate_for_currency_pair(give_id, get_id, city, amount, action):
    # get exchange rate
    give_id, get_id = str(give_id), str(get_id)
    direction_id = get_direction(give_id=str(give_id), get_id=str(get_id))

    if not direction_id:
        return None

    direction_data = get_direction_data(direction_id=direction_id)

    if not direction_data:
        return None

    exchange_rate = get_calc(direction_id, amount, action, city)

    return exchange_rate


def get_all_exchange_rate(give_id, get_id, city, action):
    # get all available procedures depending on the amount
    amount = {
        'USD': [100, 500, 1500, 5000, 10000],
        'RUB': [10000, 50000, 150000, 500000, 1000000]
    }
    if give_id == 535 or give_id == '535':
        amount = amount.get('RUB')
    else:
        amount = amount.get('USD')

    massive_rate = []
    for summ in amount:
        massive_rate += [get_exchange_rate_for_currency_pair(give_id, get_id, city, summ, action)]
    return massive_rate
