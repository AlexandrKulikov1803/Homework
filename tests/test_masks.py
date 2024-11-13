from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(card_number_1: str, card_number_2: str, card_number_3: str) -> None:
    assert get_mask_card_number(card_number_1) == ""
    assert get_mask_card_number(card_number_2) == "7000 79** **** 6361"
    assert get_mask_card_number(card_number_3) == "7000 79** **** 6361 1234 5678"


def test_mask_account(account_1: str, account_2: str, account_3: str) -> None:
    assert get_mask_account(account_1) == ""
    assert get_mask_account(account_2) == "**4108"
    assert get_mask_account(account_3) == "**4305"
