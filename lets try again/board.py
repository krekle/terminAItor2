import node

class Board:
    def __init__(self, x, y, k):
        self.x = x
        self.y = y
        self.k = k
        self.board = [[node.Node(self) for i in range(x)] for j in range(y)]
        self.populated = False
    
    def get_node(self, node_x, node_y):
        if node_x >= 0 and node_x < self.x and node_y >= 0 and node_y < self.y:
            return self.board[node_y][node_x]
        else:
            return None
    
    def set_node(self, node, pos_x, pos_y):
        if pos_x >= 0 and pos_x < self.x and pos_y >= 0 and pos_y < self.y:
            self.board[y][x] = node
    
    
    def print_pretty(self):
        print "---------------"
        for i in range(self.y):
            print self.board[i]
        
    