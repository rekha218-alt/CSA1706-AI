import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))


# Get input from user
print("Enter two input values:")
x1 = float(input("X1: "))
x2 = float(input("X2: "))

print("Enter target output:")
target = float(input("Target: "))

# Initial weights
w1 = 0.5
w2 = 0.5
w3 = 0.5
w4 = 0.5

learning_rate = 0.5

# -------- Forward Pass --------

# Hidden layer
h1 = sigmoid(x1 * w1 + x2 * w2)
h2 = sigmoid(x1 * w3 + x2 * w4)

# Output layer
output = sigmoid(h1 + h2)

print("\nOutput before training:", round(output, 4))

# -------- Backpropagation --------

error = target - output

# Output layer delta
delta_output = error * output * (1 - output)

# Update weights
w1 = w1 + learning_rate * delta_output * x1
w2 = w2 + learning_rate * delta_output * x2
w3 = w3 + learning_rate * delta_output * x1
w4 = w4 + learning_rate * delta_output * x2

# -------- Forward Pass Again --------

h1 = sigmoid(x1 * w1 + x2 * w2)
h2 = sigmoid(x1 * w3 + x2 * w4)

output = sigmoid(h1 + h2)

print("Output after training:", round(output, 4))
print("Error:", round(target - output, 4))
