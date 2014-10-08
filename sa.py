from abc import ABCMeta, abstractmethod


class SimulatedAnnealing(object):

    __metaclass__ = ABCMeta

    def __init__(self, temp=100):
        self.list = ()   # [score, unique type(grid)]
        self.temperature = temp

    def get_best_scores(self):
        return self.list.sort(key=lambda x: x[0])

    @abstractmethod
    def objective_function(self, current):
        pass

    @abstractmethod
    def get_neighbour(self, neighbour):
        #n = number of neighbours
        pass

    @abstractmethod
    def sa(self):
        pass