import os

from src.generators import filter_by_currency
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_key_string, filter_by_state, sort_by_date
from src.transactions_files import transactions_csv, transactions_xlsx
from src.utils import get_financial_transaction_data
from src.widget import get_date

directory = os.getcwd()

print(
    """Привет! Добро пожаловать в программу работы с банковскими транзакциями.

Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
"""
)

menu_item = int(input("Пользователь:"))

if menu_item == 1:
    print("\nДля обработки выбран JSON-файл.")
    path_json_str = os.path.join(directory, "data", "operations.json")
    list_transactions = get_financial_transaction_data(path_json_str)
elif menu_item == 2:
    print("\nДля обработки выбран CSV-файл.")
    path_csv_str = os.path.join(directory, "data", "transactions.csv")
    list_transactions = transactions_csv(path_csv_str)
else:
    print("\nДля обработки выбран XLSX-файл.")
    path_xlsx_str = os.path.join(directory, "data", "transactions_excel.xlsx")
    list_transactions = transactions_xlsx(path_xlsx_str)

while True:
    print(
        """\nВведите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )
    status = input("Пользователь:").upper()

    if status in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'\nОперации отфильтрованы по статусу "{status}"')
        list_transactions = filter_by_state(list_transactions, status)
        break
    else:
        print(f'\nСтатус операции "{status}" недоступен.')

while True:
    print("\nОтсортировать операции по дате? да/нет")
    answer_1 = input("Пользователь:").lower()

    if answer_1 == "да":
        while True:
            print("\nОтсортировать по возрастанию или по убыванию? по возрастанию/по убыванию")
            answer_2 = input("Пользователь:").lower()

            if answer_2 == "по возрастанию":
                list_transactions = sort_by_date(list_transactions, False)
                break
            elif answer_2 == "по убыванию":
                list_transactions = sort_by_date(list_transactions, True)
                break
        break
    elif answer_1 == "нет":
        break

while True:
    print("\nВыводить только рублевые транзакции? да/нет")

    answer = input("Пользователь:").lower()

    if answer == "да":
        list_transactions = list(filter_by_currency(list_transactions, "RUB"))
        break
    elif answer == "нет":
        break

while True:
    print("\nОтфильтровать список транзакций по определенному слову в описании? да/нет")

    answer = input("Пользователь:").lower()

    if answer == "да":
        print("\nВведите ключевое слово")
        key_word = input("Пользователь:")
        list_transactions = filter_by_key_string(list_transactions, key_word)
        break
    elif answer == "нет":
        break

print("\nРаспечатываю итоговый список транзакций...\n")

count_transactions = len(list_transactions)

if count_transactions == 0:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
    print(f"Всего банковских операций в выборке: {count_transactions}\n")

    for transaction in list_transactions:
        date = get_date(transaction["date"])
        amount = transaction.get("amount") or transaction.get("operationAmount")["amount"]
        currency = transaction.get("currency_code") or transaction.get("operationAmount")["currency"]["name"]
        transaction_from = transaction.get("from")
        transaction_to = transaction.get("to")

        if transaction["description"] == "Открытие вклада":
            print(f"{date} Открытие вклада")
            print(f"Счет {get_mask_account(transaction_to)}")

        elif transaction["description"] == "Перевод с карты на карту":
            print(f"{date} Перевод с карты на карту")

            name_card_from = ""
            number_card_from = ""
            for i in transaction_from:
                if i.isdigit():
                    number_card_from += i
                else:
                    name_card_from += i
            number_card_from = get_mask_card_number(number_card_from)

            name_card_to = ""
            number_card_to = ""
            for i in transaction_to:
                if i.isdigit():
                    number_card_to += i
                else:
                    name_card_to += i
            number_card_to = get_mask_card_number(number_card_to)
            print(f"{name_card_from} {number_card_from} -> {name_card_to} {number_card_to}")

        elif transaction["description"] == "Перевод организации":
            print(f"{date} Перевод организации")
            name_card_from = ""
            number_card_from = ""
            for i in transaction_from:
                if i.isdigit():
                    number_card_from += i
                else:
                    name_card_from += i
            print(
                f"{name_card_from} {get_mask_card_number(number_card_from)} -> Счет {get_mask_account(transaction_to)}"
            )

        elif transaction["description"] == "Перевод со счета на счет":
            print(f"{date} Перевод со счета на счет")
            print(f"Счет {get_mask_account(transaction_from)} -> Счет {get_mask_account(transaction_to)}")

        elif transaction["description"] == "Перевод с карты на счет":
            print(f"{date} Перевод с карты на счет")
            name_card_from = ""
            number_card_from = ""
            for i in transaction_from:
                if i.isdigit():
                    number_card_from += i
                else:
                    name_card_from += i
            print(
                f"{name_card_from} {get_mask_card_number(number_card_from)} -> Счет {get_mask_account(transaction_to)}"
            )

        print(f"Сумма: {amount} {currency}\n")
