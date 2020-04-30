marker_1 = "X"
marker_2 = "O"


# Prints TicTacToe board with lines
def print_board(array):
    print()
    for r in range(len(array)):
        if r == 0:
            for c in range(len(array[r])):
                if c == 0:
                    print(array[r][c], end=" ")
                else:
                    print("| " + array[r][c], end=" ")
        else:
            for c in range(len(array[r]) * 2 - 1):
                print("-", end=" ")
            print()
            for c in range(len(array[r])):
                if c == 0:
                    print(array[r][c], end=" ")
                else:
                    print("| " + array[r][c], end=" ")
        print()
    print()


# r % 2
# array[int(r/2)]
def print_board2(array):
    print()
    for r in range(len(array) * 2 - 1):
        if r % 2 == 0:
            for c in range(len(array[int(r/2)])):
                if c == 0:
                    print(array[int(r/2)][c], end=" ")
                else:
                    print("| " + array[int(r/2)][c], end=" ")
        elif r % 2 == 1:
            for c in range(len(array[int(r/2)]) * 2 - 1):
                print("-", end=" ")
        print()
    print()


# Checks if marker position in the array is a valid input
def check_pos(array, pos):
    try:
        pos = int(pos)
        if 1 <= pos <= 9:
            if array[(pos - 1) // 3][(pos - 1) % 3] == int:
                return pos
            else:
                raise ValueError
        else:
            raise ValueError
    except ValueError:
        raise ValueError


# TicTacToe simulation
def ttt_simulation():
    print("Hello! Welcome to Joanne Tic-Tac-Toe!")
    print("This is a Tic-Tac-Toe game between two players.")
    input("Please press enter to start the game: ")
    game = "Y"
    win = "N"

    while game == "Y":
        # Creates a new 2D array for TicTacToe values
        val_rows, val_cols = (3, 3)
        val = []
        i = 1
        for r in range(val_rows):
            col = []
            for c in range(val_cols):
                col.append(str(i))
                i += 1
            val.append(col)

        print_board(val)
        print("Player 1 is %s" % marker_1)
        print("Player 2 is %s" % marker_2)
        print()

        while win == "N":
            while True:
                try:
                    user_pos_1 = input("Player 1, please choose a number on the board to place your marker: ")
                    pos_1 = check_pos(val, user_pos_1)
                    val[(pos_1 - 1) // 3][(pos_1 - 1) % 3] = marker_1
                    print_board(val)
                    break
                except ValueError:
                    print("Not a valid input. Please try again.")

            while True:
                try:
                    user_pos_2 = input("Player 2, please choose a number on the board to place your marker: ")
                    pos_2 = check_pos(val, user_pos_2)
                    val[(pos_2 - 1) // 3][(pos_2 - 1) % 3] = marker_2
                    print_board(val)
                    break
                except ValueError:
                    print("Not a valid input. Please try again.")

            win = "Y"

        game = "N"


def main():
    ttt_simulation()


if __name__ == "__main__":
    main()

# Questions
# Allow players to select their own markers
# How to add different error messages to the same function
# Check array for win scenarios
