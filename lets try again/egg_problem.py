
#
# Imports
#

import board

'''
EggProblem
Class for the Egg problem
'''

class EggProblem:
    
    #
    # Constructor
    #
    
    def __init__(self):
        # Set temperature
        self.tempreature = 1000
        
        # Init the board
        self.board = board.Board(5, 5, 1)
        
        # Get start node
        self.current = self.board.get_start_node()
        
        # Debug for the shit
        self.board.print_pretty()
        
        # Solve the problem
        self.solve()
    
    #
    # Function that solved the actual problem
    #
    
    def solve(self):
        # Loop untill we find the solution or the temperature goes out
        while True:
            # Calculate score for this sate
            score = self.current.get_score()
            
            # Check if the optimal solution has been found
            if score >= 1.0:
                # We have solved it!
                break
            
            # Generate the neighbours for this state
            neighbours = self.current.get_neighbours()
            
            # Some variables to keep track of what state to chose
            new_node = None
            highest_neighbour_score = 0
            
            # Find the state neighbour with the highest score
            for neighbour in neighbours:
                neighbour.print_pretty()
                neighbour_score = neighbour.get_score()
                if neighbour_score > highest_neighbour_score:
                    new_node = neighbour
                    highest_neighbour_score = neighbour_score
            
            # Debug
            break
        

#
# Main class
#

def main():
    EggProblem()


#
# Gogo
#

main()