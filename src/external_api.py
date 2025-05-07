import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

path_file = "\\".join(os.getcwd().split("\\")[: os.getcwd().split("\\").index("Homework") + 1]) + "\\logs"
os.makedirs(path_file, exist_ok=True)

logger = logging.getLogger("external_api")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{path_file}/external_api.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def currency_conversion(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях."""

    logger.info("Началась конвертация валюты в рубли")

    code = transaction["operationAmount"]["currency"]["code"]
    amount = float(transaction["operationAmount"]["amount"])
    if code != "RUB":
        headers = {"apikey": api_key}
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        conversion_to_RUB = requests.get(url, headers=headers)
        print(conversion_to_RUB.status_code)
        amount = conversion_to_RUB.json()["result"]

    logger.info("Конвертация успешно завершена")
    return amount
