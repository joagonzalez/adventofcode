"""
AdventofCode 2023 - Day 4 Challenge Unit Tests
"""
from common import load_file
from typing import List, Dict
from day4 import calculate_winning_points


test_solution = 13
test_data = load_file('data/day4_test')


def test_scratchcards():
    assert calculate_winning_points(test_data) == test_solution

