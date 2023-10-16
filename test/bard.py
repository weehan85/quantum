import dimod
import numpy as np

distance_matrix = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

qubo = {}
for i in range(4):
    for j in range(4):
        if i != j:
            qubo[(i, j)] = -distance_matrix[i, j]



exactsolver = dimod.ExactSolver()

#sampleset = solver.sample_qubo(qubo)

# Get the sample with the lowest energy.

#best_sample = sampleset.samples[np.argmin([dimod.energy(sample) for sample in sampleset.samples]) if sampleset.energies is None else np.argmin(sampleset.energies)]


bqm = dimod.BinaryQuadraticModel.from_qubo(qubo,offset=0)

results = exactsolver.sample(bqm)


for smpl, energy in results.data(['sample', 'energy']):
    print(smpl, energy)


#tsp_tour = []
#for city in range(4):
#    tsp_tour.append(best_sample[city])

#print(tsp_tour)