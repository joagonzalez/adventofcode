"""
AdventofCode 2023 - Day 1 Challenge
"""
from common import load_file
from typing import List, Dict


game_cubes = {
    'blue': 14,
    'red': 12,
    'green': 13,
}

data = load_file('data/day2_1_test')


def parse_sets(data: List) -> Dict: pass

def parse_games(data: List) -> Dict:
    """
    Parse raw games data and build dict structure
    with everything needed to decide if its a 
    valid game or not

    Args:
        data (List): List with lines of raw data file

    Returns:
        Dict: Dict with structure data
    
        key: game index
        value: list with dicts, each dict is a set in the game
    {
        '1': [{'blue': 3, 'red': 4}, ...]
    }
    """
    pass

def find_valid_games(data: List) -> List: 
    return [3, 4]