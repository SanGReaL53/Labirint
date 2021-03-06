class LabirintTurtle():
    def __init__(self):
        self.map = []
        self.turtle = []
        self.exit = 0
        self.exitc = []
        self.lab = []
        self.exitn = []
        self.mint = []
        self.maxt = []
        self.miner = ''
        self.maxer = ''

    def load_map(self, file):
        try:
            f = open(file, 'r')
            line = f.readline()
            length = len(line) - 1
            while line.find('*') != -1 or line.find(' ') != -1:
                self.map.append(list(line[:-1]) + (length - len(line[:-1])) * 
                                [" "])
                self.lab.append(list(line[:-1]) + (length - len(line[:-1])) *
                                [" "])
                line = f.readline()
            pos_x = int(line)
            pos_y = int(f.readline())
            self.turtle = [pos_x, pos_y]
            self.check_map()
        except ValueError:
            print('Error')
            self.load_map(input())

    def show_map(self, turtle=None):
        if turtle != None:
            self.map[self.turtle[0]][self.turtle[1]] = chr(128034)
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j], end='\t')
            print()

    def check_map(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] != chr(128034) and self.map[i][j] != '*':
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
        
    def exit_count_step(self):
        self.find_way()
        self.clear = False
        x = self.exitc[0][0]
        y = self.exitc[0][1]
        print(self.lab[x][y] - 1)
    
    def exit_show_step(self):
        self.find_way()
        min_n = 0
        max_n = 0
        for i in self.exitc:
            x = i[0]
            y = i[1]
            self.exitn.append(self.lab[x][y])
        minimal = min(self.exitn)
        maximal = max(self.exitn)
        for i in range(len(self.exitn)):
            if self.exitn[i] == minimal:
                min_n = i
            elif self.exitn[i] == maximal:
                max_n = i
        min_c = self.exitc[min_n]
        max_c = self.exitc[max_n]
        self.map[min_c[0]][min_c[1]] = chr(129462)
        self.map[max_c[0]][max_c[1]] = chr(129462)
        if min_c[0] == 0:
            min_c[0] += 1
            minimal -= 1
            self.miner = 'down'
        elif min_c[0] == len(self.map) - 1:
            min_c[0] -= 1
            minimal -= 1
            self.miner = 'right'
        elif min_c[1] == 0:
            min_c[1] += 1
            minimal -= 1
            self.miner = 'up'
        elif min_c[1] == len(self.map[0]) - 1:
            min_c[1] -= 1
            minimal -= 1
            self.miner = 'left'
        if max_c[0] == 0:
            max_c[0] += 1
            maximal -= 1
            self.maxer = 'down'
        elif max_c[0] == len(self.map) - 1:
            max_c[0] -= 1
            maximal -= 1
            self.maxer = 'right'
        elif max_c[1] == 0:
            max_c[1] += 1
            maximal -= 1
            self.maxer = 'up'
        elif max_c[1] == len(self.map[0]) - 1:
            max_c[1] -= 1
            maximal -= 1
            self.maxer = 'left'
        while min_c != self.turtle:
            if min_c != self.turtle:
                self.map[min_c[0]][min_c[1]] = chr(129462)
                if self.lab[min_c[0] - 1][min_c[1]] == minimal - 1:
                    minimal -= 1
                    min_c[0] -= 1
                    self.mint.append('down')
                elif self.lab[min_c[0]][min_c[1] + 1] == minimal - 1:
                    minimal -= 1
                    min_c[1] += 1
                    self.mint.append('right')
                elif self.lab[min_c[0] + 1][min_c[1]] == minimal - 1:
                    minimal -= 1
                    min_c[0] += 1
                    self.mint.append('up')
                elif self.lab[min_c[0]][min_c[1] - 1] == minimal - 1:
                    minimal -= 1
                    min_c[1] -= 1
                    self.mint.append('left')
        while max_c != self.turtle:
            if max_c != self.turtle:
                self.map[max_c[0]][max_c[1]] = chr(129462)
                if self.lab[max_c[0] - 1][max_c[1]] == maximal - 1:
                    maximal -= 1
                    max_c[0] -= 1
                    self.maxt.append('down')
                elif self.lab[max_c[0]][max_c[1] + 1] == maximal - 1:
                    maximal -= 1
                    max_c[1] += 1
                    self.maxt.append('right')
                elif self.lab[max_c[0] + 1][max_c[1]] == maximal - 1:
                    maximal -= 1
                    max_c[0] += 1
                    self.maxt.append('up')
                elif self.lab[max_c[0]][max_c[1] - 1] == maximal - 1:
                    maximal -= 1
                    max_c[1] -= 1
                    self.maxt.append('left')
        self.lab[self.turtle[0]][self.turtle[1]] = chr(129462)
        self.mint.append(self.miner)
        self.maxt.append(self.maxer)
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                print(self.map[i][j], end='\t')
            print()
        for i in range(len(self.mint) - 1):
            print(self.mint[len(self.mint) - 1 - i], end="->")
        print(self.mint[0])
        for i in range(len(self.maxt) - 1):
            print(self.maxt[len(self.maxt) - 1 - i], end="->")
        print(self.maxt[0])
