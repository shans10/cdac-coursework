# Get the elements of the matrix from user
def get_matrix_from_user(size):
    print(f"Enter the elements of the {size}x{size} matrix row-wise:")
    matrix = []
    for i in range(size):
        row = list(map(float, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != size:
            raise ValueError("Number of columns must match the matrix size.")
        matrix.append(row)
    return matrix


# Print the matrix
def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{elem:.2f}" for elem in row))


# Get the identity matrix for the given matrix
def get_identity_matrix(size):
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


# Calculate the inverse of the given matrix
def calculate_inverse(matrix):
    size = len(matrix)
    augmented_matrix = [
        row[:] + identity_row[:]
        for row, identity_row in zip(matrix, get_identity_matrix(size))
    ]

    for i in range(size):
        # Make the diagonal contain all 1s
        diag = augmented_matrix[i][i]
        if diag == 0:
            return None  # Matrix is singular

        for j in range(2 * size):
            augmented_matrix[i][j] /= diag

        # Make the other rows contain 0s in the current column
        for k in range(size):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(2 * size):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    # Extract the inverse matrix
    inverse_matrix = [row[size:] for row in augmented_matrix]
    return inverse_matrix


# Main function to perform matrix inversion
def main():
    # Check user input is positive for size of matrix
    try:
        size = int(input("Enter the size of the square matrix (e.g., 2 for 2x2): "))
        if size <= 0:
            raise ValueError("Size must be a positive integer.")

        matrix = get_matrix_from_user(size)

        print("Input Matrix:")
        print_matrix(matrix)

        inverse = calculate_inverse(matrix)

        if inverse:
            print("Inverse Matrix:")
            print_matrix(inverse)
        else:
            print("The matrix is singular and does not have an inverse.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
