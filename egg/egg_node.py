#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Imports
#

import copy
import random
import egg_board

'''
Node

One Node on the board
'''

class EggNode:
    
    #
    # Constructor
    #
    
    def __init__(self, board):
        self.board = board
        self.value = None
    
    #
    # toString()
    #
    
    def __repr__(self):
        if self.value is None:
            return 'o'
        else:
            return '\033[91mx\033[0m'
    
    #
    # Returns the position for this node (in a hackyyy way)
    #
    
    def get_pos(self):
        # Loop y
        for y in range(self.board.y):
            # Loop x
            for x in range(self.board.x):
                # Check if current node is self
                if self.board.get_node(y, x) == self:
                    # This is the correct node, return pos
                    return y, x
        
        # This node has no positions? WTF
        return None, None
    
    #
    # Check if move up/down is valid for this
    #
    
    def is_valid_position(self, direction):
        # Get current position
        pos_x, pos_y = self.get_pos()
        
        # Check what direction to move
        if direction is 'up':
            pos_y -= 1
        else:
            pos_y += 1
        
        # Check if desiered move is valid
        if pos_x >= 0 and pos_x < self.board.x and pos_y >= 0 and pos_y < self.board.y and self.board.get_node(pos_x, pos_y).value is None:
            # Valid, yolo
            return True
        else:
            # Not valid
            return False
    
    #
    # Generate a life of neighbours for this node
    #
    
    def get_neighbours(self):
        # Store in this array
        neighbours = []
         
        # Loop y
        for y in range(self.board.y):
            # Loop x
            for x in range(self.board.x):
                # Get node at current position
                temp_node = self.board.get_node(x, y)
                
                # Only keep going if the current node is active
                if temp_node is not None and temp_node is not self and temp_node.value is not None:
                    
                    # Check if generate random
                    if (random.uniform(0, 0.90) < (self.board.solver.temperature / self.board.solver.temperature_max)):
                        temp_board = egg_board.EggBoard(self.board.x, self.board.y, self.board.k, self.board.solver)
                        neighbours.append(temp_board)
                    else:
                        # Active, check up move
                        if temp_node.is_valid_position('up') is True:
                            # Up move is valid, add to array
                            temp_board1 = copy.deepcopy(self.board)
                            temp_board1.move(x, y, 'up')
                            neighbours.append(temp_board1)
                        
                        # Check down move
                        if temp_node.is_valid_position('down') is True:
                            # Down move is valid, add to array
                            temp_board2 = copy.deepcopy(self.board)
                            temp_board2.move(x, y, 'down')
                            neighbours.append(temp_board2)
        
        # Return list
        return neighbours
    
    #
    # Return the score
    #
    
    def objective_function(self):
        # We just call the method implemented in board
        return self.board.objective_function()