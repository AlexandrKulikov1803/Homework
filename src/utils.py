import json
import logging
import os
from typing import Any

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transaction_data(path_json_str: str) -> Any:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях."""

    logger.info("Начался подсчёт суммы транзакции")

    try:
        if os.path.exists(path_json_str) and os.path.getsize(path_json_str) != 0:
            with open(path_json_str, encoding="utf-8") as file:
                transactions = json.load(file)
            logger.info("Подсчёт успешно завершён")
            return transactions
        else:
            logger.error("Подсчёт не может быть выполнен")
            return []
    except json.JSONDecodeError:
        logger.error("Подсчёт не может быть выполнен")
        return []
