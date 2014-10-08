#from sa import SimulatedAnnealing
import random

#class Egg(SimulatedAnnealing):
class Egg():
    
    #
    # Constructor
    #
    
    def __init__(self):
        self.board = None
        
        
        self.n = 5
        self.m = 5
        self.k = 2
        self.max_pieces = 10
        
        self.init_board()
        self.set_first_board()
        self.print_board()
    
    def init_board(self):
        self.board = [[None for i in range(self.n)] for j in range(self.m)]
    
    def print_board(self):
        for i in range(len(self.board)):
            print self.board[i]
    
    def set_first_board(self):
        pieces_left = 10
        while True:
            rand1 = random.randint(0, self.n - 1)
            rand2 = random.randint(0, self.m - 1)
            
            if self.board[rand1][rand2] == None:
                self.board[rand1][rand2] = 'o'
                pieces_left -= 1
            
            if pieces_left == 0:
                break
            
        
    
    
    
    
Egg()