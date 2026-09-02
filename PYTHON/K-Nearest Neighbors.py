# K-Nearest Neighbors

import math

data = [
    ([1, 2], "A"),
    ([2, 3], "A"),
    ([3, 3], "A"),
    ([6, 7], "B"),
    ([7, 8], "B"),
    ([8, 9], "B")
]

k = 3

x = float(input("Enter first value: "))
y = float(input("Enter second value: "))

new_point = [x, y]

distances = []

for point, label in data:
    distance = math.sqrt(
        (point[0] - new_point[0]) ** 2 +
        (point[1] - new_point[1]) ** 2
    )

    distances.append((distance, label))

# Sort according to distance
distances.sort()

# Take K nearest points
nearest = distances[:k]

count_A = 0
count_B = 0

for distance, label in nearest:
    if label == "A":
        count_A += 1
    else:
        count_B += 1

if count_A > count_B:
    result = "A"
else:
    result = "B"

print("Nearest neighbors:", nearest)
print("Predicted Class:", result)
