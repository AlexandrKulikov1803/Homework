import re


def filter_by_state(info_states: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и фильтрует его по ключу state"""

    new_list_of_states = [i for i in info_states if (("state" in i) and (i["state"] == state))]
    return new_list_of_states


def sort_by_date(info_states: list, order: bool = True) -> list:
    """Функция принимает список словарей и сортирует его по дате"""

    info_states.sort(key=lambda x: x["date"], reverse=order)
    return info_states


def filter_by_key_string(info_states: list, key_string: str) -> list:
    """Функция принимает список словарей и фильтрует его по строке поиска"""

    new_list_of_states = []
    pattern = rf"{re.escape(key_string)}"
    for i in info_states:
        if i.get("description") is None or type(i.get("description")) == float:
            continue
        elif re.search(pattern, i.get("description"), re.IGNORECASE):
            new_list_of_states.append(i)
    return new_list_of_states
