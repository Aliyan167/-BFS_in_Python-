import math

# Constants for players
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns and diagonals
    for row in board:
        if row[0] == row[1] == row[2] != EMPTY:
            return True, row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return True, board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return True, board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return True, board[0][2]

    # Check for a tie (no empty spaces)
    if all(cell != EMPTY for row in board for cell in row):
        return True, None

    return False, None

# Mini-Max algorithm
def minimax(board, depth, is_maximizing):
    game_over, winner = is_game_over(board)
    
    if game_over:
        if winner == PLAYER_X:
            return -1
        elif winner == PLAYER_O:
            return 1
        else:
            return 0  # Tie

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O  # O's turn
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY  # Undo move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X  # X's turn
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY  # Undo move
                    best_score = min(score, best_score)
        return best_score

# Find the best move for O
def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER_O  # Try the move
                score = minimax(board, 0, False)
                board[row][col] = EMPTY  # Undo move

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

# Main game loop
def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        # Player X move
        while True:
            try:
                x, y = map(int, input("Player X, enter your move (row and column): ").split())
                if board[x][y] == EMPTY:
                    board[x][y] = PLAYER_X
                    break
                else:
                    print("Cell already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column (0-2).")

        print_board(board)
        game_over, winner = is_game_over(board)
        if game_over:
            if winner:
                print(f"Player {winner} wins!")
            else:
                print("It's a tie!")
            break

        # Player O move (AI)
        print("Player O is thinking...")
        row, col = find_best_move(board)
        board[row][col] = PLAYER_O
        print(f"Player O played at ({row}, {col})")
        print_board(board)
        
        game_over, winner = is_game_over(board)
        if game_over:
            if winner:
                print(f"Player {winner} wins!")
            else:
                print("It's a tie!")
            break

# Start the game
play_game()
