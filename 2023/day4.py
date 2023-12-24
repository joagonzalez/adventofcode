"""
AdventofCode 2023 - Day 4 Challenge
"""
from pprint import pprint
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
            
def calculate_winning_points(data: List[str]) -> (int, List[Dict[int, str]]):
    parsed_data = parse_data(data=data)
    winner_counter = []
    
    for k, v in parsed_data.items():
        counter = 0
        for i in v['card_numbers']:
            if i in v['winner_numbers'] and i != '': 
                counter += 1        
        winner_counter.append({'card': k,'points': calculate_card_points(counter), 'counter': counter, 'qty': 1})
         
    result = add_card_points(winner_counter)
    print(f'\nWinnner counter: {winner_counter}\nTotal points: {result}')
    
    return result, winner_counter

def count_scratchcards(data: List[Dict[int, str]]) -> int:
    for index, card in enumerate(data):
        for i in range(card['card']+1,card['card']+card['counter']+1):
            data[i-1]['qty'] += 1*card['qty']

    counter = 0
    for i in data:
        counter += i['qty']
    return counter

def logic() -> None:
    data = load_file('data/day4')
    show_data(data=data)
    points, output = calculate_winning_points(data=data)
    pprint(output)
    counter = count_scratchcards(output)
    print('----')
    pprint(output)
    print(f'# of cards: {counter}')
    
if __name__ == '__main__':
    logic()