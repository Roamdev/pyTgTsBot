import os
import requests
from dotenv import load_dotenv


load_dotenv()

api_login = os.getenv('API_LOGIN')
api_key = os.getenv('API_KEY')
base_url = os.getenv('BASE_URL')
query_headers = {'API-LOGIN': api_login, 'API-KEY': api_key}


def get_direction(currency_in, currency_out):
    # send api request get_directions with params

    method_name = 'get_directions'
    endpoint = base_url + method_name
    response = requests.post(endpoint, headers=query_headers)
    directions = response.json().get('data')
    for direction in directions:
        
        if (direction.get('currency_get_id') == currency_in
                and direction.get('currency_give_id') == currency_out):
            return direction.get('direction_id')


def get_calc(direction_id, amount, city, action=1):
    # send api request get_calc with params

    method_name = 'get_calc'
    endpoint = base_url + method_name
    data = {
        'direction_id': str(direction_id),
        'calc_amount': amount,
        'calc_action': action,
        'cd': f'city={city}'
        }
    response = requests.post(
        endpoint,
        data=data,
        headers=query_headers
    )
    request_data = response.json().get('data', {})
    course_give = request_data.get('course_give')
    course_get = request_data.get('course_get')

    if course_give > course_get:
        key = 'course_give'
    else:
        key = 'course_get'
    exchange_rate = request_data.get(key)

    return exchange_rate


def get_chosen_city_name(city):
    # select city name from api
    method_name = 'get_direction'
    endpoint = base_url + method_name
    example_direction_id = '1331'
    data = {'direction_id': example_direction_id}
    response = requests.post(endpoint, data=data, headers=query_headers)
    city = (
        response.json().get("data", {}).get("dir_fields", {}).get("city", {}).get("options", {}).get(city, "Не выбран")
    )

    return city


def get_exchange_rate_for_currency_pair(currency_in, currency_out, city, amount, action=1):
    # get exchange rate

    direction_id = get_direction(currency_in=currency_in, currency_out=currency_out)

    if not direction_id:
        return None

    exchange_rate = get_calc(direction_id, amount, city, action)

    return exchange_rate


def get_all_exchange_rate(currency_in, currency_out, city):
    # get all available procedures depending on the amount

    rub_id = '535'
    amounts_list = {
        'USD': [100, 500, 1500, 5000, 10000],
        'RUB': [10000, 50000, 150000, 500000, 1000000]
    }

    amounts = amounts_list.get('USD')
    if currency_out == rub_id:
        amounts = amounts_list.get('RUB')

    rate_arr = []
    for summ in amounts:
        exchange_rate = get_exchange_rate_for_currency_pair(currency_in, currency_out, city, summ, action=1)
        if exchange_rate is None:
            return None
        rate_arr += [exchange_rate]
    return rate_arr
