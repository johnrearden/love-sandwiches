# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import time


def create_board(width, height):
    board = []
    for ind in range(width * height):
        board.append('.')
        if ind % width == 0:
            board.append('=\n')
    return board
    

def stringify_board(board):
    output = ''.join(board)
    return output


def main():
    """
    Run all program functions
    """
    board = create_board(60, 22)
    output = stringify_board(board)
    print(output)
    for i in range(1, 10):
        board[i] = '*'
        board[i - 1] = '.'
        output = stringify_board(board)
        print(output)
        time.sleep(0.1)


print("Welcome to Love Sandwiches data automation")


main()
