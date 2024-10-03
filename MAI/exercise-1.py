#
# Problem Statement: Write an algorithm to multiply two matrices Amxn and Bnxp.
#

# Function to take matrix input from user
def input_matrix(name):
    rows = int(input(f"Enter the number of rows for {name}: "))
    cols = int(input(f"Enter the number of columns for {name}: "))

    matrix = []
    print(f"Enter the elements for {name} row-wise:")
    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    return matrix

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Get dimensions
    rows_matrix1 = len(matrix1)
    cols_matrix1 = len(matrix1[0])
    rows_matrix2 = len(matrix2)
    cols_matrix2 = len(matrix2[0])

    # Ensure multiplication is valid
    if cols_matrix1 != rows_matrix2:
        raise ValueError("Number of columns in Matrix 1 must equal number of rows in Matrix 2")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(cols_matrix2)] for _ in range(rows_matrix1)]

    # Perform matrix multiplication
    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Function to display matrix
def display_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

# Main program
if __name__ == "__main__":
    print("Matrix 1")
    matrix1 = input_matrix("Matrix 1")
    print("\nMatrix 2")
    matrix2 = input_matrix("Matrix 2")

    try:
        result = multiply_matrices(matrix1, matrix2)
        print("\nResultant Matrix after multiplication:")
        display_matrix(result)
    except ValueError as e:
        print(f"Error: {e}")
