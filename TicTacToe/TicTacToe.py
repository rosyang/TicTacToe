player1 = "X"
player2 = "O"

# Works best with an odd number of rows and columns
rows, cols = (5, 5)
board = []


# Creates a 2D array for the TicTacToe board
# Headings with appropriate indices are displayed with board
# Works best with an odd number of rows and columns
def create_board():
    top_heading = []

    for i in range(cols):
        col_1 = []
        col_2 = []
        top_heading = []

        for j in range(rows):
            if j % 2 == 0:
                col_1.append(" ")
                top_heading.append(j)
            elif j % 2 == 1:
                col_1.append("|")
                top_heading.append(" ")
            col_2.append("-")

        col_1.insert(0, i)
        col_2.insert(0, " ")

        if i % 2 == 0:
            board.append(col_1)
        elif i % 2 == 1:
            board.append(col_2)

    top_heading.insert(0, " ")
    board.insert(0, top_heading)


# Prints the TicTacToe board
def print_board():
    for r in board:
        for c in r:
            print(c, end=" ")
        print()


# TicTacToe simulation
def ttt_simulation():
    print("Hello! Welcome to Joanne Tic-Tac-Toe!")
    print("This is a Tic-Tac-Toe game between two players.")
    print("Player 1 is %s" % player1)
    print("Player 2 is %s" % player2)

    create_board()
    print_board()


def main():
    ttt_simulation()


if __name__ == "__main__":
    main()

# Questions
# Allow players to select their own markers?
