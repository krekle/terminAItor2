"""
Abstract pseudocode, general idea
"""


class Node:

    def __init__(self, gene):
    # The node must contain a cost value
        self.gene = gene
        self.cost = self.objective_function( gene )

    def random_neighbour(self):
        # **IMPLEMENT**
        # generate neighbors
        """
        We only care about pseudo generating the neighbors,
        since we are going to pick just one of them. Thus
        we only need to perform a "small" random alteration
        to the parent.
        """
        return neighbor

    def objective_function(self, gene ):
        # **IMPLEMENT**
        # evaluate this state
        return evaluation




def initial_temp( node ):
    """
    f.ex upper bound on (max cost - min cost)
    The example below belongs to the Egg Box exercise.
    Returns the maximum cost possible by putting an egg in each
    of the availible spots.
    """
    tmp = np.ones(shape=node.gene.shape,dtype="uint8")
    return float(node.objective_function( tmp ))

def dependant_initial_t( temperature,node,neighbor ):
    """
    Increase the temperature to make this neighbor a very likely choice.
    This helps us to "correct" the initial temperature if it was initially
    too low.
    This function may not decrease the temperature.
    """
    x = temperature/(abs(node.cost-neighbor.cost)+1)*math.log1p(100/99)
    return temperature/x if 1>x>0 else temperature

def reduce_t( temperature,repetitions ):
    """
    common function for temperatur reduction
    """
    return temperature/math.log(repetitions+2,2)

def sa( start_node, goal_cost ):
    """
    d : # of repetitions pr temperature value
    This should initially be set to something like the size( neighborhood )
    but since we're only generating a single neighbor, we're forced to
    approximate.
    """
    node = start_node
    d = start_node.gene.shape[0]**2 # number of repetitions pr temperature value
    temperature = initial_temp( node )
    repetitions = 0
    while temperature>1e-100 and node.cost > goal_cost:
        neighbor = Node( node.random_neighbor(),k ) # choose random neigh
        if neighbor.cost < node.cost:
            node = neighbor
        else:
            annealing = random.uniform(0,1)
            if annealing < math.pow(math.e,-(neighbor.cost-node.cost)/temperature):
            """
            A stochastic evaluation for checking it its time to perform the
            annealing.
            """
            node = neighbor
            repetitions += 1

        if repetitions<d:
            # set a dependant initial temperature
            # we enter this clause during the first couple of runs
            temperature = dependant_initial_t( temperature,node,neighbor )
        elif repetitions%d==0:
            # and then we enter this clause occationally afterwards.
            temperature = reduce_t( temperature,repetitions )
            #end while
    return node