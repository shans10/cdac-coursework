#
# Problem Statement: Write a program to find the rank of a given matrix.
#

# Function to determine rank of the given matrix
def matrix_rank(matrix):
    def swap_rows(m, row1, row2):
        m[row1], m[row2] = m[row2], m[row1]

    def scale_row(m, row, scalar):
        m[row] = [element * scalar for element in m[row]]

    def add_scaled_row(m, target_row, source_row, scalar):
        m[target_row] = [
            target_element + scalar * source_element
            for target_element, source_element in zip(m[target_row], m[source_row])
        ]

    # Convert all rows to floats for consistent arithmetic
    for row in matrix:
        row[:] = [float(x) for x in row]

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    rank = 0

    for col in range(cols):
        # Find a pivot row
        pivot_row = None
        for row in range(rank, rows):
            if matrix[row][col] != 0:
                pivot_row = row
                break

        if pivot_row is None:
            continue  # No pivot in this column, move to the next column

        # Swap the pivot row to the current rank position
        swap_rows(matrix, rank, pivot_row)

        # Normalize the pivot row
        scale_row(matrix, rank, 1.0 / matrix[rank][col])

        # Eliminate the current column in all other rows
        for row in range(rows):
            if row != rank:
                add_scaled_row(matrix, row, rank, -matrix[row][col])

        rank += 1

    return rank

# Function to take matrix input from user
def get_matrix_input():
    rows = int(input("Enter the number of rows in the matrix: "))
    cols = int(input("Enter the number of columns in the matrix: "))
    matrix = []
    print("Enter the matrix row by row (space-separated values):")
    for i in range(rows):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        while len(row) != cols:
            print(f"Row {i + 1} must have exactly {cols} values. Try again.")
            row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


# Main program
print("Matrix Rank Calculator")
user_matrix = get_matrix_input()
print("Rank of the matrix:", matrix_rank(user_matrix))
