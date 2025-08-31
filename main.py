# libraries to be used
import matplotlib.pyplot as plt
import math


# functions to be used
from greet import greet   # import the greet function
from math_functions import cal   # import the cal function

# print("Hello, Python in VS Code!")
a = 4 
b = a * 2
print(b) 
print(a > b)   # True

greet()

i, return1, return2 = cal(a,b)

# return2 = subtract(a,b)

print("Hi ")

print(return1)

print(return2)

print(i)

# Example data
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 9, 16]

# Plot
plt.plot(x, y)

# Add title and labels
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show the plot
plt.show()