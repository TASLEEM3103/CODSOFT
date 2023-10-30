import random

def create_board():
    board = [[" " for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def random_place(board, player):
    available = possibilities(board)
    if available:
        row, col = random.choice(available)
        board[row][col] = player

def row_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    return False

def col_win(board, player):
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    return False

def diag_win(board, player):
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def evaluate(board):
    for player in ["X", "O"]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            return player
    if " " not in board[0] and " " not in board[1] and " " not in board[2]:
        return "Draw"
    return None

def play_game():
    board = create_board()
    players = ["X", "O"]
    random.shuffle(players)
    player = players[0]

    while True:
        print_board(board)
        print(f"Player {player}'s turn")

        if player == "X":
            row, col = map(int, input("Enter your move (row and column, e.g., 0 1): ").split())
            if board[row][col] == " ":
                board[row][col] = player
            else:
                print("Invalid move. Try again.")
                continue
        else:
            random_place(board, player)

        result = evaluate(board)
        if result:
            print_board(board)
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"Player {result} wins!")
            break

        player = "X" if player == "O" else "O"

if __name__ == "__main__":
    play_game()
