scores = {
    'rock': 1,
    'scissor': 3,
    'paper': 2,
    'win': 6,
    'draw': 3,
    'lost': 0
}

player1 = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissor'
}
player2 = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissor'
}

def open_file(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data 

def game_logic(x, y):
    winner = None # 0 is draw
    
    if 'rock' in player1[x] and 'scissor' in player2[y]:
        winner = 1
    if 'rock' in player1[x] and 'paper' in player2[y]:
        winner = 2
    if 'rock' in player1[x] and 'rock' in player2[y]:
        winner = 0
        
    if 'paper' in player1[x] and 'scissor' in player2[y]:
        winner = 2
    if 'paper' in player1[x] and 'paper' in player2[y]:
        winner = 0
    if 'paper' in player1[x] and 'rock' in player2[y]:
        winner = 1
        
    if 'scissor' in player1[x] and 'scissor' in player2[y]:
        winner = 0
    if 'scissor' in player1[x] and 'paper' in player2[y]:
        winner = 1
    if 'scissor' in player1[x] and 'rock' in player2[y]:
        winner = 2
    
    return winner
        
def run_logic(data):
    points = 0
    
    for game in data.split('\n'):
        
        if len(game) > 1:
            result = game_logic(game.split(' ')[0], game.split(' ')[1])
        
        if result == 2:
            points += scores['win']
            
        if result == 0:
            points += scores['draw']
            
    return points
            
        
    
if __name__ == '__main__':
    filename = 'day2_input.txt'
    data = open_file(filename)
    
    points = run_logic(data=data)
    
    print(f'Points for player2: {points}')