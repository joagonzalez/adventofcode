a = 10
b = 8

for i in range(0,5):
    print(f'desde outer: {a}')
    a = 0
    for j in range(0,5):
        print('desde inner')
        print(a)
        a += 1