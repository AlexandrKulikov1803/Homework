import pytest


@pytest.fixture
def card_number_1() -> str:
    return ""


@pytest.fixture
def card_number_2() -> str:
    return "7000792289606361"


@pytest.fixture
def card_number_3() -> str:
    return "700079228960636112345678"


@pytest.fixture
def account_1() -> str:
    return ""


@pytest.fixture
def account_2() -> str:
    return "73654108"


@pytest.fixture
def account_3() -> str:
    return "73654108430135874305"


@pytest.fixture
def data_1() -> str:
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def data_2() -> str:
    return ""


@pytest.fixture
def data_3() -> str:
    return "2024\\03\\11T02:26:18.671407"


@pytest.fixture
def data_4() -> str:
    return "2024.03.11T02:26:18.671407"


@pytest.fixture
def data_5() -> str:
    return "31st of February, 2023"


@pytest.fixture
def info_state_1() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def info_state_2() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def info_state_3() -> list:
    return [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
