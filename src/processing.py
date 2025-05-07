import logging
import os
import re

path_file = "\\".join(os.getcwd().split("\\")[: os.getcwd().split("\\").index("Homework") + 1]) + "\\logs"
os.makedirs(path_file, exist_ok=True)

logger = logging.getLogger("processing")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{path_file}/processing.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filter_by_state(info_states: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и фильтрует его по ключу state"""

    logger.info("Началась фильтрация по ключу")

    new_list_of_states = [i for i in info_states if (("state" in i) and (i["state"] == state))]
    logger.info("Фильтрация по ключу успешно завершена")
    return new_list_of_states


def sort_by_date(info_states: list, order: bool = True) -> list:
    """Функция принимает список словарей и сортирует его по дате"""

    logger.info("Началась фильтрация по дате")

    info_states.sort(key=lambda x: x["date"], reverse=order)
    logger.info("Фильтрация по дате успешно завершена")
    return info_states


def filter_by_key_string(info_states: list, key_string: str) -> list:
    """Функция принимает список словарей и фильтрует его по строке поиска"""

    logger.info("Началась фильтрация по строке поиска")

    new_list_of_states = []
    pattern = rf"{re.escape(key_string)}"
    for i in info_states:
        if i.get("description") is None or type(i.get("description")) == float:
            continue
        elif re.search(pattern, i.get("description"), re.IGNORECASE):
            new_list_of_states.append(i)
    logger.info("Фильтрация по строке поиска успешно завершена")
    return new_list_of_states
