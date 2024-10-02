from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    """Функция маскировки номера карты/счёта"""
    if "Счет" in account_card_info:
        account_info_mask = ""
        for i, char in enumerate(account_card_info):
            if char in "0123456789":
                account_info_mask += get_mask_account(account_card_info[i:])
                break
            else:
                account_info_mask += char
        return account_info_mask
    else:
        card_info_mask = ""
        for i, char in enumerate(account_card_info):
            if char in "0123456789":
                card_info_mask += get_mask_card_number(account_card_info[i:])
                break
            else:
                card_info_mask += char
        return card_info_mask


def get_date(exact_date: str) -> str:
    day = exact_date[8:10]
    month = exact_date[5:7]
    year = exact_date[0:4]
    date_format_day_month_year = day + "." + month + "." + year
    return date_format_day_month_year
