from keys import keys
import requests
import json

class ConretionException(Exception):
    pass
class CryptConveret:
    @staticmethod
    def convert(quot: str, base: str, amount: str):
        if quot == base:
            raise ConretionException('Одинаковые величины')
        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConretionException('Неудалось обработать валюту')
        try:
            quot_tiker = keys[quot]
        except KeyError:
            raise ConretionException('Неудалось обработать валюту')

        try:
            amount == float(amount)

        except ValueError:
            raise ConretionException(f'Не удалось обработать количество валюты {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quot_tiker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[keys[base]]
        return total_base