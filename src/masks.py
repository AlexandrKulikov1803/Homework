import logging
import os

path_file = "\\".join(os.getcwd().split("\\")[: os.getcwd().split("\\").index("Homework") + 1]) + "\\logs"
os.makedirs(path_file, exist_ok=True)

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{path_file}/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""

    logger.info("Началась маскировка номера банковской карты")

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
    logger.info("Маскировка номера банковской карты успешно завершена")
    return mask_card_number


def get_mask_account(account: str) -> str:
    """Функция маскировки номера банковского счёта"""

    logger.info("Началась маскировка номера банковского счёта")

    if account != "":
        mask_account = "**" + account[-4:]
        logger.info("Маскировка номера банковского счёта успешно завершена")
        return mask_account
    else:
        logger.error("Невозможно замаскировать номер банковского счёта")
        return ""
