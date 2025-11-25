#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        winner = check_winner(board)
        if winner:
            print_board(board)
            print("Player", winner, "wins!")
            break

        row = valid_input("Enter row (0, 1, or 2) for player " + player + ": ")
        col = valid_input("Enter column (0, 1, or 2) for player " + player + ": ")

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        player = "O" if player == "X" else "X"

tic_tac_toe()
