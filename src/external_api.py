import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")


def currency_conversion(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях."""

    code = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])
    if code != "RUB":
        headers = {"apikey": api_key}
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        conversion_to_RUB = requests.get(url, headers=headers)
        print(conversion_to_RUB.status_code)
        amount = conversion_to_RUB.json()["result"]
    return amount
