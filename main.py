board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]

# ******* To Create A Board ********** #


def print_board():
    for row in board:
        print(row)


print_board()

# ******* Making Index Value of Board Easy ********** #
a = board[0][0]
b = board[0][1]
c = board[0][2]

d = board[1][0]
e = board[1][1]
f = board[1][2]

g = board[2][0]
h = board[2][1]
i = board[2][2]

# ********* Printing Introduction ********** #
print("\nINTRODUCTION \nWelcome to Tic-tac-toe\n"
      "This table is denoted by alphabets ranging from a to i."
      "To put your X or O Give the position in terms of alphabets!\n"
      "Have a nice game!")

# ********** Selecting Player ********** #
player = input("Would you like to choose X or O?").lower()
if player == "x":
    player_1 = "x"
    player_2 = "O"
else:
    player_1 = "0"
    player_2 = "X"

# ********** Starting Game ********** #
game = True
sample = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]

]

# ********** Check Game ********** #


def won():
    if board[0][0] == board[0][1] == board[0][2] == "X" \
            or board[0][0] == board[1][0] == board[2][0] == "X" \
            or board[0][0] == board[1][1] == board[2][2] == "X" \
            or board[0][2] == board[1][2] == board[2][2] == "X" \
            or board[1][0] == board[1][1] == board[1][2] == "X" \
            or board[2][0] == board[2][1] == board[2][2] == "X":
        print('player_1 has won the game')
        return "player_1"
    elif board[0][0] == board[0][1] == board[0][2] == "O" \
            or board[0][0] == board[1][0] == board[2][0] == "O" \
            or board[0][0] == board[1][1] == board[2][2] == "O" \
            or board[0][2] == board[1][2] == board[2][2] == "O" \
            or board[1][0] == board[1][1] == board[1][2] == "O" \
            or board[2][0] == board[2][1] == board[2][2] == "O":
        print('player_2 has won the game')
        return "player_2"


def start_game():
    while game:
        if won() == "player_1":
            break
        elif won() == "player_2":
            break

        position_x = input(f"where you would like to put your X?")
        if position_x == "a":
            board[0][0] = "X"
            print_board()
            won()

        elif position_x == "b":
            board[0][1] = "X"
            print_board()
            won()

        elif position_x == "c":
            board[0][2] = "X"
            print_board()
            won()

        elif position_x == "d":
            board[1][0] = "X"
            print_board()
            won()

        elif position_x == "e":
            board[1][1] = "X"
            print_board()
            won()

        elif position_x == "f":
            board[1][2] = "X"
            print_board()
            won()

        elif position_x == "g":
            board[2][0] = "X"
            print_board()
            won()

        elif position_x == "h":
            board[2][1] = "X"
            print_board()
            won()

        elif position_x == "i":
            board[2][2] = "X"
            print_board()
            won()

        if won() == "player_1":
            break
        elif won() == "player_2":
            break

        position_o = input(f"where you would like to put your O?")

        if position_o == "a":
            board[0][0] = "0"
            print_board()
            won()

        elif position_o == "b":
            board[0][1] = "O"
            print_board()
            won()

        elif position_o == "c":
            board[0][2] = "0"
            print_board()
            won()

        elif position_o == "d":
            board[1][0] = "O"
            print_board()
            won()

        elif position_o == "e":
            board[1][1] = "O"
            print_board()
            won()

        elif position_o == "f":
            board[1][2] = "O"
            print_board()
            won()

        elif position_o == "g":
            board[2][0] = "O"
            print_board()
            won()

        elif position_o == "h":
            board[2][1] = "O"
            print_board()
            won()

        elif position_o == "i":
            board[2][2] = "O"
            print_board()
            won()


start_game()
