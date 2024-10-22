import random

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def create_board():
    """Creates an initial board with one queen in each column."""
    board = []
    for col in range(8):
        row = random.randint(0, 7)
        board.append((row, col))
    return board

def calculate_attacks(board):
    """Calculates the number of pairs of queens attacking each other."""
    attacks = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i][0] == board[j][0]:  # Same row
                attacks += 1
            if abs(board[i][0] - board[j][0]) == abs(board[i][1] - board[j][1]):  # Same diagonal
                attacks += 1
    return attacks

def hill_climbing():
    board = create_board()
    current_attacks = calculate_attacks(board)

    while True:
        # Find the best neighboring state
        best_board = board
        best_attacks = current_attacks

        for col in range(8):
            # Try moving the queen in this column to each row
            for row in range(8):
                if row != board[col][0]:  # Skip the current position
                    new_board = board[:]
                    new_board[col] = (row, col)
                    new_attacks = calculate_attacks(new_board)
                    
                    # Check if this new board is better
                    if new_attacks < best_attacks:
                        best_board = new_board
                        best_attacks = new_attacks
        
        if best_attacks < current_attacks:  # Found a better state
            board = best_board
            current_attacks = best_attacks
        else:
            # No better state found, stop
            break

    return board, current_attacks

# Main execution
solution, attacks = hill_climbing()

if attacks == 0:
    print("Solution found:")
    # Prepare the board for printing
    board_output = [["." for _ in range(8)] for _ in range(8)]
    for row, col in solution:
        board_output[row][col] = "Q"
    print_board(board_output)
else:
    print(f"Failed to find a solution. Attacks: {attacks}")
