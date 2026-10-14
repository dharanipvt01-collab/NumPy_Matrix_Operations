
import numpy as np

# Create two matrices
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix addition
print("\nMatrix Addition (A + B):")
print(A + B)

# Matrix subtraction
print("\nMatrix Subtraction (A - B):")
print(A - B)

# Matrix multiplication
print("\nMatrix Multiplication (A @ B):")
print(A @ B)

# Transpose of Matrix A
print("\nTranspose of Matrix A:")
print(A.T)

# Transpose of Matrix B
print("\nTranspose of Matrix B:")
print(B.T)
