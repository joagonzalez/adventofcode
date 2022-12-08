# stack implementation (FILO)
from common.stack import Stack
from common.general import open_file


def load_data():
    return {
        '1': ['Z', 'P', 'M', 'H', 'R'],
        '2': ['P', 'C', 'J', 'B'],
        '3': ['S', 'N', 'H', 'G', 'L', 'C', 'D'],
        '4': ['F', 'T', 'M', 'D', 'Q', 'S', 'R', 'L'],
        '5': ['F', 'S', 'P', 'Q', 'B', 'T', 'Z', 'M'],
        '6': ['T', 'F', 'S', 'Z', 'B', 'G'],
        '7': ['N', 'R', 'V'],
        '8': ['P', 'G', 'L', 'T', 'D', 'V', 'C', 'M'],
        '9': ['W', 'Q', 'N', 'J', 'F', 'M', 'L'], 
        }
    # return {
    #     '1': ['Z', 'N'],
    #     '2': ['M', 'C', 'D'],
    #     '3': ['P']
    # }


def show_stacks(stacks):
    i = 0
    for stack in stacks:
        i += 1 
        print(f'{i} - {stack}')
    
def load_instructions():
    data = open_file(filename='day5_input.txt').split('\n')
    instructions = [x for x in data if 'move' in x]
    
    return instructions

def load_stacks():
    data = load_data()
    stacks = [Stack() for s in range(STACKS)]

    i = 0
    
    for stack in stacks:
        i += 1 
        
        for v in data[str(i)]:
            stack.push(v)
            
        print(f'{i} - {stack}')
    
    return stacks
   
def parse_instruction(instruction):
    quantity = instruction.split(' ')[1]
    source = instruction.split(' ')[3]
    destination = instruction.split(' ')[5]
    
    return int(quantity), int(source), int(destination)
   
def run_logic(instructions, stacks):
    for instruction in instructions:
        quantity, source, destination = parse_instruction(instruction=instruction)
        print(f'q: {quantity} - s: {source} - d: {destination}')    

        tmp = []
        
        for i in range(int(quantity)):
            tmp.append(stacks[source-1].pop())
            print(f'remove {tmp} from {source} to {destination}')
        
        tmp.reverse()
        
        for d in tmp:
            if d is not None:
                stacks[destination-1].push(d)

STACKS = len(load_data())
    
if __name__ == '__main__':
    
    instructions = load_instructions()
    stacks = load_stacks()

    run_logic(instructions=instructions, stacks=stacks)
    
    show_stacks(stacks=stacks)
    
    '''
    ANSWER: VQZNJMWTR
    1 - Stack elements: ['D', 'G', 'V'] - Stack size: 3
    2 - Stack elements: ['G', 'P', 'Q', 'T', 'C', 'B', 'T', 'M', 'C', 'V', 'S', 'M', 'R', 'F', 'Q'] - Stack size: 15
    3 - Stack elements: ['P', 'S', 'M', 'Z', 'Z'] - Stack size: 5
    4 - Stack elements: ['M', 'F', 'L', 'F', 'P', 'B', 'N', 'S', 'L', 'L', 'D', 'N'] - Stack size: 12
    5 - Stack elements: ['J'] - Stack size: 1
    6 - Stack elements: ['N', 'H', 'R', 'Z', 'L', 'Q', 'M'] - Stack size: 7
    7 - Stack elements: ['H', 'P', 'C', 'W'] - Stack size: 4
    8 - Stack elements: ['D', 'S', 'T'] - Stack size: 3
    9 - Stack elements: ['G', 'J', 'F', 'B', 'T', 'R'] - Stack size: 6
    
    
    for i in range(int(quantity)):
            tmp = stacks[source-1].pop()
            print(f'remove {tmp} from {source} to {destination}')
            if d is not None:
                stacks[destination-1].push(d)
    '''
    
    '''
    PROBLEM 2 WITH LIST REVERSE: NLCDCLVMQ
    '''
    
    