#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Imports
#

import node
import random

'''
Board

Class that keeps track of the posision of all the nodes
'''

class Board:
    
    #
    # Constructor
    #
    
    def __init__(self, x, y, k, solver):
        # Reference to solver
        self.solver = solver
        
        # Set posision and k value
        self.x = x
        self.y = y
        self.k = k
        
        self.active_nodes = []
        
        # Populate the board
        self.populate()
    
    #
    # Get node at a given position
    #
    
    def get_node(self, node_x, node_y):
        # Check if valid position
        if node_x >= 0 and node_x < self.x and node_y >= 0 and node_y < self.y:
            # Valid position, return node
            return self.board[node_y][node_x]
        else:
            # Not valid, return false
            return None
    
    #
    # Move a active node up or down
    #
    
    def move(self, pos_x, pos_y, direction):
        # Remove active nodes
        self.active_nodes = []
        
        # Reset old node
        old_node = self.get_node(pos_x, pos_y)
        old_node.value = None
        
        # Check what way to move
        if direction is 'up':
            pos_y -= 1
        else:
            pos_y += 1
        
        # Get new node
        new_node = self.get_node(pos_x, pos_y)
        new_node.value = True
    
    #
    # Calulcate score
    #
    
    def objective_function(self):
        # Storing the score here
        score = 0
        
        # Lists for all the values
        list_x = [0 for i in range(self.x)]
        list_y = [0 for i in range(self.x)]
        list_diagonal_left = [0 for i in range(self.x + self.y - 1)]
        list_diagonal_right = [0 for i in range(self.x + self.y - 1)]
        
        # Populate position lists
        for x in range(self.x):
            for y in range(self.y):
                if self.get_node(x, y).value is not None:
                    self.active_nodes.append(self.get_node(x, y))
                    list_x[x] += 1
                    list_y[y] += 1
                    
                    list_diagonal_left[x + y] += 1
                    list_diagonal_right[self.x - x + y - 1] += 1
        
        # Check position lists against 
        for x in range(self.x):
            for y in range(self.y):
                if self.get_node(x, y).value is not None:
                    if list_x[x] <= self.k and list_y[y] <= self.k and \
                       list_diagonal_left[x + y] <= self.k and \
                       list_diagonal_right[self.x - x + y - 1] <= self.k:
                        score += 1
        
        # Return score
        return score / float(self.x * self.k)
    
    #
    # Populate the board
    #
    
    def populate(self):
        # Create empty matrix for nodes
        self.board = [[node.Node(self) for i in range(self.x)] for j in range(self.y)]
        
        # Loop each column
        for pos_x in range(self.x):
            # Score how many we have generate for this column
            generated = 0
            
            # While true because we might generate nodes that are placed over other
            while True:
                # Check if we have generated all the nodes we need
                if generated == self.k:
                    # We have, break
                    break
                
                # Generate a random y position
                pos_y = random.randint(0, self.y - 1)
                
                # Get node at this position
                temp_node = self.get_node(pos_x, pos_y)
                
                # Check current value
                if temp_node.value is None:
                    # Not already active, activate
                    temp_node.value = True
                    
                    # Add to list
                    self.active_nodes.append(temp_node)
                    
                    # Increase number of generated nodes
                    generated += 1
    
    #
    # Returns the first node we can find
    #
    
    def get_random_node(self):
        if len(self.active_nodes) == 0:
            self.objective_function()
        
        return random.choice(self.active_nodes)
    
    #
    # Debug
    #
    
    def print_pretty(self):
        
        for i in range(self.y):
            print self.board[i]
        print " "