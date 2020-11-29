class LabirintTurtle():
    def __init__(self):
        self.map = []
        self.turtle = []
        self.exit = 0
        self.exitc = []

    def load_map(self, file):
        f = open(file, 'r')
        for line in f:
            if line.startswith(' ') or line.startswith('*'):
                self.map.append(list(line[:-1]))
            else:
                self.turtle.append(int(line))
        check_map(self)

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
                    self.exitc.append(a)
                elif (j == 0 or j == len(self.map[i]) - 1) and self.map[i][j] == ' ':
                    a = []
                    a.append(i)
                    a.append(j)
                    self.exitc.append(a)
            if len(self.exitc) == 0:
                return False
        if self.turtle == []:
            return False
        if self.map[self.turtle[0]][self.turtle[1]] == '*':
            return False
