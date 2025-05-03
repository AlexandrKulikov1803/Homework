import pytest

from src.processing import filter_by_key_string, filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        )
    ],
)
def test_filter_by_state(info_state_1: list, info_state_2: list, expected_result: list) -> None:
    assert filter_by_state(info_state_1, "EXECUTED") in expected_result
    assert filter_by_state(info_state_1, "CANCELED") in expected_result
    assert filter_by_state(info_state_1) in expected_result
    assert filter_by_state(info_state_2, "EXECUTED") in expected_result


@pytest.mark.parametrize(
    "excepted_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        )
    ],
)
def test_sort_by_date(info_state_1: list, info_state_3: list, excepted_result: list) -> None:
    assert sort_by_date(info_state_1) in excepted_result
    assert sort_by_date(info_state_1, False) in excepted_result
    assert sort_by_date(info_state_1, True) in excepted_result


@pytest.mark.parametrize(
    "expected_result",
    [
        (
            [
                {
                    "id": 587085106,
                    "state": "EXECUTED",
                    "date": "2018-03-23T10:45:06.972075",
                    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 41421565395219882431",
                },
                {
                    "id": 596171168,
                    "state": "EXECUTED",
                    "date": "2018-07-11T02:26:18.671407",
                    "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 72082042523231456215",
                },
                {
                    "id": 863064926,
                    "state": "EXECUTED",
                    "date": "2019-12-08T22:46:21.935582",
                    "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Открытие вклада",
                    "to": "Счет 90424923579946435907",
                },
                {
                    "id": 172864002,
                    "state": "EXECUTED",
                    "date": "2018-12-28T23:10:35.459698",
                    "operationAmount": {"amount": "49192.52", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Открытие вклада",
                    "to": "Счет 96231448929365202391",
                },
                {
                    "id": 801684332,
                    "state": "EXECUTED",
                    "date": "2019-11-05T12:04:13.781725",
                    "operationAmount": {"amount": "21344.35", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 77613226829885488381",
                },
                {
                    "id": 108066781,
                    "state": "EXECUTED",
                    "date": "2019-06-21T12:34:06.351022",
                    "operationAmount": {"amount": "25762.92", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 90817634362091276762",
                },
                {
                    "id": 285353808,
                    "state": "EXECUTED",
                    "date": "2018-08-06T16:22:54.643491",
                    "operationAmount": {"amount": "82946.19", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 12189246980267075758",
                },
                {
                    "id": 176798279,
                    "state": "CANCELED",
                    "date": "2019-04-18T11:22:18.800453",
                    "operationAmount": {"amount": "73778.48", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 90417871337969064865",
                },
                {
                    "id": 893507143,
                    "state": "EXECUTED",
                    "date": "2018-02-03T07:16:28.366141",
                    "operationAmount": {"amount": "90297.21", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 37653295304860108767",
                },
                {
                    "id": 207126257,
                    "state": "EXECUTED",
                    "date": "2019-07-15T11:47:40.496961",
                    "operationAmount": {"amount": "92688.46", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Открытие вклада",
                    "to": "Счет 35737585785074382265",
                },
            ]
        )
    ],
)
def test_filter_by_key_string(list_of_transactions: list, expected_result: list) -> None:
    assert filter_by_key_string(list_of_transactions, "КлАд") == expected_result
    assert filter_by_key_string(list_of_transactions, "оТКРыТие") == expected_result
    assert filter_by_key_string(list_of_transactions, "Вложение") == []
