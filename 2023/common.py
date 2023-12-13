def load_file(filename: str = '') -> list:
    f = open(filename, 'r')
    
    return f.readlines()
    
    