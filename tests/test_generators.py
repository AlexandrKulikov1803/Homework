import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "expected_result",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
            [],
            [
                {
                    "id": 4234093,
                    "state": "EXECUTED",
                    "date": "2021-07-08T07:31:21Z",
                    "amount": 23182.0,
                    "currency_name": "Ruble",
                    "currency_code": "RUB",
                    "from": "Visa 0773092093872450",
                    "to": "Discover 8602781449570491",
                    "description": "Перевод с карты на карту",
                }
            ],
        ),
    ],
)
def test_filter_by_currency(transactions_1: list, transactions_2: list, expected_result: list) -> None:
    assert list(filter_by_currency(transactions_1, "RUB")) in expected_result
    assert list(filter_by_currency(transactions_1, "USD")) in expected_result
    assert list(filter_by_currency(transactions_1, "EUR")) in expected_result
    assert list(filter_by_currency(transactions_2, "RUB")) in expected_result
    assert list(filter_by_currency([], "RUB")) == []


def test_transaction_descriptions(transactions_1: list, descriptions: list) -> None:
    assert list(transaction_descriptions(transactions_1)) == descriptions


@pytest.mark.parametrize(
    "expected_result",
    [
        (
            [
                "0000 0000 0000 0015",
                "0000 0000 0000 0016",
                "0000 0000 0000 0017",
                "0000 0000 0000 0018",
                "0000 0000 0000 0019",
            ],
            ["Введено неверное значение"],
            ["Превышено максимальное значение"],
            [],
        ),
    ],
)
def test_card_number_generator(expected_result: list) -> None:
    assert list(card_number_generator(15, 19)) in expected_result
    assert list(card_number_generator(-5, 15)) in expected_result
    assert list(card_number_generator(9, 10000000000000000)) in expected_result
    assert list(card_number_generator(10, 5)) in expected_result
