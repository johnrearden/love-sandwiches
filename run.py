# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import threading
import sys
import os

class Board:
    def __init__(self, width, height):
        self.cells = []
        for ind in range(width * height):
            if ind > 0 and ind % width == 0:
                self.cells.append("=\n")
            else:
                self.cells.append(".")
        self.cells.append('\n')
    
    def stringify(self):
        return ''.join(self.cells)


def draw_board(board):
    sys.stdout.write('\x1b7')
    sys.stdout.write('\r')
    sys.stdout.write('\x1b[22A')
    sys.stdout.write(board.stringify())
    sys.stdout.write('\x1b8')
    sys.stdout.flush()
    t = threading.Timer(2, draw_board, args=[board])
    t.start()


def main():
    """
    Run all program functions
    """
    board = Board(60, 20)
    sys.stdout.write(board.stringify())
    sys.stdout.flush()
    t = threading.Timer(2, draw_board, args=[board])
    t.start()

    while True:
        i = input("Enter a command:")
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
        sys.stdout.flush()
        # os.system('clear')

    sys.stdout.write("You are the man.\nI am but a dufus\nGo dude\nok?")
    sys.stdout.write('\x1b7')
    sys.stdout.write('\r')
    sys.stdout.write('\x1b[3A')
    sys.stdout.write("aaa")
    sys.stdout.write('\x1b8')
    input("Enter a command : ")
    sys.stdout.write("Woohoo!")
    

main()
