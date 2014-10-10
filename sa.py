from abc import ABCMeta, abstractmethod
from random import randint, random, shuffle, uniform
from math import *


#
# TIP of the day -> ndarray for objective function
#

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
    def get_neighbour(self, current):
        # Parameter: a coordinate for current
        #
        # Return: list of neighbours, random or random from current
        #
        pass

    #
    # The Main Loop
    #

    def sa(self, current, goal):
        self.current = current
        while self.temperature > self.temperature_min and current[0] < goal:  # Should also check if goal is reached in a generic condition
            neighbour = self.get_neighbour(self.current)

            # If the neighbour is better change current -> neighbour
            for n in neighbour:
                if n[0] > current[0]:
                    current = n

            # if not, change the current to neighbour only if, the random function hits

            else:
                jump = uniform(0, 1)
                if jump < math.pow(math.e, -(neighbour[0]-self.current[0]) / self.temp):
                    #Jump to random neighbour
                    self.current = shuffle(neighbour)

        return self.current


class State(object):
    n = 5
    m = 5
    k = 2

    def __init__(self, grid=None):
        self.grid = None
        if grid is None:
            self.init_grid()
            self.create_random()
        else:
            self.grid = self.randomize_current(self, grid)

    #
    # Initialize a new empty grid
    #

    def init_grid(self):
        self.grid = [[0 for i in range(self.n)] for j in range(self.m)]

    #
    # Create a new total random state/grid
    #

    def create_random(self):
        pieces_left = 10
        while True:
            rand1 = randint(0, self.n - 1)
            rand2 = randint(0, self.m - 1)

            if self.grid[rand1][rand2] is None:
                self.grid[rand1][rand2] = 1
                pieces_left -= 1
            else:
                self.grid[rand1][rand2] = 0

            if pieces_left == 0:
                break

    #
    # Change the grid/state a litte
    #

    def randomize_current(self, grid):
        new_grid = grid

        has_piece = False

        while True:
            rand1 = randint(0, self.n - 1)
            rand2 = randint(0, self.m - 1)

            if has_piece is False:
                if new_grid[rand1][rand2] is not None:
                    new_grid[rand1][rand2] = None
                    has_piece = True
            else:
                if new_grid[rand1][rand2] is None:
                    new_grid[rand1][rand2] = 'o'
                    break

        return new_grid

    def __str__(self):
        for i in range(len(self.grid)):
            print self.grid[i]


state = State()
print state