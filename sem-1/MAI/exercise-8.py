#
# Problem Statement: Write a program to solve system of equations using Cramer's Rule.
#


# Function to find the determinant of given matrix
def determinant(matrix):
    """Calculate the determinant of a square matrix."""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sub_matrix = [row[:col] + row[col + 1 :] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    return det


# Function to apply Cramer's Rule
def cramer_rule(coeff_matrix, constants):
    """Solve a system of linear equations using Cramer's Rule."""
    n = len(coeff_matrix)
    det_main = determinant(coeff_matrix)
    if det_main == 0:
        raise ValueError("The system has no unique solution (determinant is 0).")

    solutions = []
    for i in range(n):
        temp_matrix = [
            row[:i] + [constants[row_idx]] + row[i + 1 :]
            for row_idx, row in enumerate(coeff_matrix)
        ]
        det_temp = determinant(temp_matrix)
        solutions.append(det_temp / det_main)
    return solutions


# Function to get matrix from user
def get_matrix_input():
    """Get coefficient matrix and constants from the user."""
    n = int(input("Enter the number of variables (n): "))
    print("Enter the coefficient matrix row by row (space-separated values):")
    coeff_matrix = []
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        while len(row) != n:
            print(f"Row {i + 1} must have exactly {n} values. Try again.")
            row = list(map(float, input(f"Row {i + 1}: ").split()))
        coeff_matrix.append(row)

    print("Enter the constants vector (space-separated values):")
    constants = list(map(float, input().split()))
    while len(constants) != n:
        print(f"The constants vector must have exactly {n} values. Try again.")
        constants = list(map(float, input().split()))

    return coeff_matrix, constants


# Main Program
print("Solve a System of Linear Equations using Cramer's Rule")
try:
    coeff_matrix, constants = get_matrix_input()
    solutions = cramer_rule(coeff_matrix, constants)
    print("The solution is:")
    for i, sol in enumerate(solutions):
        print(f"x{i + 1} = {sol}")
except ValueError as e:
    print("Error:", e)
