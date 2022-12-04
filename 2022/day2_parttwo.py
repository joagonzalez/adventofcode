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
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

def open_file(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data 

def decision(decision, game_result):
    points = scores[game_result]      
    if 'win' in game_result:  
        if 'rock' in decision:
            points += scores['paper']
        
        if 'paper' in decision:
            points += scores['scissor']
        
        if 'scissor' in decision:
            points += scores['rock']
        
    if 'draw' in game_result:        
        if 'rock' in decision:
            points += scores['rock']
        
        if 'paper' in decision:
            points += scores['paper']
        
        if 'scissor' in decision:
            points += scores['scissor']

    if 'lose' in game_result:        
        if 'rock' in decision:
            points += scores['scissor']
        
        if 'paper' in decision:
            points += scores['rock']
        
        if 'scissor' in decision:
            points += scores['paper']
        
    return points

def game_logic(x, y):
    return decision(
                decision=player1[x], 
                game_result=player2[y])
         
def run_logic(data):
    points = 0
    data = data.split('\n')
    print(f'size: {len(data)}')
    
    for game in data:
        print(f'Analyzing {game} data')
        if len(game) > 1:
            points += game_logic(game.split(' ')[0], game.split(' ')[1])
            
    return points
            
if __name__ == '__main__':
    filename = 'day2_input.txt'
    data = open_file(filename)
    
    points = run_logic(data=data)
    
    print(f'Points for player2: {points}')