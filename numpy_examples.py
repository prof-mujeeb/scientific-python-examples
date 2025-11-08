import numpy as np

# Create an array
a = np.array([1, 2, 3, 4])
print("Array:", a)

# Dot product example
b = np.array([4, 3, 2, 1])
dot = np.dot(a, b)
print("Dot product:", dot)

# Matrix multiplication
A = np.array([[1,2],[3,4]])
B = np.array([[2,0],[1,2]])
C = np.matmul(A,B)
print("Matrix multiplication:\n", C)
