marker_1 = "X"
marker_2 = "O"


# Prints TicTacToe board with lines.
# Option to print introductory board with numbers indicating position.
def print_board(array, intro_board):
    i = 1
    print()
    for r in range(len(array)):
        if r != 0:
            for c in range(len(array[r]) * 2 - 1):
                print("-", end=" ")
            print()
        for c in range(len(array[r])):
            if c != 0:
                print("|", end=" ")
            if intro_board:
                print(str(i), end=" ")
                i += 1
            else:
                print(array[r][c], end=" ")
        print()
    print()


# Checks if marker position in the array is a valid input.
# (1) pos is an integer (2) pos is between 1-9 (3) pos does not contain another marker
def check_convert_pos(array, pos):
    try:
        pos = int(pos)
    except ValueError:
        print("Not a valid integer. Please try again.")
        raise ValueError

    MIN_POS = 1
    row_length = len(array)
    col_length = len(array[0])
    max_pos = row_length * col_length

    if MIN_POS <= pos <= max_pos:
        if array[(pos - 1) // 3][(pos - 1) % 3] == " ":
            return pos
        else:
            print("A marker is already in the position. Please try again.")
            raise ValueError
    else:
        print("Not a valid number. Please choose a number between %d-%d." % (MIN_POS, max_pos))
        raise ValueError


# Checks if one of three win scenarios are met.
# (1) Three in a row (2) Three in a column (3) Three diagonally (\ and /)
def check_win(array, marker):
    num_marker_diag_1 = 0
    num_marker_diag_2 = 0

    for r in range(len(array)):
        num_marker_row = 0
        num_marker_col = 0

        for c in range(len(array[r])):
            if array[r][c] == marker:
                num_marker_row += 1
            if array[c][r] == marker:
                num_marker_col += 1
            if r == c and array[r][c] == marker:
                num_marker_diag_1 += 1
                if r == 1:
                    num_marker_diag_2 += 1
            if r == 0 and c == (len(array) - 1):
                if array[r][c] == marker:
                    num_marker_diag_2 += 1
                if array[c][r] == marker:
                    num_marker_diag_2 += 1

        if num_marker_row == 3 or num_marker_col == 3:
            return True

    if num_marker_diag_1 == 3 or num_marker_diag_2 == 3:
        return True


# Checks if board still has blank spaces. Otherwise, draw scenario.
def check_draw(array):
    draw = True
    for r in range(len(array)):
        for c in range(len(array[r])):
            if array[r][c] == " ":
                draw = False
    return draw


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
        board_values = []
        for r in range(NUM_ROWS):
            col = []
            for c in range(NUM_COLS):
                col.append(" ")
            board_values.append(col)

        # Introductory board
        print()
        print("The board is arranged in the following order of numbers:")
        print("Player 1 is %s" % marker_1)
        print("Player 2 is %s" % marker_2)
        print_board(board_values, True)

        # Players take turn placing their marker on the board until there is a winner.
        while not player_won:
            while True:
                try:
                    user_pos_1 = input("Player 1, please choose a number on the board to place your marker: ")
                    pos_1 = check_convert_pos(board_values, user_pos_1)
                    board_values[(pos_1 - 1) // 3][(pos_1 - 1) % 3] = marker_1
                    break
                except ValueError:
                    pass

            print_board(board_values, False)
            if check_win(board_values, marker_1):
                print("Congratulations! Player 1 won!")
                break
            elif check_draw(board_values):
                print("The game is a draw!")
                break

            while True:
                try:
                    user_pos_2 = input("Player 2, please choose a number on the board to place your marker: ")
                    pos_2 = check_convert_pos(board_values, user_pos_2)
                    board_values[(pos_2 - 1) // 3][(pos_2 - 1) % 3] = marker_2
                    break
                except ValueError:
                    pass

            print_board(board_values, False)
            if check_win(board_values, marker_2):
                print("Congratulations! Player 2 won!")
                break
            elif check_draw(board_values):
                print("The game is a draw!")
                break

        print()
        user_play = input("Would you like to play another game (Y/N)? ")
        while True:
            if user_play == "Y":
                break
            elif user_play == "N":
                should_play = False
                break
            else:
                user_play = input("Please enter Y/N: ")

    print()
    print("Thank you for playing Joanne Tic-Tac-Toe! See you next time!")


def main():
    ttt_simulation()


if __name__ == "__main__":
    main()
