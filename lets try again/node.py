

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = None
    
    def __repr__(self):
        return '[' + str(self.x) + ',' + str(self.y) + ']'