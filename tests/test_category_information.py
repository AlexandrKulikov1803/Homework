import pytest

from src.category_information import count_operation_by_category


@pytest.mark.parametrize(
    "expected_result",
    [
        (
            {
                "Перевод организации": 40,
                "Открытие вклада": 10,
                "Перевод со счета на счет": 15,
                "Перевод с карты на карту": 19,
                "Перевод с карты на счет": 16,
            }
        )
    ],
)
def test_count_operation_by_category(list_of_transactions: list, categories: list, expected_result: dict) -> None:
    assert count_operation_by_category(list_of_transactions, categories) == expected_result
    assert count_operation_by_category([], categories) == {}
