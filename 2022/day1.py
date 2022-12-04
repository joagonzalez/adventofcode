def open_file(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data 

def find_elf(data):
    data = data.split('\n\n')
    max = 0
    count = 0
    
    for elf in data:
        tmp = 0
        count += 1
        for calories in elf.split('\n'):
            try:
                tmp += int(calories)
            except Exception as e:
                print(f'Error: {e}')    
        
        print(f'elf: {count} carry {tmp} calories')
        
        if tmp > max:
            max = tmp
    
    return max    

def find_top_elf(data):
    data = data.split('\n\n')
    l = []
    for elf in data:
        tmp = 0
        for calories in elf.split('\n'):
            try:
                tmp += int(calories) if calories != '' else 0
            except Exception as e:
                print(f'Error: {e}')    
        
        l.append(tmp)
    
    print(f'top elfs: {sorted(l, reverse=True)[:3]}')
        
    return sorted(l, reverse=True)

if __name__ == '__main__':
    data = open_file('day1_input.txt')
    max = find_elf(data=data)
    top = find_top_elf(data=data)
    print(f'max calories: {max}')
    print(f'sum calories of top 3 elfs: {sum(top[:3])}')