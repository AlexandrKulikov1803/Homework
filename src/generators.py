from typing import Generator


def filter_by_currency(list_transactions: list, currency: str) -> Generator[dict, None, None]:
    """Функция, возвращающая итератор, который поочередно выдает транзакции по заданной валюте"""

    filtered_transactions = [x for x in list_transactions if x["operationAmount"]["currency"]["code"] == currency]
    count = 0
    while count != len(filtered_transactions):
        yield filtered_transactions[count]
        count += 1


def transaction_descriptions(list_transaction: list) -> Generator[dict, None, None]:
    """Функция, которая возвращает описание каждой операции по очереди"""

    description = [x["description"] for x in list_transaction]
    count = 0
    while count != len(description):
        yield description[count]
        count += 1


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Функция, принимающая начальное и конечное значения для генерации диапазона номеров."""
    if start <= 0 or end <= 0:
        yield "Введено неверное значение"
    elif start < 10**16 and end < 10**16:
        count = start
        while count <= end:
            str_number = "0" * (16 - len(str(count))) + str(count)
            list_number = [str_number[x: x + 4] for x in range(0, len(str_number), 4)]
            number_of_card = " ".join(list_number)
            yield number_of_card
            count += 1
    else:
        yield "Превышено максимальное значение"
