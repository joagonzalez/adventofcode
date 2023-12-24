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

def maper_generator(destination: int, source: int, range: int) -> List[int]:
    
    
def maper_parser(data: str): pass

def logic():
    data = load_file('data/day5_test')
    pprint(data)


if __name__ == '__main__':
    logic()
