import os
from unittest.mock import Mock

import pandas as pd

from src.transactions_files import transactions_csv, transactions_xlsx

directory = os.getcwd()
path_file_csv = os.path.join(directory, "data", "transactions.csv")
path_file_xlsx = os.path.join(directory, "data", "transactions_excel.xlsx")


def test_transactions_csv(transactions_files_csv_and_xlsx: pd.DataFrame) -> None:
    pd.read_csv = Mock(return_value=transactions_files_csv_and_xlsx)
    assert transactions_csv(path_file_csv) == transactions_files_csv_and_xlsx.to_dict(orient="records")


def test_transactions_csv_non_existent_file() -> None:
    path_file_csv = os.path.join(directory, "data", "non-existent_file.csv")
    assert transactions_csv(path_file_csv) == []


def test_transactions_xlsx(transactions_files_csv_and_xlsx: pd.DataFrame) -> None:
    pd.read_excel = Mock(return_value=transactions_files_csv_and_xlsx)
    assert transactions_xlsx(path_file_xlsx) == transactions_files_csv_and_xlsx.to_dict(orient="records")


def test_transactions_xlsx_non_existent_file() -> None:
    path_file_xlsx = os.path.join(directory, "data", "non-existent_file.xlsx")
    assert transactions_xlsx(path_file_xlsx) == []
