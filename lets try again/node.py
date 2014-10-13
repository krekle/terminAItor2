

class Node:
    def __init__(self, board):
        self.board = board
        self.value = None
    
    def __repr__(self):
        if self.value is None:
            return ' '
        else:
            return 'o'
        
        #x, y = self.get_pos()
        
        #if x is not None:
        #    return '[' + str(x) + ',' + str(y) + ']'
        #else:
        #    return 'Err'
    
    def get_pos(self):
        for i in range(self.board.y):
            for j in range(self.board.x):
                if self.board.get_node(j, i) == self:
                    return j, i
        
        return None, None
    