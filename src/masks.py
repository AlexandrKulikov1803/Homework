def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""

    hidden_card_number = ""
    for i, char in enumerate(card_number):
        if i in range(6, 12):
            hidden_card_number += "*"
        else:
            hidden_card_number += char

    list_number = []
    for i in range(0, len(hidden_card_number), 4):
        list_number.append(hidden_card_number[i: i + 4])
    mask_card_number = " ".join(list_number)

    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция маскировки номера банковского счёта"""
    if account != "":
        mask_account = "**" + account[-4:]
        return mask_account
    else:
        return ""
