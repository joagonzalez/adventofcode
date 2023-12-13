"""
AdventofCode 2023 - Day 1 Challenge
"""
from common import load_file



numbers = ['1','2','3','4','5','6','7','8','9','0']
string_numbers_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
}
special_cases = {
    'oneight': '18',
    'twone': '21',
    'threeight': '38',
    'fiveight': '58',
    'sevenine': '75',
    'eightwo': '82',
    'eighthree': '83',
    'nineight': '98',
}

def sum_custom(a: int, b: int) -> int:
    return a+b

def find_number(directon: str = 'left', word: str = '') -> int:
    result = None
    
    if directon == 'left':
        for letter in word:
            if letter in numbers:
                result = int(letter)
                break
    else:
        reverse = word[::-1]
        for letter in reverse:
            if letter in numbers:
                result = int(letter)
                break
    
    return result

def letters2numbers(word: str = '') -> str:

    for k, v in special_cases.items():
        if k in word:
            word = word.replace(k, special_cases[k])
            
    for k, v in string_numbers_map.items():
        if k in word:
            word = word.replace(k, string_numbers_map[k])
                
    return word.replace('\n', '')
    
def find_calibration_value(line: str = ''):
    left = find_number(directon='left', word=line)
    right = find_number(directon='right', word=line)
        
    return int(str(left)+str(right)) 

def day1(filename: str = 'data/day1'):
    data = load_file(filename=filename)
    results = []
    
    for i in data:
        results.append(find_calibration_value(line=i))
        
    return sum(results)

def day1_2(filename: str = 'data/day1_2'):
    data = load_file(filename=filename)
    results = []
    
    data = [letters2numbers(word) for word in data]
        
    for i in data:
        results.append(find_calibration_value(line=i))
     
    return sum(results)



if __name__ == '__main__':
    print(f'Result part one: {day1(filename="data/day1")}')
    print(f'Result part two: {day1_2(filename="data/day1")}')