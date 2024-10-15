def filter_by_state(info_states: list, state: str = 'EXECUTED') -> list:
    '''Функция принимает список словарей и фильтрует его по ключу state'''
    new_list_of_states = [i for i in info_states if i['state'] == state]
    return new_list_of_states


def sort_by_date(info_states: list, order: bool = True) -> list:
    '''Функция принимает список словарей и сортирует его по дате'''
    info_states.sort(key=lambda x: x['date'], reverse=order)
    return info_states
