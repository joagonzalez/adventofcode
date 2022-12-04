from day1 import open_file

intersections = []
groups = {}

def result():
    for element in intersections:
        print(element) 
    return sum(intersections)
        
def logic(data):
    for rucksuck in data:
        print(f'rucksuck: {rucksuck} of size: {len(rucksuck)}')
        
        lower = rucksuck[:int(len(rucksuck)/2)]
        upper = rucksuck[int(len(rucksuck)/2):]
        
        print(lower)
        print(upper)

        lower = set(lower)
        upper = set(upper)
        
        tmp = lower.intersection(upper)
        tmp = ''.join(tmp)
        
        print(f'intersection: {lower.intersection(upper)}')
        intersections.append(ord(tmp) - 96 if tmp.islower() else ord(tmp) - 38)
        
def logic_part_two(data):
    i = 0
    group = 1
    aux = []
    for rucksuck in data:
        i += 1        
        print(f'rucksuck: {rucksuck} of size: {len(rucksuck)}')
        aux.append(rucksuck)
    
        if i % 3 == 0:
            print(f'group {group} of elements {aux}')
            group += 1          
            tmp = set(aux[0]).intersection(set(aux[1]), set(aux[2]))
            tmp = ''.join(tmp)  
            
            print(f'intersection: {tmp}')
            intersections.append(ord(tmp) - 96 if tmp.islower() else ord(tmp) - 38)
            aux = []
    
     
if __name__ == '__main__':
    filename = 'day3_input.txt'
    data = open_file(filename)
    
    # print(data)
    # logic(data=data.split('\n'))
    logic_part_two(data=data.split('\n'))
    print(result())