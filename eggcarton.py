#from sa import SimulatedAnnealing

#class Egg(SimulatedAnnealing):
class Egg():
    
    #
    # Constructor
    #
    
    def __init__(self):
        self.board = None
        
        
        self.n = 5
        self.m = 5
        
        self.init_board()
    
    def init_board(self):
        self.board = [[None for i in range(self.n)] for j in range(self.m)]
        self.print_board()
    
    def print_board(self):
        for i in range(len(self.board)):
            print self.board[i]
    
    
    def set_first_board(self):
        pass
        
    
    
    
    
Egg()