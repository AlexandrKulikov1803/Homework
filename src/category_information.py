import logging
import os
from collections import Counter

path_file = "\\".join(os.getcwd().split("\\")[: os.getcwd().split("\\").index("Homework") + 1]) + "\\logs"
os.makedirs(path_file, exist_ok=True)

logger = logging.getLogger("category_information")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{path_file}/category_information.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def count_operation_by_category(transactions: list, list_category: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список
    категорий операций, и возвращает словарь с количеством операций в каждой категории."""

    category = []

    logger.info("Началась фильтрация транзакций по категориям")

    for transaction in transactions:
        if transaction.get("description") in list_category:
            category.append(transaction["description"])
    category_counter = dict(Counter(category))

    logger.info("Фильтрация успешно завершена")

    return category_counter
