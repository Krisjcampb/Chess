import os


class Board:
    board = [
        ["r", "h", "b", "k", "q", "b", "h", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "H", "B", "K", "Q", "B", "H", "R"],
    ]
    startingboard = board
    checkboard = [
        ["-", "h", "p", "k", "q", "p", "h", "-"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "p", "p", "-", "-", "-", "-"],
        ["-", "-", "p", "-", "-", "-", "-", "-"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "H", "B", "K", "Q", "B", "H", "R"],
    ]

    def printboard(self, board):
        os.system("cls")
        print('\n'.join([''.join(['{:3}'.format(item)
                                  for item in row]) for row in board]))

    def gamewin(self, PlayerNum):
        print("Player {} wins!".format(PlayerNum))
        while True:
            Restart = input(
                "Would you like to play again? Y/N\n")
            if Restart == "Y":
                pass
            elif Restart == "N":
                quit()
            else:
                print("Please input put Y or N.")
