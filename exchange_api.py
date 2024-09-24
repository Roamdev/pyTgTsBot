import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_login = os.getenv('API_LOGIN')
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
query_headers = {'API-LOGIN': api_login, 'API-KEY': api_key}

currency_id_to_name_mapping = {
    "CASHUSD": "568",
    "ETH": "355",
    "WIREUAH": "537",
    "ZELLE": "578",
    "WIREKZT": "539",
    "USDTBEP20": "369",
    "USDTERC20": "367",
    "TRX": "385",
    "WIRERUB": "535",
    "LYUBOYBANK": "581",
    "USDCERC20": "371",
    "USDTTRC20": "368",
    "BTC": "348"
}


def get_direction(give_id, get_id):
    # send api request get_directions with params

    give_id = str(currency_id_to_name_mapping.get(give_id, f'{give_id}'))
    get_id = str(currency_id_to_name_mapping.get(get_id, f'{get_id}'))
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


def get_chosen_city_name(city):
    # select city name from api
    method_name = 'get_direction'
    endpoint = base_url + method_name
    response = requests.post(endpoint, data={'direction_id': '1331'}, headers=query_headers)
    city_name = response.json().get("data", {}).get("dir_fields", {}).get("city", {}).get("options", {}).get(city, "0")
    return city_name


def get_exchange_rate_for_currency_pair(give_id, get_id, city, amount, action):
    # get exchange rate

    give_id = str(currency_id_to_name_mapping.get(give_id, f'{give_id}'))
    get_id = str(currency_id_to_name_mapping.get(get_id, f'{get_id}'))

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

    give_id = str(currency_id_to_name_mapping.get(give_id, f'{give_id}'))
    get_id = str(currency_id_to_name_mapping.get(get_id, f'{get_id}'))
    amounts_list = {
        'USD': [100, 500, 1500, 5000, 10000],
        'RUB': [10000, 50000, 150000, 500000, 1000000]
    }

    amounts = amounts_list.get('USD')
    if str(give_id) == '535':
        amounts = amounts_list.get('RUB')

    rate_arr = []
    for summ in amounts:
        rate_arr += [get_exchange_rate_for_currency_pair(give_id, get_id, city, summ, action)]
    return rate_arr
