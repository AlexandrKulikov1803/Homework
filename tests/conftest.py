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
