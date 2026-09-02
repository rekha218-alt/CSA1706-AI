# Simple Linear SVM

data = [
    ([1, 1], -1),
    ([2, 1], -1),
    ([2, 2], -1),
    ([6, 6], 1),
    ([7, 6], 1),
    ([7, 7], 1)
]

w1 = 0.0
w2 = 0.0
b = 0.0

learning_rate = 0.01

# Training
for epoch in range(1000):

    for point, label in data:

        x1 = point[0]
        x2 = point[1]

        value = label * (w1 * x1 + w2 * x2 + b)

        if value < 1:

            w1 = w1 + learning_rate * label * x1
            w2 = w2 + learning_rate * label * x2
            b = b + learning_rate * label

print("Training completed.")

x1 = float(input("Enter first value: "))
x2 = float(input("Enter second value: "))

result = w1 * x1 + w2 * x2 + b

if result >= 0:
    print("Predicted Class: +1")
else:
    print("Predicted Class: -1")
