import pytest

from src.decorators import log


@pytest.mark.parametrize("x,y, expected_result",
                         [(5, 4, "function ok"), (5, 0, "function error: division by zero. Inputs: (5, 0), {}"),
                          (5, "s",
                           "function error: unsupported operand type(s) for /: 'int' and 'str'. Inputs: (5, 's'), {}")])
def test_console_log(capsys, x, y, expected_result):
    @log()
    def function(a, b):
        return a / b

    function(x, y)
    captured = capsys.readouterr()
    assert expected_result in captured.out

    @log("my_log.txt")
    def function(a, b):
        return a / b

    function(x, y)

    with open("../log/my_log.txt", "r", encoding="UTF-8") as file:
        result = "".join(file.readlines()[-2])[:-2]
    assert result == expected_result
