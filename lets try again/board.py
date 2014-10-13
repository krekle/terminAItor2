
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
    
    def __init__(self, x, y, k):
        # Set posision and k value
        self.x = x
        self.y = y
        self.k = k
        
        # Populate the board
        self.board = [[node.Node(self) for i in range(x)] for j in range(y)]
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
        # Reset old node
        old_node = self.get_node(pos_x, pos_y)
        old_node.value = None
        
        # Check what way to move
        if direction is 'up':
            pos_y += 1
        else:
            pos_y -= 1
        
        # Get new node
        new_node = self.get_node(pos_x, pos_y)
        new_node.value = True
    
    #
    # Calulcate score
    #
    
    def get_score(self):
        return 5
    
    #
    # Populate the board
    #
    
    def populate(self):
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
                    
                    # Increase number of generated nodes
                    generated += 1
    
    #
    # Returns the first node we can find
    #
    
    def get_start_node(self):
        # Loop x
        for pos_x in range(self.x):
            # Loop y
            for pos_y in range(self.y):
                # Get node at current position
                temp_node = self.get_node(pos_x, pos_y)
                
                # Check the value
                if temp_node.value is not None:
                    # Node is active, return this
                    return temp_node
        
        # This should never happen
        return None
    
    #
    # Debug
    #
    
    def print_pretty(self):
        print "---------------"
        for i in range(self.y):
            print self.board[i]