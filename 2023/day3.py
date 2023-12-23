"""
AdventofCode 2023 - Day 3 Challenge
"""
import sys
from common import load_file
from typing import List, Dict


PLACEHOLDER = '.'
NUMBERS = ['1','2','3','4','5','6','7','8','9','0', '\n']


def valid_limit(row: int, col: int, data: List[List[str]]) -> bool:
    cols = len(data[0].replace('\n',''))
    rows = len(data)
    
    if row >= 0 and row < rows and col >= 0 and col < cols:
        return True
    
    return False
      
def is_number(char: str) -> bool:
    return True if char in NUMBERS else False

def is_gear(char: str) -> bool:
    return True if char in ['*'] else False

def search_adjacencies(row: int, col: int, data: List[List[str]]) -> bool: 
    adjacency = False
    gears = []
    
    if valid_limit(row=row-1, col=col-1, data=data):
        if data[row-1][col-1] not in NUMBERS and data[row-1][col-1] not in PLACEHOLDER:
            if is_gear(data[row-1][col-1]): gears.append([row-1, col-1])
            adjacency = True
    
    if valid_limit(row=row-1, col=col, data=data):        
        if data[row-1][col] not in NUMBERS and data[row-1][col] not in PLACEHOLDER:
            if is_gear(data[row-1][col]): gears.append([row-1, col])
            adjacency = True
    
    if valid_limit(row=row-1, col=col+1, data=data):        
        if data[row-1][col+1] not in NUMBERS and data[row-1][col+1] not in PLACEHOLDER:
            if is_gear(data[row-1][col+1]): gears.append([row-1, col+1])
            adjacency = True

    if valid_limit(row=row, col=col-1, data=data):            
        if data[row][col-1] not in NUMBERS and data[row][col-1] not in PLACEHOLDER:
            if is_gear(data[row][col-1]): gears.append([row, col-1])
            adjacency = True
    
    if valid_limit(row=row, col=col, data=data):        
        if data[row][col] not in NUMBERS and data[row][col] not in PLACEHOLDER:
            if is_gear(data[row][col]): gears.append([row, col])
            adjacency = True
    
    if valid_limit(row=row, col=col+1, data=data):        
        if data[row][col+1] not in NUMBERS and data[row][col+1] not in PLACEHOLDER:
            if is_gear(data[row][col+1]): gears.append([row, col+1])
            adjacency = True
        
    if valid_limit(row=row+1, col=col-1, data=data):
        if data[row+1][col-1] not in NUMBERS and data[row+1][col-1] not in PLACEHOLDER:
            if is_gear(data[row+1][col-1]): gears.append([row+1, col-1])
            adjacency = True
    
    if valid_limit(row=row+1, col=col, data=data):   
        if data[row+1][col] not in NUMBERS and data[row+1][col] not in PLACEHOLDER:
            if is_gear(data[row+1][col]): gears.append([row+1, col])
            adjacency = True
    
    if valid_limit(row=row+1, col=col+1, data=data):        
        if data[row+1][col+1] not in NUMBERS and data[row+1][col+1] not in PLACEHOLDER:
            if is_gear(data[row+1][col+1]): gears.append([row+1, col+1])
            adjacency = True
        
    return adjacency, gears
        
def find_pieces(data: List[str]) -> Dict[str, Dict[str, str]]: 
    pieces = []
    tmp = ''
    tmp_piece = []
    save = False
       
    for row, row_value in enumerate(data):
        for column, column_value in enumerate(row_value):
            if valid_limit(row=row, col=column, data=data):
                if is_number(data[row][column]) and column == len(row_value)-2:
                    tmp += data[row][column]
                    save = True
                
                elif is_number(data[row][column]) and column != len(row_value):
                    save = False
                    is_piece = False
                    if valid_limit(row=row, col=column-1, data=data) and is_number(data[row][column-1]): 
                        tmp += data[row][column]
                    else:
                        tmp = data[row][column]
                        
                    adjacency, counter = search_adjacencies(data=data, row=row, col=column)
                    tmp_piece.append(adjacency)
                else:
                    if column == len(row_value) and is_number(data[row][column]):
                        save = True
                    
                    if valid_limit(row=row, col=column-1, data=data) and is_number(data[row][column-1]):
                        save = True                  
            
            if save: 
                if True in tmp_piece: 
                    is_piece = True
                else:
                    is_piece = False
                
                if tmp not in pieces:
                    pieces.append({'value': tmp, 'is': is_piece}) if len(tmp_piece) != 0 else None

                tmp_piece = []
        
    return pieces

def find_gears(data: List[str]) -> Dict[str, Dict[str, str]]: 
    pieces = []
    gears = []
    tmp = ''
    tmp_piece = []
    tmp_gear_counter = None
    tmp_gears = []
    save = False
       
    for row, row_value in enumerate(data):
        for column, column_value in enumerate(row_value):
            if valid_limit(row=row, col=column, data=data):
                
                if is_gear(data[row][column]):
                    gears.append({'symbol': data[row][column], 'coordinates': [row, column]})
                
                if is_number(data[row][column]) and column == len(row_value)-2:
                    tmp += data[row][column]
                    save = True
                
                elif is_number(data[row][column]) and column != len(row_value):
                    save = False
                    is_piece = False
                    if valid_limit(row=row, col=column-1, data=data) and is_number(data[row][column-1]): 
                        tmp += data[row][column]
                    else:
                        tmp = data[row][column]
                        
                    adjacency, tmp_gear_counter = search_adjacencies(data=data, row=row, col=column)
                    tmp_piece.append(adjacency)
                    tmp_gears.append(tmp_gear_counter)
                else:
                    if column == len(row_value) and is_number(data[row][column]):
                        save = True
                    
                    if valid_limit(row=row, col=column-1, data=data) and is_number(data[row][column-1]):
                        save = True                  
            
            if save: 
                if True in tmp_piece: 
                    is_piece = True
                else:
                    is_piece = False
                
                if tmp not in pieces:
                    pieces.append({'value': tmp, 'is': is_piece, 'neigh_gears_count': len([x for x in tmp_gears if x != []]), 'neigh_gears': tmp_gears}) if len(tmp_piece) != 0 else None

                tmp_piece = []
                tmp_gears = []
        
    return pieces, gears

def find_valid_pieces(pieces: List[Dict[str,str]], gears: List[Dict[str,str]]) -> Dict[str, Dict[str, str]]:
    print(gears)
    print(pieces)
    pairs = []
    
    for gear in gears:
        pair = []
        for piece in pieces:
            if gear['coordinates'] in [x[0] for x in piece['neigh_gears'] if x != []]:
                pair.append(piece['value'])
        if len(pair) == 2:
            pairs.append(pair)
        
    print(pairs)
    
    result = []
    for pair in pairs:
        result.append(int(pair[0])*int(pair[1]))
    print(f'result = {sum(result)}')
    
def sum_pieces(data: Dict) -> int:
    result = 0
    
    for piece in data:
        if piece['is']:
            result = result + int(piece['value']) 

    print(f'the sum is: {result}')
    return result

def logic():
    # falta considerar a los del extremo derecho de la matriz. ej: 130
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = 'data/day3_1'
        
    data = load_file(filename=filename)
    
    for line in data:
        print(line)

    pieces = find_pieces(data=data)
    print(pieces)
    sum_pieces(pieces)
    
    pieces, gears = find_gears(data=data)
    find_valid_pieces(pieces=pieces, gears=gears)
    

if __name__ == '__main__':
    logic()