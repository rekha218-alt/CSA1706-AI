from itertools import permutations

graph = [
[0,10,15,20],
[10,0,35,25],
[15,35,0,30],
[20,25,30,0]
]

cities = [1,2,3]

min_cost = 9999

best_path = ()

for path in permutations(cities):

    cost = 0

    k = 0

    for city in path:

        cost += graph[k][city]

        k = city

    cost += graph[k][0]

    if cost < min_cost:

        min_cost = cost

        best_path = path

print("Minimum Cost =",min_cost)

print("Path = 0",end=" ")

for city in best_path:

    print("->",city,end=" ")

print("-> 0")
