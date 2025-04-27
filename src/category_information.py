from collections import Counter


def count_operation_by_category(transactions: list, list_category: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список
    категорий операций, и возвращает словарь с количеством операций в каждой категории."""

    category = []

    for transaction in transactions:
        if transaction.get("description") in list_category:
            category.append(transaction["description"])
    category_counter = dict(Counter(category))
    return category_counter
