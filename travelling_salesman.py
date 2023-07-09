import numpy as np

def nearest_neighbor(graph, start_city):
    num_cities = len(graph)
    unvisited_cities = set(range(num_cities))
    unvisited_cities.remove(start_city)
    current_city = start_city
    tour = [current_city]

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: graph[current_city][city])
        unvisited_cities.remove(next_city)
        tour.append(next_city)
        current_city = next_city

    return tour

graph = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

start_city = 0  
num_cities = len(graph)  

# using the Nearest Neighbor algorithm
tour = nearest_neighbor(graph, start_city)


print("Tour:", tour)
total_distance = sum(graph[tour[i]][tour[(i + 1) % num_cities]] for i in range(num_cities))
print("Total Distance:", total_distance)

