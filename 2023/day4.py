"""
AdventofCode 2023 - Day 4 Challenge
"""
from common import load_file
from typing import List, Dict


def parse_data(data: List[str]) -> Dict[str, str]: 
    result = {}
    
    for i in data:
        card = i.split(':')[0].split(' ')[-1] 
        winner_numbers = i.split(':')[1].split('|')[0].split(' ')
        card_numbers = i.split(':')[1].split('|')[1].split(' ')
        
        winner_numbers = [int(x) for x in winner_numbers if x != '']
        card_numbers = [int(x) for x in card_numbers if x != '']

        result.update({int(card): {'winner_numbers': set(winner_numbers), 'card_numbers': set(card_numbers)}})
    
    print(result)
    return result
    
def show_data(data: List[str]) -> None:
    for i in data:
        print(i, end='')
    print('\n-----')

def calculate_card_points(value: int) -> int: 
    if value < 0: return 0
    if value >= 0: return 2**(value-1)
   
def add_card_points(data: List[Dict[int, str]]) -> int:
    result = 0 
    for i in data: 
        if i['counter'] != 0: result += i['points'] 
    
    return result
            
def calculate_winning_points(data: List[str]) -> int:
    parsed_data = parse_data(data=data)
    winner_counter = []
    
    for k, v in parsed_data.items():
        counter = 0
        for i in v['card_numbers']:
            if i in v['winner_numbers'] and i != '': 
                counter += 1        
        winner_counter.append({'card': k,'points': calculate_card_points(counter), 'counter': counter})
         
    result = add_card_points(winner_counter)
    print(f'\nWinnner counter: {winner_counter}\nTotal points: {result}')
    
    return result

def logic() -> None:
    data = load_file('data/day4')
    show_data(data=data)
    calculate_winning_points(data=data)

if __name__ == '__main__':
    logic()