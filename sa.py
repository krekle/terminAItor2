from abc import ABCMeta, abstractmethod

#
# Abstract class
#

class SimulatedAnnealing(object):
    
    #
    # Define as an abstract class
    #
    
    __metaclass__ = ABCMeta
    
    #
    # Constructor
    #
    
    def __init__(self):
        # Set temperatur
        self.temperature = 100
        self.temperature_min = 0
        
        # Init nodes
        self.current = None
        self.next = None
    
    #
    # The objective function
    #
    
    @abstractmethod
    def objective_function(self):
        pass
    
    #
    # Return neigbours for the current Node
    #
    
    @abstractmethod
    def get_neighbour(self, neighbour):
        pass