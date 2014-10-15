#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        self.board = board.Board(8, 8, 1, self)
        
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
        # Loop untill we find the solution or the temperature goes out
        while True:
            # Check if we are finished
            if self.temperature == 0:
                break
            
            # Calculate score for this sate
            score = self.board.objective_function()
            
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
                neighbour_score = neighbour.objective_function()
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
                
                # Check if we should explore
                if random.random() >  min(0.9, delta):
                    # Explooore
                    self.board = new_node
                    self.current = self.board.get_random_node()
            
            # Decrease temperature
            self.temperature -= 0.1
        self.board.print_pretty()

#
# Check if we should run the script
#

if __name__ == '__main__':
    EggProblem()