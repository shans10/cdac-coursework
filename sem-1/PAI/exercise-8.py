def print_solution(board):
    """Print the chessboard."""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col, n):
    """
    Check if placing a queen at board[row][col] is safe.
    """
    # Check the current column
    for i in range(row):
        if board[i][col]:
            return False

    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, row, n):
    """
    Solve the N Queens problem using backtracking.
    """
    if row >= n:
        print_solution(board)
        return True

    res = False
    for col in range(n):
        if is_safe(board, row, col, n):
            # Place the queen
            board[row][col] = True

            # Recurse for the next row
            res = solve_n_queens(board, row + 1, n) or res

            # Backtrack and remove the queen
            board[row][col] = False

    return res

def n_queens(n):
    """
    Initialize the board and solve the N Queens problem.
    """
    board = [[False] * n for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists.")

# Example Usage
if __name__ == "__main__":
    N = 8  # Change this to solve for a different board size
    n_queens(N)
