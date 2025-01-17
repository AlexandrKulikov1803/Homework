import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "expected_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        )
    ],
)
def test_filter_by_state(info_state_1: list, info_state_2: list, expected_result: list) -> None:
    assert filter_by_state(info_state_1, "EXECUTED") in expected_result
    assert filter_by_state(info_state_1, "CANCELED") in expected_result
    assert filter_by_state(info_state_1) in expected_result
    assert filter_by_state(info_state_2, "EXECUTED") in expected_result


@pytest.mark.parametrize(
    "excepted_result",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        )
    ],
)
def test_sort_by_date(info_state_1: list, info_state_3: list, excepted_result: list) -> None:
    assert sort_by_date(info_state_1) in excepted_result
    assert sort_by_date(info_state_1, False) in excepted_result
    assert sort_by_date(info_state_1, True) in excepted_result
