"""
AdventofCode 2023 - Day 5 Challenge
"""
from pprint import pprint
from common import load_file
from typing import List, Dict, Tuple
from copy import copy

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
    
    output = None
    
    min_source = source
    max_source = source+range_map
    # source_range = list(range(source, source+range_map))
    
    min_destination = destination
    max_destintion = destination+range_map
    # destination_range = list(range(destination, destination+range_map))
    
    if input >= min_source and input < max_source:
        tmp = input - min_source
        output = min_destination + tmp
    else:
        output = input
            
    return output

def analyze_seed(input: int = None, seed_data: List[str] = None) -> Dict[str, str]:
    found = False
    output = input
    
    for line in seed_data:
        if 'map' not in line:
            params = line.split(' ')
            params = [int(x) for x in params]
            print(f'analyze params: {params} for input {input}')
    
            # print(f'i:{input} in {list(range(params[1], params[1]+params[2]))} {int(input) in list(range(params[1], params[1]+params[2]))}')
            min = params[1]
            max = params[1]+params[2]
            
            if input >= min and input < max:
                found = True
                output = maper_generator(input, params[0], params[1], params[2])
                print(f'output is: {output}')
            elif not found:
                output = input
        else:
            found = False
            input = output
            print('---')
            print(f'new map: {line} - input: {input}')      
    return output

def find_min(data: List[Dict[str, str]]) -> int:
    min = float('inf')
    for res in data:
        v, = res.values()
        print(v)
        if  v < min: min = v
    return min

def create_input_ranges(input: List[str]) -> List[Tuple]:
    result = []
    if len(input) % 2 != 0: # must have even number of elements to work
        return -1
    else:
        while(input):
            a = input.pop(0); b = input.pop(0)
            result.append((int(a),int(a)+int(b)))
    return result

def maper_parser(data: str):
    inputs = data[0].split(':')[1].split(' ')
    inputs = [x for x in inputs if len(x) != 0]
    print(f'Inputs: {inputs}')
    tmp = copy(inputs)
    new_inputs = create_input_ranges(tmp)
    print(new_inputs)
    output = None
    outputs = []
    
    for seed_range in new_inputs:
        for seed in range(seed_range[0], seed_range[1]):
            print('---')
            print(f'Analyzing input seed: {seed}')   
            output = analyze_seed(input=int(seed), seed_data=data[1:])
            outputs.append({seed: output})
        
    print(f'result: {outputs}') 
    min = find_min(outputs)
    print(f'lowest location number is: {min}')

def data_cleaning(data: List[Dict[int, str]]) -> List[Dict[int, str]]:
    data = [x.replace('\n', '') for x in data]
    data = [x for x in data if len(x) != 0]
    
    return data

def logic():
    data = load_file('data/day5')
    data = data_cleaning(data=data)
    pprint(data)
    print('----')
    maper_parser(data=data)

if __name__ == '__main__':
    logic()
