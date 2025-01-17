import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value: str, expected_result: str) -> None:
    assert mask_account_card(value) == expected_result


def test_get_date(data_1: str, data_2: str, data_3: str, data_4: str, data_5: str) -> None:
    assert get_date(data_1) == "11.03.2024"
    assert get_date(data_2) == ""
    assert get_date(data_3) == "11.03.2024"
    assert get_date(data_4) == "11.03.2024"
    assert get_date(data_5) == "Неверный формат даты"
