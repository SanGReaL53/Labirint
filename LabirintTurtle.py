class LabirintTurtle():
    def __init__(self):
        self.map = []
        self.turtle = []
        self.exit = 0
        self.exitc = []
        self.labirint111 = []

    def load_map(self, file):
        f = open(file, 'r')
        for line in f:
            if line.startswith(' ') or line.startswith('*'):
                self.map.append(list(line[:-1]))
            else:
                self.turtle.append(int(line))
        self.check_map()

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
        self.labirint111 = self.map

 
 


 
        y=self.turtle[0]
        x=self.turtle[1]
        self.labirint111[y][x]=1 
        for y in range(0, len(self.labirint111)):
            for x in range(0, len(self.labirint111[y])):
                 if self.labirint111[y][x]=='*':
                     self.labirint111[y][x]=''
                 elif self.labirint111[y][x]=='':
                     self.labirint111[y][x]= 0
        
 
 
        for yy in range(0, len(self.labirint111)-1):
            for xx in range(0, len(self.labirint111[yy])-1):
 
                for y in range(0, len(self.labirint111) - 1):
                    for x in range(0, len(self.labirint111[y]) - 1):
                        if labirint111[y][x] != '':
 
                        
                            if self.labirint111[y - 1][x] != '' and self.labirint111[y - 1][x] == 0 and self.labirint111[y][x] != 0:
                                self.labirint111[y - 1][x] = int(self.labirint111[y][x]) + 1
                        
                            if self.labirint111[y][x + 1] != '' and self.labirint111[y][x + 1] == 0 and self.labirint111[y][x] != 0:
                                self.labirint111[y][x + 1] = int(self.labirint111[y][x]) + 1
                        
                            if self.labirint111[y + 1][x] != '' and self.labirint111[y + 1][x] == 0 and self.labirint111[y][x] != 0:
                                self.labirint111[y + 1][x] = int(self.labirint111[y][x]) + 1
                        
                            if self.labirint111[y][x - 1] != '' and self.labirint111[y][x - 1] == 0 and self.labirint111[y][x] != 0:
                                self.labirint111[y][x - 1] = int(self.labirint111[y][x]) + 1
 
 
 

    for y in range(0, len(self.labirint111)):
       for x in range(0, len(self.labirint111[y])):
            if self.labirint111[y][x]=='':
                self.labirint111[y][x]=1

    for y in range(0, len(self.labirint111)):
        print(self.labirint111[y])
    
            
t = LabirintTurtle()
t.load_map('l1.txt')
t.show_map(True)
t.check_map()
print(t.exitc)
