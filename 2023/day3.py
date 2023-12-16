"""
AdventofCode 2023 - Day 1 Challenge
"""
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

def search_adjacencies(row: int, col: int, data: List[List[str]]) -> bool: 
    adjacency = False
    
    if valid_limit(row=row-1, col=col-1, data=data):
        if data[row-1][col-1] not in NUMBERS and data[row-1][col-1] not in PLACEHOLDER:
            adjacency = True
    
    if valid_limit(row=row-1, col=col, data=data):        
        if data[row-1][col] not in NUMBERS and data[row-1][col] not in PLACEHOLDER:
            adjacency = True
    
    if valid_limit(row=row-1, col=col+1, data=data):        
        if data[row-1][col+1] not in NUMBERS and data[row-1][col+1] not in PLACEHOLDER:
            adjacency = True

    if valid_limit(row=row, col=col-1, data=data):            
        if data[row][col-1] not in NUMBERS and data[row][col-1] not in PLACEHOLDER:
            adjacency = True
    
    if valid_limit(row=row, col=col, data=data):        
        if data[row][col] not in NUMBERS and data[row][col] not in PLACEHOLDER:
            adjacency = True
    
    if valid_limit(row=row, col=col+1, data=data):        
        if data[row][col+1] not in NUMBERS and data[row][col+1] not in PLACEHOLDER:
            adjacency = True
        
    if valid_limit(row=row+1, col=col-1, data=data):
        if data[row+1][col-1] not in NUMBERS and data[row+1][col-1] not in PLACEHOLDER:
            adjacency = True
    
    if valid_limit(row=row+1, col=col, data=data):   
        if data[row+1][col] not in NUMBERS and data[row+1][col] not in PLACEHOLDER:
            adjacency = True
    
    if valid_limit(row=row+1, col=col+1, data=data):        
        if data[row+1][col+1] not in NUMBERS and data[row+1][col+1] not in PLACEHOLDER:
            adjacency = True
        
    return adjacency
        
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
                    tmp_piece.append(search_adjacencies(data=data, row=row, col=column))
                else:
                    print(f'row: {row} col: {column}: {data[row][column]}')
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
                # else:
                #     pieces.append({tmp: {'value': int(tmp)+int(tmp), 'is': is_piece}}) if len(tmp_piece) != 0 else None
                # print(f'{tmp}: {tmp_piece}: {True if True in tmp_piece else False}') if len(tmp_piece) != 0 else None
                tmp_piece = []
        
    # print(f'pieces: {pieces}')
    return pieces

def sum(data: Dict) -> int:
    result = 0
    
    for piece in data:
        if piece['is']:
            result = result + int(piece['value']) 

    print(f'the sum is: {result}')
    return result

def logic():
    # falta considerar a los del extremo derecho de la matriz. ej: 130
    data = load_file(filename='data/day3_1_test')
    
    for line in data:
        print(line)

    pieces = find_pieces(data=data)
    print(pieces)
    
    sum(pieces)
    
    import json
    f = open('dump.json', 'w')
    json.dump(pieces, f)


if __name__ == '__main__':
    logic()