# Linear Regression

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

n = len(x)

sum_x = sum(x)
sum_y = sum(y)

sum_xy = 0
sum_x2 = 0

for i in range(n):
    sum_xy += x[i] * y[i]
    sum_x2 += x[i] * x[i]

# Calculate slope
m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)

# Calculate intercept
c = (sum_y - m * sum_x) / n

print("Linear Regression Equation:")
print("y =", round(m, 2), "* x +", round(c, 2))

value = float(input("Enter X value: "))

prediction = m * value + c

print("Predicted Y value:", prediction)
