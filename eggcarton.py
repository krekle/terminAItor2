from sa import SimulatedAnnealing
from random import *
import math


class Egg(SimulatedAnnealing):
    
    #
    # Constructor
    #
    
    def __init__(self):
        # Set max temperature
        self.temperature = 100
        self.temperature_min = 0
        
        # Init nodes
        self.current = 0
        self.next = 0
        
        self.board = None
        
        self.n = 5
        self.m = 5
        self.k = 2
        self.max_pieces = 10
        
        self.debug = 0
        
        self.objective_function()
    
    def init_board(self):
        self.board = [[None for i in range(self.n)] for j in range(self.m)]
    
    def print_board(self, board=None):
        if board is None:
            output_board = self.board
        else:
            output_board = board
        
        for i in range(len(self.board)):
            print output_board[i]
        
    def set_first_board(self):
        pieces_left = 10
        while True:
            rand1 = randint(0, self.n - 1)
            rand2 = randint(0, self.m - 1)
            
            if self.board[rand1][rand2] is None:
                self.board[rand1][rand2] = 'o'
                pieces_left -= 1

            if pieces_left == 0:
                break
    
    def objective_function(self):
        if self.debug == 100:
            return
        
        # Check if we should init the board or handle a pick neighbours
        if self.board is None:
            # No board set, init board
            self.init_board();
            
            # Set pieces
            self.set_first_board()
            
            # Debug
            self.print_board()
            self.current = self.calculate_score(self.board)
            print self.current
        else:
            neighbour = self.get_neighbour(randint(0, 4))
            
            # Debug
            self.print_board(neighbour)
            
            new_value = self.calculate_score(neighbour)
            print new_value
            
            if new_value <= self.current:
                self.current = new_value
                self.board = neighbour
        
        self.debug += 1
        
        # Call self
        self.objective_function()
            

    def calculate_score(self, board):
        score = 0
        
        # Loop horizontally
        for i in range(len(board)):
            horizontal_score = 0
            for j in range(len(board[i])):
                if board[i][j] is 'o':
                    horizontal_score += 1
            score += math.fabs(self.k - horizontal_score)
        print " "
        return score
    
    #
    # Return neigbours for the current Node
    #

    def get_neighbour(self, neighbour):
        # Total random
        for i in range(0, len(self.board)):
            shuffle(self.board[i])
        shuffle(self.board)
        # Not diagonal random. damn.

        return self.generate_change(self.board)
    
    #
    # Method that does minor changes to a board
    #
    
    def generate_change(self, board):
        new_board = board
        
        has_piece = False
        
        while True:
            rand1 = randint(0, self.n - 1)
            rand2 = randint(0, self.m - 1)
            
            if has_piece is False:
                if new_board[rand1][rand2] is not None:
                    new_board[rand1][rand2] = None
                    has_piece = True
            else:
                if new_board[rand1][rand2] is None:
                    new_board[rand1][rand2] = 'o'
                    break
        
        return new_board
    

# Check for abstract class
if __name__ == '__main__':
    print 'Subclass:', issubclass(Egg, SimulatedAnnealing)
    print 'Instance:', isinstance(Egg(), SimulatedAnnealing)
    Egg()
