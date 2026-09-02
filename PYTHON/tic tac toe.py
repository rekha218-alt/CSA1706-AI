# Tic Tac Toe Game

board = [" " for _ in range(9)]

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win = [(0,1,2),(3,4,5),(6,7,8),
           (0,3,6),(1,4,7),(2,5,8),
           (0,4,8),(2,4,6)]

    for a, b, c in win:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

player = "X"

for turn in range(9):
    display()

    pos = int(input(f"Player {player}, Enter position (1-9): ")) - 1

    if board[pos] != " ":
        print("Position already filled! Try again.")
        continue

    board[pos] = player

    if check_winner(player):
        display()
        print("Player", player, "Wins!")
        break

    player = "O" if player == "X" else "X"

else:
    display()
    print("Match Draw!")
