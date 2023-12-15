"""
AdventofCode 2023 - Day 2 Challenge
"""
from math import prod
from common import load_file
from typing import List, Dict


game_cubes = {
    'blue': 14,
    'red': 12,
    'green': 13,
}

data = load_file('data/day2_1')

def valid_game(cubes: Dict) -> bool:
    """
    Compares received values with available cubes

    Args:
        cubes (Dict): {'red': '6'}

    Returns:
        bool: valid or not?
    """
    for k, v in cubes.items():
        # print(f'analyzing Game {k}-{v} if {game_cubes[k]} minor than {int(v)}')

        if game_cubes[k] < int(v):
            return False
        else:
            return True

def parse_sets(id: int, data: List[str]) -> Dict:
    """
    Give game data create a structure
    with sets

    Args:
        id (int): Game id
        data (List): string with single game info

    Returns:
        Dict: {'blue': 3, 'red': 4}
    """
    result = []
    invalid = False
    filtered_data = data.split(':')[1].split(';')

    for game in filtered_data:
        game_set = game.split(',') 

        for gs in game_set:      
            result.append({gs.split(' ')[2].replace('\n', ''): gs.split(' ')[1].replace('\n', '')})

            if not valid_game({gs.split(' ')[2].replace('\n', ''): gs.split(' ')[1].replace('\n', '')}):
                invalid = True
          
    return result, invalid

def parse_game(data: List[str]) -> int:
    """
    Returns Game index given single game data

    Args:
        data (List[str]): raw single game info

    Returns:
        int: Game index
    """
    return data.split(':')[0].split(' ')[1]

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
    result = {}
    valid_games = []
    
    for game in data:
        index = parse_game(game)
        parsed_games, invalid = parse_sets(id=index, data=game)
        result.update({index: parsed_games})

        if not invalid: valid_games.append(int(index))
        
    return result, valid_games

def valid_fewest_games(data: Dict) -> Dict:
    
    result = {}
    power = []
    
    for k, v in data.items():
        green = 0
        blue = 0
        red = 0
        
        for set in v:
            for key, value in set.items():
                value = int(value)
                
                if key == 'green': 
                    if value > green: green = value 
                if key == 'blue':
                    if value > blue: blue = value
                if key == 'red':
                    if value > red: red = value
                    
        power.append(prod([green, red, blue]))        
        result.update({k : [green, red, blue]})
    
    return result, sum(power)

def find_valid_games(data: List) -> List: 

    data, valid_games = parse_games(data=data)
    
    # print(data)
    
    cubes, sum_power = valid_fewest_games(data=data)
    
    print(f'Invalid: {valid_games}\n#: {len(valid_games)}\nsum: {sum(valid_games)}')
    print(f'Sum power: {sum_power}')
    return valid_games



if __name__ == '__main__':
    find_valid_games(data=data)