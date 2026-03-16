import numpy as np
import matplotlib.pyplot as plt

# this function calculates the final optimal values for m (slope) and b (bias or y-intercept) using gredient descent (partial derivatives)
def gradient_descent(curr_m, curr_b, points, learning_rate):
  m_g = 0
  b_g = 0

  n = len(points)
  for i in range(n):
    x = points[i, 0] # the independent variable
    y = points[i, 1] # the dependent variable

    m_g += -(2/n) * x * (y - (curr_m * x + curr_b)) # partial derivative of error by m "slope"
    b_g += -(2/n) * (y - (curr_m * x + curr_b)) # partial derivative of error by b "bias or y-intercept"

  # final m
  m = curr_m - (learning_rate * m_g)
  # final b
  b = curr_b - (learning_rate * b_g)

  return m,b

# Generate some sample data for testing the function
x_values = np.random.rand(100) * 10 # 100 random x values between 0 and 10
y_values = 2 * x_values + 5 + np.random.randn(100) * 2
data = np.column_stack((x_values, y_values)) # Combine x and y into a 2D array

# initializations before executing the function
m = 0
b = 0
learning_rate = 0.0001
iterations = 300

for i in range(iterations):
  m, b = gradient_descent(m, b, data, learning_rate)

print(f"End of {iterations} iterations:")
print(f"Optimal m: {m}")
print(f"Optimal b: {b}")

# Evaluating model performance by calculating mean square error
from sklearn.metrics import mean_squared_error

y_predicted = m * data[:, 0] + b
mse = mean_squared_error(data[:, 1], y_predicted)

print(f"Mean Squared Error: {mse}")

# Visualizing the result:
# visualizing the data points ->
plt.scatter(data[:, 0], data[:, 1], color="black", label="Data Points")

# visualizing the regression line ->
min_x_val = np.min(data[:, 0])
max_x_val = np.max(data[:, 0])
x_line = np.linspace(min_x_val, max_x_val, 100)
y_line = m * x_line + b
plt.plot(x_line, y_line, color="red", label="Regression Line")

plt.title("Linear Regression with Gradient Descent")
plt.legend()
plt.show()
