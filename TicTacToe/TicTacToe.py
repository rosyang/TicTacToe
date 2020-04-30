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


# Updates array with players' placement of marker
# def place_marker(pos):


# TicTacToe simulation
def ttt_simulation():
    print("Hello! Welcome to Joanne Tic-Tac-Toe!")
    print("This is a Tic-Tac-Toe game between two players.")
    input("Please press enter to start the game: ")
    game = "Y"

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

        # pos_1 = input("Player 1, please choose a number on the board to place your marker: ")
        # place_marker(pos_1)
        # print_board(val)

        # pos_2 = input("Player 2, please choose a number on the board to place your marker: ")
        # place_marker(pos_2)
        # print_board(val)

        game = "N"


def main():
    ttt_simulation()


if __name__ == "__main__":
    main()

# Questions
# Allow players to select their own markers?
# Need to add error messages to marker inputs
