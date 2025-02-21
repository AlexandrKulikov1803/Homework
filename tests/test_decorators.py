import os
from typing import Any

import pytest


@pytest.mark.parametrize(
    "x,y, expected_result",
    [
        (5, 4, "function ok"),
        (5, 0, "function error: division by zero. Inputs: (5, 0), {}"),
        (5, "s", "function error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: (5, 's'), {}"),
    ],
)
def test_console_log(capsys: Any, decorated_function_1: Any, decorated_function_2: Any,
                     x: Any, y: Any, expected_result: str) -> None:
    decorated_function_1(x, y)
    captured = capsys.readouterr()
    assert expected_result in captured.out

    decorated_function_2(x, y)
    path_file = os.path.abspath(__file__)
    path_by_project = "/".join(path_file.split("\\")[: path_file.split("\\").index("Homework") + 1])

    with open(path_by_project + "/log/my_log.txt", "r", encoding="UTF-8") as file:
        result = "".join(file.readlines()[-2])[:-2]
    assert result == expected_result
    os.remove(path_by_project + "/log/my_log.txt")
