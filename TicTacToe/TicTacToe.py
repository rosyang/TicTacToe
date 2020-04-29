player1 = "X"
player2 = "O"


# Prints TicTacToe board with lines
def print_board(arr):
    board_rows, board_cols = (5, 5)
    print()
    for r in range(board_rows):
        if r % 2 == 0:
            i = 0
            for c in range(board_cols):
                if c % 2 == 0:
                    print(arr[int(r/2)][i], end=" ")
                    i += 1
                elif c % 2 == 1:
                    print("|", end=" ")
        elif r % 2 == 1:
            for c in range(board_cols):
                print("-", end=" ")
        print()
    print()


# TicTacToe simulation
def ttt_simulation():
    print("Hello! Welcome to Joanne Tic-Tac-Toe!")
    print("This is a Tic-Tac-Toe game between two players.")
    input("Please press enter to start the game: ")
    game = "Y"

    while game == "Y":
        # Creates a new 2D array for TicTacToe values
        arr_rows, arr_cols = (3, 3)
        arr = []
        i = 1
        for r in range(arr_rows):
            col = []
            for c in range(arr_cols):
                col.append(str(i))
                i += 1
            arr.append(col)

        print_board(arr)
        print("Player 1 is %s" % player1)
        print("Player 2 is %s" % player2)
        print()

        game = "N"


def main():
    ttt_simulation()


if __name__ == "__main__":
    main()

# Questions
# Allow players to select their own markers?
