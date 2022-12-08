def open_file(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return data 