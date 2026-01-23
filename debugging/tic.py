#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_draw(board):
    # Returns True if the board is full and there is no empty space
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)

        if check_winner(board):
            winner = "O" if player == "X" else "X"
            print(f"Player {winner} wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

                # Check bounds
                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Row and column must be 0, 1, or 2.")
                    continue

                # Check if spot is free
                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue

                # Valid input → place the move
                board[row][col] = player
                winner = player  # last player who moved

                # Switch player
                player = "O" if player == "X" else "X"

                break  # exit the inner input loop

            except ValueError:
                print("Please enter numeric values only.")

        # After each valid move, print the board
        print_board(board)

tic_tac_toe()
