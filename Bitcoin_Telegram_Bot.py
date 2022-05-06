# coinmarketcap API:
# https://coinmarketcap.com/api

# coinmarketcap API documentation:
# https://coinmarketcap.com/api/documentation/v1/


import requests
import time

# global variables
api_key = '4dcc976d-384c-438e-8919-966123b25f2b'
bot_key = '5157670585:AAHiepeKtMK2LXPMaY3DwRQRm8JPIDNsQh0'
chat_id = '1556529828'
limit = 100
time_interval = 5


def get_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '2',
        'convert': 'USD',

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }
    response = requests.get(url, headers=headers, params=parameters).json()
    data = response['data'][0]['quote']['USD']['price']
    return data


def send_message(id, message):
    url = f"https://api.telegram.org/bot{bot_key}/sendMessage?chat_id={id}&text={message}"

    requests.get(url)


def main():
    while True:
        price = int(get_price())
        print(price)
        if price < limit:
            send_message(chat_id, f"Price is lower than  {price}")
        time.sleep(time_interval)


main()
