from math import prod

class Excercise():
    MAP = []
    HEIGHT = 323
    WIDTH = 31
    RIGHT_SLOPE = [1, 3, 5, 7, 1]
    BOTTOM_SLOPE = [1, 1, 1, 1, 2]
    RESULT = []


    def __init__(self):
        self.read_map()

        for i in range(len(self.RIGHT_SLOPE)):
            result = self.count_trees(self.RIGHT_SLOPE[i], self.BOTTOM_SLOPE[i])
            self.RESULT.append(result)
            print(f'Amount of trees for ({self.RIGHT_SLOPE[i]}, {self.BOTTOM_SLOPE[i]}) in path: {result}')

        print(f'Result: {self.RESULT} - Product: {prod(self.RESULT)}')


    def read_map(self):
        f = open('map', 'r')

        data = f.readlines()

        self.MAP = [line.strip() for line in data]

        i = 0
        for line in self.MAP:
            self.MAP[i] = self.MAP[i] * (self.WIDTH * 4 +1)
            i += 1

        print(f'Height of map: {len(self.MAP)}\nWidth of map: {len(self.MAP[0])}')

    def get_map(self):
        return self.MAP


    def print_map(self):
        for line in self.MAP:
            print(line)


    def is_tree(self, y_position, x_position):
        # print(f'Checking if is tree for (x,y)=({x_position+1},{y_position+1})...')
        if self.MAP[y_position][x_position] == '#':
            # self.MAP[y_position] = self.MAP[y_position][:x_position] + 'X' + self.MAP[y_position][x_position+1] 
            # print('Aqui hay un arbol!')
            return 1
        else:
            return 0


    def count_trees(self, slope_right, slope_bottom):
        TREES = 0
        Y_POS = 1
        X_POS = 0

        for row in self.get_map():
            if Y_POS < self.HEIGHT:
                if Y_POS % slope_bottom == 0: # in case slope != 1
                    X_POS = X_POS + slope_right            
                    TREES = TREES + self.is_tree(Y_POS, X_POS) 
            Y_POS += 1
                
        return TREES


if __name__ == '__main__':
    app = Excercise()