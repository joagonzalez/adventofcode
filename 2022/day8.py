from common.general import open_file


def get_rows(board):
    return len(board)

def get_cols(board):
    return len(board[0])

def print_board(board):
    for i, row in enumerate(board):
        print('')
        for j, col in enumerate(row):
            print(f'{board[i][j]}', end=' ')
    print('\n')

def analyze(tree, neighbor, result):
    if tree > neighbor:
        result.add(True)
    else:
        result.add(False)
    # print(f'tmp for: {tree},{neighbor}: {result}')   
    return result

def evaluate(board, row, col, data, type=None):
    _visible = False
    _found = False
    counter = 0
    tmp = set()

    if type is None:
        for value in data:
            print(f'cols: compare if {board[row][col]} is higher than {value}') 
            analyze(tree=board[row][col], neighbor=value, result=tmp)
            
            if not _found:
                counter +=1
                if False in tmp:
                    _found = True
                
    if type is not None:
        for value in data[::-1]:
            print(f'rows: compare if {board[row][col]} is higher than {value[col]}')
            tmp = analyze(tree=board[row][col], neighbor=value[col], result=tmp)     
            
            if not _found:
                counter +=1
                if False in tmp:
                    _found = True           

    if False not in tmp:
        _visible = True
        
    return _visible, counter

def is_visible(board, row, col):
    _visible = set()
    # right
    right, view_right = evaluate(board=board, row=row, col=col, data=board[row][col+1:])
    _visible.add(right)
    # left
    left, view_left = evaluate(board=board, row=row, col=col, data=board[row][:col][::-1]) 
    _visible.add(left)
    # top 
    top, view_top = evaluate(board=board, row=row, col=col, data=board[:row], type='row')
    _visible.add(top)
    # bottom
    bottom, view_bottom = evaluate(board=board, row=row, col=col, data=board[row+1:], type='row')
    _visible.add(bottom)     
    
    total_view = view_bottom * view_left * view_right * view_top
    print(f'scenic score is {total_view} = {view_left}*{view_right}*{view_top}*{view_bottom}')
    
    return True in _visible, total_view

def find_visible_trees(board, rows, cols):
    result = 0
    scenic_score = []
    
    for i, row in enumerate(board):
        for j, tree in enumerate(row):
            if i != 0 and j != 0 and i != rows-1 and j != cols-1:
                _is_visible, view = is_visible(board=board, row=i, col=j)
                scenic_score.append(view)
                print(f'analyze if tree ({i},{j}) = {tree} is visible: {_is_visible}')
                print('---------------')
                if _is_visible:
                    result += 1
    return result, max(scenic_score)
                

if __name__ == '__main__':
    filename = 'test.txt'
    filename_prod='day8_input.txt'
    board = open_file(filename=filename_prod).split('\n')
    rows = len(board)
    cols = len(board[0])
    edges = rows * 2 + (cols - 2) * 2
    
    print(f'rows: {rows} - cols: {cols} - edges: {edges}')
    print_board(board=board)
    
    inner_trees, scenic_score = find_visible_trees(board=board, rows=rows, cols=cols)
    
    print(f'visible trees: {inner_trees + edges} - max scenic score: {scenic_score}')