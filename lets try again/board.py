
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
        
        # Populate the board with empty nodes
        self.board = [[node.Node(self) for i in range(x)] for j in range(y)]
        self.populate()
    
    def get_node(self, node_x, node_y):
        if node_x >= 0 and node_x < self.x and node_y >= 0 and node_y < self.y:
            return self.board[node_y][node_x]
        else:
            return None
    
    def move(self, pos_x, pos_y, direction):
        old_node = self.get_node(pos_x, pos_y)
        
        if old_node is not None:
            old_node.value = None
            
        if direction is 'up':
            pos_y += 1
        else:
            pos_y -= 1
        
        new_node = self.get_node(pos_x, pos_y)
        
        if new_node is not None:
            new_node.value = True
    
    def get_score(self):
        return 5
    
    
    def populate(self):
        for pos_x in range(self.x):
            generated = 0
            while True:
                if generated == self.k:
                    break
                
                pos_y = random.randint(0, self.y - 1)
                temp_node = self.get_node(pos_x, pos_y)
                
                if temp_node.value is None:
                    temp_node.value = True
                    generated += 1
    
    def get_start_node(self):
        for pos_x in range(self.x):
            for pos_y in range(self.y):
                temp_node = self.get_node(pos_x, pos_y)
                if temp_node.value is not None:
                    return temp_node
        return None
    
    
    def print_pretty(self):
        print "---------------"
        for i in range(self.y):
            print self.board[i]
        
    