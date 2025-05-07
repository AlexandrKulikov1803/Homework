import logging
import os

import pandas as pd

path_file = "\\".join(os.getcwd().split("\\")[: os.getcwd().split("\\").index("Homework") + 1]) + "\\logs"
os.makedirs(path_file, exist_ok=True)

logger = logging.getLogger("transactions_files")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(f"{path_file}/transactions.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transactions_csv(path_file_csv: str) -> list[dict]:
    """Функция считывает финансовые операции из CSV и выдает список словарей с транзакциями."""

    logger.info("Началось считывание файла")

    if os.path.exists(path_file_csv):
        df = pd.read_csv(path_file_csv, sep=";")
        df = df.fillna("")
        logger.info("Данные файла успешно преобразованы в список словарей")
        return df.to_dict(orient="records")
    else:
        logger.error("Преобразование невозможно")
        return []


def transactions_xlsx(path_file_xlsx: str) -> list[dict]:
    """Функция считывает финансовые операции из Excel и выдает список словарей с транзакциями."""

    logger.info("Началось считывание файла")

    if os.path.exists(path_file_xlsx):
        df = pd.read_excel(path_file_xlsx)
        logger.info("Данные файла успешно преобразованы в список словарей")
        return df.to_dict(orient="records")
    else:
        logger.error("Преобразование невозможно")
        return []
