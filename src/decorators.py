import os
from functools import wraps
from typing import Any, Callable


def log(file_name: str = "") -> Any:
    """Функция-декоратор, которая автоматически логирует начало и
    конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def decorator(func: Callable[[Any, Any], Any]) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                func(*args, **kwargs)
                message = f"{func.__name__} ok \n"
            except Exception as error:
                message = f"{func.__name__} error: {error}. Inputs: {args}, {kwargs} \n"
                result = "error"
            if file_name:

                path_file = os.getcwd()
                path_by_project = "\\".join(path_file.split("\\")[: path_file.split("\\").index("Homework") + 1])
                path_by_log = path_by_project + "\\log"
                os.makedirs(path_by_log, exist_ok=True)
                path_by_log = path_by_log + f"\\{file_name}"
                with open(path_by_log, "a", encoding="UTF-8") as file:
                    file.write(message + "\n")
            else:
                print(message)
            return result

        return wrapper

    return decorator
