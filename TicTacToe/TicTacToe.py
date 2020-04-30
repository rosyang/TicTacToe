marker_1 = "X"
marker_2 = "O"


# Prints TicTacToe board with lines.
def print_board(array):
    print()
    for r in range(len(array)):
        if r != 0:
            for c in range(len(array[r]) * 2 - 1):
                print("-", end=" ")
            print()
        for c in range(len(array[r])):
            if c != 0:
                print("|", end=" ")
            print(array[r][c], end=" ")
        print()
    print()


# Checks if marker position in the array is a valid input.
# (1) pos is an integer (2) pos is between 1-9 (3) pos does not contain another marker
def check_pos(array, pos):
    try:
        pos = int(pos)
    except ValueError:
        print("Not a valid integer. Please try again.")
        raise ValueError

    # row and col length variables for 1-9
    # max position num
    if 1 <= pos <= 9:
        int(array[(pos - 1) // 3][(pos - 1) % 3])
        return pos
    else:
        print("Not a valid number. Please choose a number between 1-9.")
        raise ValueError


# Checks if one of three win scenarios are met.
# (1) Three in a row (2) Three in a column (3) Three diagonally
# def check_win(array):


# TicTacToe simulation.
def ttt_simulation():
    print()
    print("Hello! Welcome to Joanne Tic-Tac-Toe!")
    print("This is a Tic-Tac-Toe game between two players.")
    input("Please press enter to start the game: ")
    should_play = True
    player_won = False

    while should_play:
        # Creates a new 2D array for TicTacToe values.
        NUM_ROWS, NUM_COLS = (3, 3)
        val = []
        i = 1
        for r in range(NUM_ROWS):
            col = []
            for c in range(NUM_COLS):
                col.append(str(i))
                i += 1
            val.append(col)

        print_board(val)
        print("Player 1 is %s" % marker_1)
        print("Player 2 is %s" % marker_2)
        print()

        # Players take turn placing their marker on the board until there is a winner.
        while not player_won:
            while True:
                try:
                    user_pos_1 = input("Player 1, please choose a number on the board to place your marker: ")
                    pos_1 = check_pos(val, user_pos_1)
                    val[(pos_1 - 1) // 3][(pos_1 - 1) % 3] = marker_1
                    # check_win(val)
                    print_board(val)
                    break
                except ValueError:
                    pass

            while True:
                try:
                    user_pos_2 = input("Player 2, please choose a number on the board to place your marker: ")
                    pos_2 = check_pos(val, user_pos_2)
                    val[(pos_2 - 1) // 3][(pos_2 - 1) % 3] = marker_2
                    # check_win(val)
                    print_board(val)
                    break
                except ValueError:
                    pass

            player_won = True

        should_play = False


def main():
    ttt_simulation()


if __name__ == "__main__":
    main()

# Questions
# Allow players to select their own markers
# How to add different error messages to the same function
# Check array for win scenarios
# check_pos variables
# print introductory board, boolean parameter
