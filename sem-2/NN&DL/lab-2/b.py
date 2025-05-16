import numpy as np

# Step 1: Create two matrices for multiplication
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8], [9, 10], [11, 12]])

# Step 2: Matrix multiplication (A is 2x3, B is 3x2 -> result is 2x2)
C = A @ B
print("Matrix Multiplication (A @ B):\n", C)

# Step 3: Transpose the result
C_T = C.T
print("\nTranspose of the result:\n", C_T)

# Step 4: Reshape the transposed matrix (from 2x2 to 1x4)
C_reshaped = C_T.reshape((1, 4))
print("\nReshaped Transposed Matrix (1x4):\n", C_reshaped)
