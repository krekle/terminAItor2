import board
import random

class EggProblem:
    def __init__(self):
        # Init the board
        self.board = board.Board(5, 5, 1)
        
        # Debug for the shit
        self.board.print_pretty()
        
        # Derp
        self.solve()
    
    def solve(self):
        if self.board.populated is False:
            self.initial_populate()
            
            self.board.print_pretty()
        
    
    def initial_populate(self):
        for pos_x in range(self.board.x):
            generated = 0
            while True:
                if generated == self.board.k:
                    break
                
                pos_y = random.randint(0, self.board.y - 1)
                temp_node = self.board.get_node(pos_x, pos_y)
                
                if temp_node is not None:
                    if temp_node.value is None:
                        temp_node.value = True
                        generated += 1
        
    

EggProblem()