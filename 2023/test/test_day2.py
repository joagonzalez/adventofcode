import pytest
from common import load_file
from day2 import find_valid_games



test_solution = [1, 2, 5]
test_data = load_file('data/day2_1_test')


def test_day2_find_valid():
    assert find_valid_games(test_data) == test_solution