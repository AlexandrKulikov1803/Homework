import os

from src.utils import get_financial_transaction_data

directory = os.getcwd()
path_json_str = os.path.join(directory, "data", "operations.json")


def test_get_financial_transaction_data(list_of_transactions: list[dict]) -> None:
    assert get_financial_transaction_data(path_json_str) == list_of_transactions


def test_get_financial_transaction_data_non_existent_file() -> None:
    path_json_str = os.path.join(directory, "data", "non-existent_file.json")
    with open(path_json_str, "a", encoding="UTF-8"):
        assert get_financial_transaction_data(path_json_str) == []
    os.remove(path_json_str)


def test_get_financial_transaction_data_incorrect_content() -> None:
    path_json_str = os.path.join(directory, "data", "incorrect_content.json")
    with open(path_json_str, "a", encoding="UTF-8") as file:
        file.write("incorrect_content")
    assert get_financial_transaction_data(path_json_str) == []
    os.remove(path_json_str)
