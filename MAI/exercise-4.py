#
# Problem Statement: Solve a given system of equations using Gauss Jordan Method.
#


def gauss_jordan():
    n = int(input("Enter the number of unknowns: "))
    a = []

    # Reading the Augmented Matrix
    print("Enter the Augmented Matrix row-wise:")
    for i in range(n):
        b = []
        print(f"Enter the Row {i+1}:")
        for j in range(n + 1):
            b.append(int(input()))
        a.append(b)

    print("\n")

    # Printing the matrix
    print("The matrix is: ")
    for i in range(n):
        for j in range(n + 1):
            print(a[i][j], end=" ")
        print()

    # Applying Gauss Jordan
    for i in range(n):
        if a[i][i] == 0.0:
            print("Mathematical error!")
            return

        for j in range(n):
            if i != j:
                ratio = a[j][i] / a[i][i]

                for k in range(n + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]

    # Printing the matrix
    print("The matrix after applying Gauss Jordan elimination is: ")
    for i in range(n):
        for j in range(n + 1):
            print(a[i][j], end=" ")
        print()

    # Printing the solution
    print("The solution is: ")
    for i in range(n):
        print(f"x{i+1} = {a[i][n]/a[i][i]}")


# Here we use the Gauss Jordan Function
if __name__ == "__main__":
    gauss_jordan()
