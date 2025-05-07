import logging
import os
from typing import Any, Generator

path_file = "\\".join(os.getcwd().split("\\")[: os.getcwd().split("\\").index("Homework") + 1]) + "\\logs"
os.makedirs(path_file, exist_ok=True)

logger = logging.getLogger("generators")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{path_file}/generators.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_by_currency(list_transactions: list, currency: str) -> Any:
    """Функция, возвращающая итератор, который поочередно выдает транзакции по заданной валюте"""

    logger.info("Началась фильтрация транзакций по выбранной валюте")
    if list_transactions == []:
        return []
    elif list_transactions[0].get("operationAmount"):
        list_transactions = [x for x in list_transactions if x]
        filtered_transactions = [
            x for x in list_transactions if x.get("operationAmount")["currency"]["code"] == currency
        ]

    elif list_transactions[0].get("currency_code"):
        filtered_transactions = [x for x in list_transactions if x.get("currency_code") == currency]

    count = 0
    while count != len(filtered_transactions):
        yield filtered_transactions[count]
        count += 1
        logger.info("Транзакция выдана успешно")


def transaction_descriptions(list_transaction: list) -> Generator[dict, None, None]:
    """Функция, которая возвращает описание каждой операции по очереди"""

    logger.info("Началась сканирование транзакций")

    description = [x["description"] for x in list_transaction]
    count = 0
    while count != len(description):
        yield description[count]
        count += 1
        logger.info("Описание транзакции выдано успешно")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Функция, принимающая начальное и конечное значения для генерации диапазона номеров."""

    logger.info("Началась генерация диапазона номеров")

    if start <= 0 or end <= 0:
        logger.error("Невозможно сгенерировать диапазон номеров. Введено не верное значение")
        yield "Введено неверное значение"
    elif start < 10**16 and end < 10**16:
        count = start
        while count <= end:
            str_number = "0" * (16 - len(str(count))) + str(count)
            list_number = [str_number[x: x + 4] for x in range(0, len(str_number), 4)]
            number_of_card = " ".join(list_number)
            yield number_of_card
            count += 1
            logger.info("Сгенерированный номер выдан успешно")
    else:
        logger.error("Невозможно сгенерировать диапазон номеров. Превышено максимальное значение")
        yield "Превышено максимальное значение"
