from functools import wraps
import os


def log(file_name: str = None) -> [int, float]:
    """Функция-декоратор, которая автоматически логирует начало и
    конец выполнения функции, а также ее результаты или возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # result = func(*args, **kwargs)
                func(*args, **kwargs)
                message = f"{func.__name__} ok \n"
            except Exception as error:
                message = f"{func.__name__} error: {error}. Inputs: {args}, {kwargs} \n"
            if file_name:
                os.makedirs("../log", exist_ok=True)
                filepath = os.path.join("../log", f"{file_name}")
                with open(filepath, 'a', encoding="UTF-8") as file:
                    file.write(message + "\n")
            else:
                print(message)
            # return result

        return wrapper

    return decorator
