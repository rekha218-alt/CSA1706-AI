# Alpha-Beta Pruning for Gaming

import math

def alpha_beta(depth, node, maximizing, values, alpha, beta):

    # Leaf node
    if depth == 0:
        return values[node]

    if maximizing:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(depth - 1, node * 2 + i,
                               False, values, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(depth - 1, node * 2 + i,
                               True, values, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta pruning
            if beta <= alpha:
                break

        return best


# Main Program

depth = int(input("Enter depth of game tree: "))

nodes = 2 ** depth
values = []

print("Enter", nodes, "leaf node values:")

for i in range(nodes):
    value = int(input("Leaf " + str(i + 1) + ": "))
    values.append(value)

result = alpha_beta(
    depth, 0, True, values,
    -math.inf, math.inf
)

print("\nBest value for MAX player:", result)
