# Map Coloring using CSP

colors = ["Red", "Green", "Blue"]

# Map connections
graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

color = {}


def is_safe(region, c):
    for neighbor in graph[region]:
        if neighbor in color and color[neighbor] == c:
            return False
    return True


def solve(regions):
    if len(color) == len(regions):
        return True

    region = regions[len(color)]

    for c in colors:
        if is_safe(region, c):
            color[region] = c

            if solve(regions):
                return True

            del color[region]

    return False


regions = list(graph.keys())

if solve(regions):
    print("Map Coloring Solution:")
    for region in regions:
        print(region, "->", color[region])
else:
    print("No solution exists")
