#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the current board state.

    Returns:
        str: 'X' if player X wins, 'O' if player O wins, None if no winner.
    """
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_board_full(board):
    """
    Checks if the board is full.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play Tic-Tac-Toe game.
    """
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
        col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        
        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            print("Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        if board[row][col] == " ":
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()

