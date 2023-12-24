"""
AdventofCode 2023 - Day 5 Challenge
"""
from pprint import pprint
from common import load_file
from typing import List, Dict

MAPPERS = [
    'seed-to-soil map',
    'soil-to-fertilizer map',
    'fertilizer-to-water map',
    'water-to-light map',
    'light-to-temperature map',
    'temperature-to-humidity map',
    'humidity-to-location map',
]

def maper_generator(
    input:int, 
    destination: int, 
    source: int, 
    range_map: int) -> List[int]:
    
    print(f'Input: {input} - Source: {source} - Dest: {destination} - Range: {range_map}')
    output = None
    
    source_range = list(range(source, source+range_map))
    destination_range = list(range(destination, destination+range_map))
    
    if input in source_range:
        tmp = source_range.index(input)
        output = destination_range[tmp]
    else:
        output = input
        
    # pprint(source_range)
    # pprint(destination_range)
    # print(output)    
    
    return output, source_range, destination_range

def maper_parser(data: str):
    inputs = data[0].split(':')[1].split(' ')
    inputs = [x for x in inputs if len(x) != 0]
    print(f'Inputs: {inputs}')
    outputs = []
    
    for i in inputs:
        for line in data[1:]:
            if 'map' not in line:
                params = line.split(' ')
                params = [int(x) for x in params]
                
                if i in list(range(params[1], params[1]+params[2]))
                    maper_generator(i, params[0], params[1], params[2])

def data_cleaning(data: List[Dict[int, str]]) -> List[Dict[int, str]]:
    data = [x.replace('\n', '') for x in data]
    data = [x for x in data if len(x) != 0]
    
    return data

def logic():
    data = load_file('data/day5_test')
    data = data_cleaning(data=data)
    pprint(data)
    print('----')
    maper_parser(data=data)


if __name__ == '__main__':
    logic()
