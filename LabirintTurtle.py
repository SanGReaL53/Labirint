class LabirintTurtle():
    def __init__(self):
        self.map = []
        self.turtle = []
    def load_map(self, file):
        f = open(file, 'r')
        for line in f:
            if line.startswith(' ') or line.startswith('*'):
                self.map.append(line.strip())
            else:
                self.turtle.append(int(line))
        print(self.map, self.turtle)
t = LabirintTurtle()
t.load_map('l1.txt')
        

        
