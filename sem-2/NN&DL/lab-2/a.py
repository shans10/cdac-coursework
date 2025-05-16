import numpy as np

# From a Python list
a = np.array([1, 2, 3])
print(a)  # [1 2 3]

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# Zeros, Ones, and Identity
np.zeros((2, 3))  # 2x3 array of zeros
np.ones((3, 2))  # 3x2 array of ones
np.eye(3)  # 3x3 identity matrix

# Range and linspace
np.arange(0, 10, 2)  # [0 2 4 6 8]
np.linspace(0, 1, 5)  # [0.   0.25 0.5  0.75 1.  ]

a = np.array([[10, 20, 30], [40, 50, 60]])

print(a[0, 1])  # 20
print(a[:, 1])  # Column: [20 50]
print(a[1, :])  # Row: [40 50 60]
