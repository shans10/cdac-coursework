#
# Problem Statement: Write an algorithm to transpose a square matrix A within A.
#

# for taking input from user for m*n matrix
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


# here is the fuction which transpose the matrix within the same matrix
for i in range(n):
    for j in range(i+1):
        temp=matrix[i][j]
        matrix[i][j]=matrix[j][i]
        matrix[j][i]=temp


# printing the transpose of the original matrix
print("The matrix after being transposedis: ")

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()
