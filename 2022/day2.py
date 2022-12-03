scores = {
    'rock': 1,
    'paper': 2,
    'scissor': 3,
    'win': 6,
    'draw': 3,
    'lose': 0
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
    choice = None
    
    if 'rock' in player1[x] and 'scissor' in player2[y]:
        winner = 1
        choice = 'scissor'
    if 'rock' in player1[x] and 'paper' in player2[y]:
        winner = 2
        choice = 'paper'
    if 'rock' in player1[x] and 'rock' in player2[y]:
        winner = 0
        choice = 'rock'
        
    if 'paper' in player1[x] and 'scissor' in player2[y]:
        winner = 2
        choice = 'scissor'
    if 'paper' in player1[x] and 'paper' in player2[y]:
        winner = 0
        choice = 'paper'
    if 'paper' in player1[x] and 'rock' in player2[y]:
        winner = 1
        choice = 'rock'
        
    if 'scissor' in player1[x] and 'scissor' in player2[y]:
        winner = 0
        choice = 'scissor'
    if 'scissor' in player1[x] and 'paper' in player2[y]:
        winner = 1
        choice = 'paper'
    if 'scissor' in player1[x] and 'rock' in player2[y]:
        winner = 2
        choice = 'rock'
    
    return winner, choice
        
def run_logic(data):
    points = 0
    data = data.split('\n')
    print(f'size: {len(data)}')
    
    for game in data:
        print(f'Analyzing {game} data')
        if len(game) > 1:
            result, choice = game_logic(game.split(' ')[0], game.split(' ')[1])
        
        if result == 2:
            add = scores['win'] + scores[choice]
            print(f'result is win for player 2 and choose {choice} and adds {add} points')
            points += add
            
        if result == 0:
            add = scores['draw'] + scores[choice]
            print(f'result is draw and player2 choose {choice} and adds {add} points')
            points += add
            
        if result == 1:
            add = scores['lose'] + scores[choice]
            print(f'result is win for player1 and player2 choose {choice} and adds {add} points')
            points += add
            
    return points
            
        
    
if __name__ == '__main__':
    filename = 'day2_input.txt'
    data = open_file(filename)
    
    points = run_logic(data=data)
    
    print(f'Points for player2: {points}')