from abc import ABCMeta, abstractmethod
from random import randint, random, shuffle, uniform
from math import *
import traceback

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
            neighbours = self.get_neighbour(self.current)

            # If the neighbour is better change current -> neighbour
            for n in neighbours:
                if n[0] > current[0]:
                    current = n

            # if not, change the current to neighbour only if, the random function hits

            else:
                jump = uniform(0, 1)
                if jump < math.pow(math.e, -(neighbour[0]-self.current[0]) / self.temp):
                    #Jump to random neighbour
                    self.current = shuffle(neighbour)

        return self.current

    def reduce_temp(self):
        pass

    #
    # State is an way of easily creating new grid states, either completely new ones or
    # a modified version of a current one
    #


class State(object):

    #
    # Constructor
    #

    def __init__(self, grid=None, n=None, k=None):
        self.cost = 0

        # Setting the size of the grid
        if n is not None and k is not None:
            self.m = n
            self.n = n
            self.k = k
        else:
            self.m = 5
            self.n = 5  # Default n,m = 5 and k = 2
            self.k = 2

        #Creating new grid or modifying current one
        if grid is None:
            self.grid = None
            self.init_grid()
            self.create_random()
        else:
            self.grid = None
            self.grid = self.randomize_current(grid)

        self.diagonals()
        self.cost = self.calculate_score()

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

            if self.grid[rand1][rand2] is 0:
                self.grid[rand1][rand2] = 1
                pieces_left -= 1
            else:
                self.grid[rand1][rand2] = 0
                pieces_left += 1

            if pieces_left == 0:
                break

    #
    # Change the grid/state a little
    #

    def randomize_current(self, grid):
        new_grid = grid

        has_piece = False

        while True:
            rand1 = randint(0, self.n - 1)
            rand2 = randint(0, self.m - 1)

            if has_piece is False:
                if new_grid[rand1][rand2] is not 0:
                    new_grid[rand1][rand2] = 0
                    has_piece = True
            else:
                if new_grid[rand1][rand2] is 0:
                    new_grid[rand1][rand2] = 1
                    break

        return new_grid

    #
    # Method for finding diagonals
    #

    def diagonals(self):

        '''
        :return: two lists of diagonals

        the method add X before an after a line to get diagonals in one coloumn, then zips and removes the X'es

        | 1 | 2 | 3 |      | x | x | 1 | 2 | 3 |
        | 4 | 5 | 6 |  =>  | x | 4 | 5 | 6 | x | each column is now a diagonal, zip it, remove x'es and we're done
        | 7 | 8 | 9 |      | 7 | 8 | 9 | x | x |

        '''


        forward_x = self.n - 1
        backward_x = 0
        left_diag = list()  # \
        right_diag = list()  # /

        for i in range(0, len(self.grid)):
            left_diag.append(['X' for k in range(forward_x)] + self.grid[i] + ['X' for j in range(backward_x)])
            right_diag.append(['X' for h in range(backward_x)] + self.grid[i] + ['X' for g in range(forward_x)])
            forward_x -= 1
            backward_x += 1

        left_diag = zip(*left_diag)
        right_diag = zip(*right_diag)

        for y in range(len(left_diag)):
            left_diag[y] = [x for x in left_diag[y] if x != 'X']
            right_diag[y] = [x for x in right_diag[y] if x != 'X']

        return left_diag, right_diag
    #
    # Calculate the score (aka objective function)
    #

    def calculate_score(self):

        #Highest possible score, should probably be max_score - min_score
        cost = 100

        # Vertical
        for i in range(0, len(self.grid)):
            cost -= abs(sum(self.grid[i]) - self.k)
        # Makes it just as bad to have 1 piece on a row as 3 pieces, might want to reevaluate this

        #Horizontal
        zipped_horizontal = zip(*self.grid)  # * for unpacking list
        for i in range(0, len(zipped_horizontal)):
            cost -= abs(sum(zipped_horizontal[i]) - self.k)
        # Makes it just as bad to have 1 piece on a row as 3 pieces, might want to reevaluate this

        left_diagonal, right_diagonal = self.diagonals()
        # \ Diagonal
        for diag_l in left_diagonal:
            if len(diag_l) >= self.k:
                cost -= sum(diag_l)

        # / Diagonal
        for diag_r in right_diagonal:
            if len(diag_r) >= self.k:
                cost -= sum(diag_r)

        print cost
        return cost

    #
    # Print the grid
    #

    def printer(self):
        for i in range(len(self.grid)):
            print str(self.grid[i])


try:
    state = State(None)
    state.printer()
except:
    traceback.print_exc()
