import logging
import os

from src.masks import get_mask_account, get_mask_card_number

path_file = "\\".join(os.getcwd().split("\\")[: os.getcwd().split("\\").index("Homework") + 1]) + "\\logs"
os.makedirs(path_file, exist_ok=True)

logger = logging.getLogger("widget")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{path_file}/widget.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def mask_account_card(account_card_info: str) -> str:
    """Функция маскировки номера карты/счёта"""

    if "Счет" in account_card_info:
        logger.info("Началась маскировка номера счёта")
        account_info_mask = ""
        for i, char in enumerate(account_card_info):
            if char in "0123456789":
                account_info_mask += get_mask_account(account_card_info[i:])
                break
            else:
                account_info_mask += char
        logger.info("Маскировка номера счёта завершена успешно")
        return account_info_mask
    else:
        logger.info("Началась маскировка номера карты")
        card_info_mask = ""
        for i, char in enumerate(account_card_info):
            if char in "0123456789":
                card_info_mask += get_mask_card_number(account_card_info[i:])
                break
            else:
                card_info_mask += char
        logger.info("Маскировка номера карты завершена успешно")
        return card_info_mask


def get_date(exact_date: str) -> str:
    """Функция, которая возвращает строку с датой в формате ДД.ММ.ГГГГ"""

    logger.info("Началось преобразование даты в формат ДД.ММ.ГГГГ")

    if exact_date == "":
        return ""
    elif exact_date[4] in ".-\\":
        day = exact_date[8:10]
        month = exact_date[5:7]
        year = exact_date[0:4]
        date_format_day_month_year = day + "." + month + "." + year
        logger.info("Преобразование даты успешно завершено")
        return date_format_day_month_year
    else:
        logger.error("Невозможно преобразовать дату")
        return "Неверный формат даты"
