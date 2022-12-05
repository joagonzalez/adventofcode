from day1 import open_file

def analyze_elf(assignment):
    start = int(assignment.split('-')[0])
    end = int(assignment.split('-')[1])
    
    return set([i for i in range(start, end + 1)])


def contains(elf1, elf2):
    _ok = False
    
    if elf1.intersection(elf2) == elf1:
        _ok = True
        
    if elf2.intersection(elf1) == elf2:
        _ok = True
    
    return _ok

def overlap(elf1, elf2):
    _ok = False
    
    if len(elf1.intersection(elf2)) != 0:
        _ok = True
    
    return _ok

def logic(data):
    tmp = []
    overlap_tmp = []
    
    for pair in data:
        if len(pair) != 0:
            print(f'analyzing {pair}')
            elf1 = pair.split(',')[0]
            elf2 = pair.split(',')[1]
            print(f'assignment of elf1 is {elf1} and elf2 is {elf2}')
            
            elf1 = analyze_elf(elf1)
            elf2 = analyze_elf(elf2)
            print(f'assignment of elf1 is {elf1} and elf2 is {elf2} as sets')
            
            if contains(elf1, elf2):
                print(f'assignment is fully contained into the other: {contains(elf1, elf2)}')
                tmp.append(contains(elf1, elf2))
                
            if overlap(elf1=elf1, elf2=elf2):
                print(f'some assignment is partially contained into the other: {contains(elf1, elf2)}')
                overlap_tmp.append(contains(elf1, elf2))
                
    
    return tmp, overlap_tmp
        
if __name__ == '__main__':
    data = open_file('day4_input.txt')
    # print(data.split('\n'))
    
    result, result_overlap = logic(data.split('\n'))
    print(f'Amount of ineficcient assinments: {len(result)}')
    print(f'Amount of non optimal assinments: {len(result_overlap)}')