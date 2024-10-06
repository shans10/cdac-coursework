#
# Problem Statement: Solve a given system of equations using Gauss Elimination Method.
#


def gauss_elimination():
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

    # Applying Gauss Elimination
    for i in range(n - 1):
        if a[i][i] == 0.0:
            print("Mathematical error!")
            return

        for j in range(i + 1, n):
            c = a[j][i] / a[i][i]
            for k in range(n + 1):
                a[j][k] = a[j][k] - c * a[i][k]

    # Back Substitution
    x = [0 for _ in range(n)]
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]
        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]
        x[i] = x[i] / a[i][i]

    # Displaying the Solutions
    print("\nSolutions:")
    for i in range(n):
        print(f"x[{i+1}] = {x[i]:.3f}")


# Here we use the Gauss Elemination Function
if __name__ == "__main__":
    gauss_elimination()
