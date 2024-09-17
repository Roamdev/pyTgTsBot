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
        if direction.get('currency_give_id') == give_id and direction.get('currency_get_id') == get_id:
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
                                 'cd': city
                                 },
                             headers=query_headers
                             )
    exchange_rate = response.json().get('data', {}).get('course_get')
    return exchange_rate


def get_exchange_rate_for_currency_pair(give_id, get_id, city, amount, action):
    # get exchange rate
    direction_id = get_direction(give_id=give_id, get_id=get_id)
    if not direction_id:
        return None
    direction_data = get_direction_data(direction_id=direction_id)
    get_city = direction_data.get("dir_fields", {}).get("city", {}).get("options", {}).get(city, 'Не выбрано')
    exchange_rate = get_calc(direction_id, amount, action, city)

    if not direction_data:
        return None

    return (currency_name_to_id_mapping.get(get_id),
            currency_name_to_id_mapping.get(give_id),
            get_city,
            amount,
            exchange_rate
            )
