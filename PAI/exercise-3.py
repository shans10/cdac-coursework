from itertools import product

# Function to check if a board configuration is valid based on Tic-Tac-Toe rules
def is_valid_board(board):
    # Count the number of X's and O's
    x_count = board.count('X')
    o_count = board.count('O')

    # Ensure the number of X's is equal to or one more than the number of O's
    if not (x_count == o_count or x_count == o_count + 1):
        return False

    # Check for winning conditions
    if check_winner(board, 'X') and check_winner(board, 'O'):
        return False  # Both players can't win simultaneously
    return True

# Function to check if a player has won
def check_winner(board, player):
    # Win conditions for rows, columns, and diagonals
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to generate all valid Tic-Tac-Toe board configurations
def generate_all_boards():
    all_boards = []
    # Generate all combinations of 'X', 'O', and ' ' for the 9 positions
    for comb in product('XO ', repeat=9):
        board = list(comb)
        if is_valid_board(board):
            all_boards.append(board)
    return all_boards

# Get all valid boards
valid_boards = generate_all_boards()

# Display all valid boards
for idx, board in enumerate(valid_boards):
    print(f"Board {idx + 1}: {board}")
