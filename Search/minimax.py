# Tic-Tac-Toe board represented as a list
# 'X' represents the first player, 'O' represents the second player, and None represents an empty cell
initial_board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(cell if cell is not None else " " for cell in row))
        print("-" * 9)

# Function to check if the current player has won
def is_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the board is full
def is_board_full(board):
    return all(all(cell is not None for cell in row) for row in board)

# Function to evaluate the board for the minimax algorithm
def evaluate_board(board):
    if is_winner(board, 'X'):
        return 1  # Player 'X' wins
    elif is_winner(board, 'O'):
        return -1  # Player 'O' wins
    elif is_board_full(board):
        return 0  # It's a draw
    else:
        return None  # Game is not over

# Minimax algorithm implementation
def minimax(board, depth, maximizing_player):
    score = evaluate_board(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'X'
                    eval_result = minimax(board, depth + 1, False)
                    board[i][j] = None
                    max_eval = max(max_eval, eval_result)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] is None:
                    board[i][j] = 'O'
                    eval_result = minimax(board, depth + 1, True)
                    board[i][j] = None
                    min_eval = min(min_eval, eval_result)
        return min_eval

# Function to find the best move using the minimax algorithm
def find_best_move(board):
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = None

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Function to play the Tic-Tac-Toe game
def play_tic_tac_toe():
    current_board = initial_board
    current_player = 'X'

    while True:
        print_board(current_board)

        if is_winner(current_board, 'X'):
            print("Player 'X' wins!")
            break
        elif is_winner(current_board, 'O'):
            print("Player 'O' wins!")
            break
        elif is_board_full(current_board):
            print("It's a draw!")
            break

        if current_player == 'X':
            print("Player 'X' turn:")
            move = find_best_move(current_board)
        else:
            print("Player 'O' turn:")
            move = tuple(map(int, input("Enter your move (row, column): ").split()))

        if current_board[move[0]][move[1]] is None:
            current_board[move[0]][move[1]] = current_player
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Cell already taken. Try again.")

# Play the game
play_tic_tac_toe()
