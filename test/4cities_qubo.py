import dimod

import itertools

from collections import defaultdict

from dwave_networkx.utils import binary_quadratic_model_sampler

exactsolver = dimod.ExactSolver()

## Q = {(0, 0): 1, (3, 3): 1, (0,1): -2, (1,2): 2, (2,3): -2}

##Q = {(0, 0): 1, (1, 1): 1, (2,2): 1, (3,3): 1, (0,1): 10, (1,2): 30, (2,3): 50, (3,1): 30, (0,2): 20, (1,3): 30} 

#Q = {(0,1): 10, (1,2): 30, (2,3): 50, (3,1): 30, (0,2): 20, (1,3): 30} 
# Define the binary variables
variables = [0, 1, 2, 3]

# Define the quadratic cost function
qubo = {}
qubo[(0, 1)] = 10
qubo[(1, 2)] = 30
qubo[(2, 3)] = 50
qubo[(3, 0)] = 30
qubo[(0, 2)] = 20
qubo[(1, 3)] = 30


bqm = dimod.BinaryQuadraticModel.from_qubo(qubo,offset=0)

results = exactsolver.sample(bqm)
#results = sampler.sample_qubo(bqm)


for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)
