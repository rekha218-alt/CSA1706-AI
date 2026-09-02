# Simple PCA

import math

data = [
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7]
]

rows = len(data)
cols = len(data[0])

# Find mean
mean = []

for j in range(cols):

    total = 0

    for i in range(rows):
        total += data[i][j]

    mean.append(total / rows)

# Center the data
centered = []

for i in range(rows):

    row = []

    for j in range(cols):
        row.append(data[i][j] - mean[j])

    centered.append(row)

# For this simple dataset, use the direction (1,1)
# as the first principal component.

pc1 = [1 / math.sqrt(2), 1 / math.sqrt(2)]

print("Original Data:")
for row in data:
    print(row)

print("\nReduced Data:")

for row in centered:

    value = row[0] * pc1[0] + row[1] * pc1[1]

    print(round(value, 2))
