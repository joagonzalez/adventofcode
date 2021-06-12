def validation(policy, password):
    aux = policy.split(' ')
    letter = aux[1]
    low = int(aux[0].split('-')[0])
    high = int(aux[0].split('-')[1])

    if password.count(letter) <= high and password.count(letter) >= low:
        return True

    return False


def validation_new(policy, password):
    aux = policy.split(' ')
    letter = aux[1]
    pos1 = int(aux[0].split('-')[0]) - 1
    pos2 = int(aux[0].split('-')[1]) - 1

    if (password[pos1] == letter and password[pos2] != letter) or (password[pos1] != letter and password[pos2] == letter):
        return True
    
    return False


def main():
    result = []
    
    f = open('passwords', 'r')

    data = f.readlines()

    for line in data:
        aux = line.split(':')
        policy = aux[0]
        password = aux[1][1:]

        print(f'Policy: {policy}')
        print(f'Password: {password}')
    
        # result.append(validation(policy, password))
        result.append(validation_new(policy, password))
    return result.count(True)


if __name__ == '__main__':
    print(main())