#
# Problem Statement: Write a program to check whether the matrix is invertible or not, if yes find the inverse.
#

# for taking input from user
n = int(input("Enter the number of rows and columns in nxn matrix: "))

# for taking the matrix input by the user
matrix = []

for i in range(n):
    print(f"Enter the {i+1} row of the matrix:")
    a = []
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

# printing the original matrix
print("The matrix is: ")
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()

# checking if the matrix is invertible or not

   ## here we get the minor of the matrix
def get_minor(matrix, row, col):
    return [r[:col] + r[col+1:] for r in (matrix[:row] + matrix[row+1:])]

   ## here we get the determinant of the matrix
def determinant(matrix):
    if len(matrix) == 1:  # Base case for 1x1 matrix
        return matrix[0][0]
    if len(matrix) == 2:  # Base case for 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant(get_minor(matrix, 0, c))
    return det

    ## here we chec if the matrix is invertible or not
if determinant(matrix) == 0:
    print("The matrix is not invertible")
    exit()
else:
    print("The matrix is invertible")


# for getting the inverse of the matrix if the matrix is invertible
def inverse(matrix):
    det = determinant(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] =determinant(get_minor(matrix, i, j))*(-1)**(i+j)  / det

    return matrix

matrix1 =inverse(matrix)
print("The inverse matrix is: ")
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        print(matrix1[i][j], end=" ")
    print()
