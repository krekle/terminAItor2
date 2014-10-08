from sa import SimulatedAnnealing
import random

class Egg(SimulatedAnnealing):
    
    #
    # Constructor
    #
    
    def __init__(self):
        # Set max temperatur
        self.temperature = 100
        self.temperature_min = 0
        
        # Init nodes
        self.current = None
        self.next = None
        
        self.board = None
        
        self.n = 5
        self.m = 5
        self.k = 2
        self.max_pieces = 10
        
        self.objective_function()
    
    def init_board(self):
        self.board = [[None for i in range(self.n)] for j in range(self.m)]
    
    def print_board(self, board = None):
        if board is None:
            output_board = self.board
        else:
            output_board = board
        
        for i in range(len(self.board)):
            print output_board[i]
        
        print " "
        
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
            
        
    
    def objective_function(self):
        # Check if we should init the board or handle a pick neighbours
        if self.board is None:
            # No board set, init board
            self.init_board();
            
            # Set pieces
            self.set_first_board()
            
            # Debug
            self.print_board()
            
            # Call self
            self.objective_function()
        else:
            neighbour = self.get_neighbour(random.randint(0, 4))
            
            # Debug
            self.print_board(neighbour)
            
        
    
    #
    # Return neigbours for the current Node
    #
    
    def get_neighbour(self, neighbour):
        return self.generate_change(self.board)
    
    #
    # Method that does minor changes to a board
    #
    
    def generate_change(self, board):
        new_board = board
        
        has_piece = False
        
        while True:
            rand1 = random.randint(0, self.n - 1)
            rand2 = random.randint(0, self.m - 1)
            
            if has_piece is False:
                if new_board[rand1][rand2] is not None:
                    new_board[rand1][rand2] = None
                    has_piece = True
            else:
                if new_board[rand1][rand2] is None:
                    new_board[rand1][rand2] = 'o'
                    break
        
        return new_board
    
    
    
Egg()