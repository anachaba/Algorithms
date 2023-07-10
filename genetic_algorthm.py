import random

# Genetic Algorithm Parameters
population_size = 50
chromosome_length = 10
mutation_rate = 0.1
generations = 100

# Create an initial population
population = []
for _ in range(population_size):
    chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
    population.append(chromosome)

# Genetic Algorithm
for generation in range(generations):
    # Evaluate the fitness of each individual in the population
    fitness_scores = []
    for chromosome in population:
        # Fitness function - example: count the number of ones in the chromosome
        fitness = sum(chromosome)
        fitness_scores.append(fitness)

    # Select parents for reproduction
    parents = random.choices(population, weights=fitness_scores, k=2)

    # Perform crossover (single-point crossover)
    crossover_point = random.randint(1, chromosome_length - 1)
    child1 = parents[0][:crossover_point] + parents[1][crossover_point:]
    child2 = parents[1][:crossover_point] + parents[0][crossover_point:]

    # Perform mutation
    for i in range(chromosome_length):
        if random.random() < mutation_rate:
            child1[i] = 1 - child1[i]
            child2[i] = 1 - child2[i]

    # Replace some individuals in the population with the new offspring
    population[random.randint(0, population_size - 1)] = child1
    population[random.randint(0, population_size - 1)] = child2

# Print the best individual in the final population
best_individual = max(population, key=lambda chromosome: sum(chromosome))
print("Best Individual:", best_individual)
print("score:",sum(best_individual))
