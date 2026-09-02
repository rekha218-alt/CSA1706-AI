# Minimax Algorithm with User Input

def minimax(values, isMax):

    # Base case
    if len(values) == 1:
        return values[0]

    temp = []

    # Compare values in pairs
    for i in range(0, len(values), 2):

        if isMax:
            temp.append(max(values[i], values[i + 1]))
        else:
            temp.append(min(values[i], values[i + 1]))

    # Display current level
    if isMax:
        print("Max Level :", temp)
    else:
        print("Min Level :", temp)

    # Recursive call
    return minimax(temp, not isMax)


# Main Program

n = int(input("Enter number of leaf nodes (Power of 2): "))

values = []

print("Enter the leaf node values:")

for i in range(n):
    value = int(input(f"Value {i+1}: "))
    values.append(value)

print("\nLeaf Nodes:", values)

answer = minimax(values, True)

print("\nOptimal Value =", answer)
