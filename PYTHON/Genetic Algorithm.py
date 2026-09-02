# Genetic Algorithm

import random

def fitness(x):
    return x * x

# Initial population
population = []

for i in range(6):
    population.append(random.randint(0, 31))

print("Initial Population:")
print(population)

for generation in range(10):

    # Sort according to fitness
    population.sort(key=fitness, reverse=True)

    # Select two best individuals
    parent1 = population[0]
    parent2 = population[1]

    new_population = [parent1, parent2]

    # Create new children
    while len(new_population) < 6:

        parent = random.choice([parent1, parent2])

        mutation = random.randint(-2, 2)

        child = parent + mutation

        if child < 0:
            child = 0

        if child > 31:
            child = 31

        new_population.append(child)

    population = new_population

# Find best solution
best = population[0]

print()
print("Best Value:", best)
print("Maximum Fitness:", fitness(best))
