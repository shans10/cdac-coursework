#
# Problem Statement: Find if the give matrix is invertible. If yes,
# then find the inverted matrix using the Adjoint method.
#


# Function to calculate the determinant of a matrix
def determinant(matrix):
    if len(matrix) == 2:  # Base case for 2x2 matrix
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant(minor(matrix, 0, c))
    return det


# Function to calculate the minor of a matrix (removes i-th row and j-th column)
def minor(matrix, i, j):
    return [row[:j] + row[j + 1 :] for row in (matrix[:i] + matrix[i + 1 :])]


# Function to calculate the cofactor matrix
def cofactor_matrix(matrix):
    cofactors = []
    for r in range(len(matrix)):
        cofactor_row = []
        for c in range(len(matrix)):
            minor_det = determinant(minor(matrix, r, c))
            cofactor_row.append(((-1) ** (r + c)) * minor_det)
        cofactors.append(cofactor_row)
    return cofactors


# Function to transpose a matrix (to get the adjugate matrix)
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix))]


# Function to find the inverse of a matrix using the cofactor adjoint method
def inverse(matrix):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("The matrix is singular and cannot have an inverse.")

    # Special case for 2x2 matrix
    if len(matrix) == 2:
        return [
            [matrix[1][1] / det, -1 * matrix[0][1] / det],
            [-1 * matrix[1][0] / det, matrix[0][0] / det],
        ]

    # Find the cofactor matrix
    cofactors = cofactor_matrix(matrix)

    # Find the adjugate matrix (transpose of the cofactor matrix)
    adjugate = transpose(cofactors)

    # Divide adjugate matrix by the determinant to get the inverse matrix
    inverse_matrix = [
        [adjugate[r][c] / det for c in range(len(adjugate))]
        for r in range(len(adjugate))
    ]

    return inverse_matrix


# Function to take matrix input from the user
def input_matrix(name):
    n = int(input(f"Enter the size of the {name} matrix (n x n): "))
    matrix = []
    print(f"Enter the elements of {name} matrix row-wise (separated by spaces):")
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


# Function to display a matrix
def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(lambda x: f"{x:.6f}", row)))


# Main program
if __name__ == "__main__":
    matrix = input_matrix("input")

    try:
        inv_matrix = inverse(matrix)
        print("\nInverse of the given matrix:")
        display_matrix(inv_matrix)
    except ValueError as e:
        print(f"Error: {e}")
