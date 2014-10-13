import copy

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
    
    def is_valid_position(self, direction):
        pos_x, pos_y = self.get_pos()
        
        if direction is 'up':
            pos_y += 1
        else:
            pos_y -= 1
        
        if pos_x >= 0 and pos_x < self.board.x and pos_y >= 0 and pos_y < self.board.y and self.board.get_node(pos_x, pos_y).value is None:
            return True
        else:
            return False
    
    def get_neighbours(self):
        neighbours = []
        
        for y in range(self.board.y):
            for x in range(self.board.x):
                temp_node = self.board.get_node(x, y)
                if temp_node is not None:
                    if temp_node.is_valid_position('up') is True:
                        temp_board1 = copy.deepcopy(self.board)
                        temp_board1.move(x, y, 'up')
                        neighbours.append(temp_board1)
                    
                    if temp_node.is_valid_position('down') is True:
                        temp_board2 = copy.deepcopy(self.board)
                        temp_board2.move(x, y, 'down')
                        neighbours.append(temp_board2)
                    break
        
        return neighbours
    
    def get_score(self):
        cost = 0.5
        
        return cost