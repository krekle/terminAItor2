#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Imports
#

import egg_board
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
        
        # Variables
        self.m = None
        self.k = None
        
        # Ask user what to solve
        self.ask()
    
    #
    # Ask user what to solve
    #
    
    def ask(self):
        # Keep track of stuff
        has_m = False
        has_k = False
        
        # Loop 'till user has inputted stuff
        while True:
            # Check if we are done
            if has_m and has_k:
                # Done!
                break
            else:
                # Avoid exceptions
                try:
                    # Ask user
                    if not has_m:
                        ipt = str(input("Enter m and n value: "))
                    else:
                        ipt = str(input("Enter k value: "))
                    
                    # Try to parse
                    val = int(ipt)
                    
                    # Update value
                    if not has_m:
                        self.m = val
                        has_m = True
                    else:
                        self.k = val
                        has_k = True
                except Exception:
                    pass
        
        # Gogo
        self.prepare()
    
    
    #
    # Prepare
    #
    
    def prepare(self):
        # Init the board
        self.board = egg_board.EggBoard(self.m, self.m, self.k, self)
        
        # Get start node
        self.current = self.board.get_random_node()
        
        # Print first board
        self.board.print_pretty()
        
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
                self.board.print_pretty()
                print "Finished!"
                
                # Break loop
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
                # Set new info
                self.board = new_node
                self.current = self.board.get_random_node()
                
                # Print
                self.board.print_pretty()
            else:
                # Check if we are about to divide on zero
                if score <= 0.0001:
                    score = 0.01
                
                # Check if we should explore!
                delta = math.exp(((highest_neighbour_score - score) / score) / self.temperature)
                
                # Check if we should explore
                if random.random() >  min(0.9, delta):
                    # Explooore
                    self.board = new_node
                    self.current = self.board.get_random_node()
                    
                    # Print
                    self.board.print_pretty()
            
            # Decrease temperature
            self.temperature -= 0.1
        
        # Check if we solved it or not
        score = self.board.objective_function()
        if score < 1.0:
            # Did not solve it
            print "Did not finish"
            print "Optimal score was: " + str(score)


#
# Check if we should run the script
#

if __name__ == '__main__':
    EggProblem()