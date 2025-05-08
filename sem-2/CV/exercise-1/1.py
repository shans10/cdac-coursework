import numpy as np

M = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [0, 2, 2],
    ]
)

a = np.array(
    [
        [1],
        [1],
        [0],
    ]
)

b = np.array(
    [
        [-1],
        [2],
        [5],
    ]
)

c = np.array(
    [
        [0],
        [2],
        [3],
        [2],
    ]
)

print(np.dot(a.T, b))
print(np.multiply(a, b).T)
print(np.multiply(a, b).T)
print(M * a.T)
print(np.sort(M))
