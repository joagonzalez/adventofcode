"""
AdventofCode 2023 - Day 6 Challenge
"""
import numpy
from pprint import pprint
from common import load_file
from typing import List, Dict, Tuple
from copy import copy

def can_win(race_duration: int, race_record: int) -> int:
    """
    Returns in how many ways can the record be beaten
    """
    win = []
    
    for i in range(1,race_duration+1):
        race_distance = (race_duration-i) * i
        print(f'press {race_duration-i}ms at speed of {i} = distance of {race_distance}mm')
    
        if race_distance > race_record: win.append(race_distance)
    
    print(win)
    return len(win)
    
def parser(data: List[str]) -> Dict[str,str]:
    time = data[0].split(':')[1].split(' ')
    distance = data[1].split(':')[1].split(' ')
    
    time = [int(x.replace('\n','')) for x in time if x != '']
    distance = [int(x.replace('\n','')) for x in distance if x != '']
    
    return time, distance
    
def logic():
    data = load_file(filename='data/day6')
    pprint(data)
    
    time, distance = parser(data=data)
    
    print(time)
    print(distance)
    
    counter = []
    
    for index, race_time in enumerate(time):
        counter.append(can_win(race_duration=race_time, race_record=distance[index]))

    print(counter)
    print(f'result: {numpy.prod(counter)}')
    
    
if __name__ == '__main__':
    logic()