
#
# Imports
#

import board
import math
import random
import copy

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
        self.temperature_max = 100
        self.temperature = 100
        
        # Init the board
        self.board = board.Board(5, 5, 2, self)
        
        # Get start node
        self.current = self.board.get_random_node()
        
        # Debug for the shit
        #self.board.print_pretty()
        
        # Solve the problem
        self.solve()
    
    #
    # Function that solved the actual problem
    #
    
    def solve(self):
        tries = 0
        # Loop untill we find the solution or the temperature goes out
        while True:
            tries += 1
            if tries % 1010000:
                print self.current.get_score()
                self.board.print_pretty()
            
            if self.temperature == 0:
                break
            
            # Calculate score for this sate
            score = self.board.get_score()
            
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
                neighbour_score = neighbour.get_score()
                if neighbour_score >= highest_neighbour_score:
                    new_node = neighbour
                    highest_neighbour_score = neighbour_score
                
            # Check if better
            if highest_neighbour_score > score:
                self.board = new_node
                self.current = self.board.get_random_node()
            else:
                # Check if we should explore!
                delta = math.exp(((highest_neighbour_score - score) / score) / self.temperature)
                print str(highest_neighbour_score) + " - " + str(delta)
                if random.random() >  min(0.9, delta):
                    # Explooore
                    self.board = new_node
                    self.current = self.board.get_random_node()
            
            # Decrease temperature
            self.temperature -= 0.1
        self.board.print_pretty()

#
# Main class
#

def main():
    EggProblem()


#
# Gogo
#

main()