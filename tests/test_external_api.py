from unittest.mock import Mock, patch

from src.external_api import currency_conversion


def test_currency_conversion_RUB(transaction_RUB: dict) -> None:
    assert currency_conversion(transaction_RUB) == 100.0


@patch("src.external_api.requests.get")
def test_currency_conversion_not_RUB(mocked_get: Mock, transaction_EUR: dict, transaction_USD: dict) -> None:
    mocked_get.return_value.json.return_value = {"result": 200}
    assert currency_conversion(transaction_EUR) == 200
    mocked_get.return_value.json.return_value = {"result": 300}
    assert currency_conversion(transaction_USD) == 300
