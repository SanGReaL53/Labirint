class LabirintTurtle():
    def __init__(self):
        self.map = []
        self.turtle = []
        self.exit = 0
        self.exitc = []
        self.lab = []

    def load_map(self, file):
        try:
            line = 0
            f = open(file, 'r')
            for line in f:
                if line.startswith(' ') or line.startswith('*'):
                    self.map.append(list(line[:-1]))
                else:
                    break
            pos_x = int(line)
            pos_y = int(f.readline())
            self.turtle = [pos_x, pos_y]
            self.check_map()
        except ValueError:
            print('Error')
            self.load_map(input())

    def show_map(self, turtle=None):
        if turtle != None:
            self.map[self.turtle[0]][self.turtle[1]] = 'A'
        for i in range(len(self.map)):
            print(*self.map[i])

    def check_map(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] != 'A' and self.map[i][j] != '*':
                    if self.map[i][j] != ' ':
                        return False
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if (i == 0 or i == len(self.map) - 1) and self.map[i][j] == ' ':
                    a = []
                    a.append(i)
                    a.append(j)
                    if a not in self.exitc:     
                        self.exitc.append(a)
                elif (j == 0 or j == len(self.map[i]) - 1) and self.map[i][j] == ' ':
                    a = []
                    a.append(i)
                    a.append(j)
                    if a not in self.exitc:
                        self.exitc.append(a)
            if len(self.exitc) == 0:
                return False
        if self.turtle == []:
            return False
        if self.map[self.turtle[0]][self.turtle[1]] == '*':
            return False
    def find_way(self):
        self.lab = self.map 
        x = self.turtle[0]
        y = self.turtle[1]
        self.lab[x][y] = 1 
        for i in range(0, len(self.lab)):
            for j in range(0, len(self.lab[i])):
                 if self.lab[i][j] == ' ':
                     self.lab[i][j] = 0
        for i in range(0, len(self.lab) - 1):
            for j in range(0, len(self.lab[i]) - 1):
                for x in range(0, len(self.lab) - 1):
                    for y in range(0, len(self.lab[x]) - 1):
                        if self.lab[x][y] != '*':
                            if self.lab[x - 1][y] != '*' and self.lab[x - 1][y] == 0 and self.lab[x][y] != 0:
                                self.lab[x - 1][y] = int(self.lab[x][y]) + 1
                            if self.lab[x][y + 1] != '*' and self.lab[x][y + 1] == 0 and self.lab[x][y] != 0:
                                self.lab[x][y + 1] = int(self.lab[x][y]) + 1
                            if self.lab[x + 1][y] != '*' and self.lab[x + 1][y] == 0 and self.lab[x][y] != 0:
                                self.lab[x + 1][y] = int(self.lab[x][y]) + 1
                            if self.lab[x][y - 1] != '*' and self.lab[x][y - 1] == 0 and self.lab[x][y] != 0:
                                self.lab[x][y - 1] = int(self.lab[x][y]) + 1
        for i in range(0, len(self.lab)):
            for j in range(0, len(self.lab[i])):
                if self.lab[i][j] == '':
                    self.lab[i][j] = 1
