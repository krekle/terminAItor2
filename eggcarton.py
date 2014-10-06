import numpy as np
import random
import math


class Node:
    def __init__(self, gene, k):
        # The node must contain a cost value
        self.gene = gene
        self.k = k
        self.cost = self.objective_function(gene)

    def random_neighbour(self):
        # generate neighbors
        tmp = np.copy(self.gene)
        np.random.shuffle(tmp[random.random()*tmp.shape[0], :])
        np.random.shuffle(tmp[:, random.random()*tmp.shape[0]])
        return tmp

    def objective_function(self, gene):
        n = gene.shape[0]
        k = self.k
        horizonal = np.sum(gene, axis=1)-k
        vertical = np.sum(gene, axis=0)-k
        diag1 = np.array([
            sum(gene.diagonal(k-n+i))
            for i in xrange(2*(n-k)+1)
                ])-k
        diag2 = np.array([
            sum(np.fliplr(gene).diagonal(k-n+i))
            for i in xrange(2*(n-k)+1)
            ])-k

        return np.sum(horizonal[horizonal>0], axis=0) + \
            np.sum(vertical[vertical>0], axis=0) + \
            np.sum(diag2[diag2>0], axis=0) + \
            np.sum(diag1[diag1>0], axis=0)


def initial_temp(node):
    tmp = np.ones(shape=node.gene.shape, dtype="uint8")
    return float(node.objective_function(tmp))


def dependant_initial_t( temperature,node,neighbor ):
    # Increase the temperature to make this neighbor a very likely choice
    # This function may not decrease the temperature
    x = temperature/(abs(node.cost-neighbor.cost)+1)*math.log1p(100/99)
    return temperature/x if 1 > x > 0 else temperature


def reduce_t( temperature, repetitions):
    # common function for temperatur reduction
    return temperature/math.log(repetitions+2,2)


def sa(start_node, goal_cost, k):
    node = start_node
    d = start_node.gene.shape[0]**2  # number of repetitions pr temperature value
    temperature = initial_temp( node )
    repetitions = 0
    while temperature>1e-100 and node.cost > goal_cost:
        neighbor = Node(node.random_neighbour(), k)  # choose random neigh
        if neighbor.cost < node.cost:
            node = neighbor
        else:
            annealing = random.uniform(0, 1)

            if annealing < math.pow(math.e, -(neighbor.cost-node.cost)/temperature):
                node = neighbor
        repetitions += 1
        if repetitions < d:
            # set a dependant initial temperature
            temperature = dependant_initial_t( temperature,node,neighbor )

        elif repetitions % d is 0:
            temperature = reduce_t( temperature,repetitions )
    #end while
    return node

n=7 # box size
x = 12 # eggs
k = 2
gene = np.array([1]*x+[0]*(int(n**2)-x)).reshape(n,n)
print "Simulated Annealing - (%dx%d) box of %d eggs width k=%d:" % (n,n,x,k)
print sa(Node( gene,k ), goal_cost = 0, k = k).gene