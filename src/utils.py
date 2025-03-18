import json
import os
from typing import Any


def get_financial_transaction_data(path_json_str: str) -> Any:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях."""
    try:
        if os.path.exists(path_json_str) and os.path.getsize(path_json_str) != 0:
            with open(path_json_str, encoding="utf-8") as file:
                transactions = json.load(file)
            return transactions
        else:
            return []
    except json.JSONDecodeError:
        return []
