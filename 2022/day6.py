from common.general import open_file


def equal(slice):
    _ok = False
    
    for char in slice:
        if slice.count(char) != 0:
            _ok = True
            
    return _ok
            
def marker(message):
    start = 0
    end = 0
    slice = 4
    size = int(len(message)/slice)
    result = None
    
    print(f'Analyze message: {message} - Slices: {size} - Message len: {len(message)}')
    
    for i in range(size+1):
        start = slice*i if slice*i == 0 else slice*i-1
        end = slice if i*slice == 0 else i*slice+slice-1
        
        print(f'slice {i} - slice window: {start}:{end} - characters: {message[start:end]}') 
           
        if not equal(message[start:end]):
            result = i
            break
    
    print(f'marker found in slice {result} - marker: {message[start:end]}')

def run_logic(data):
    result = []
    for message in data:
        result.append(marker(message))
        
    return result

if __name__ == '__main__':
    data = open_file(filename='test.txt').split('\n')
    result = run_logic(data=data)
    