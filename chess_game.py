import os
import math


class Chess:
    board = [
        ["r", "h", "b", "k", "q", "b", "h", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "Q", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "H", "B", "K", "Q", "B", "H", "R"],
    ]

    def printboard(self, board):
        os.system("cls")
        print('\n'.join([''.join(['{:3}'.format(item)
              for item in row]) for row in board]))

    def playerturn(self, turn, game, board):
        while game == True:
            if turn is True:
                turn = not turn
                c.player1move(board, turn, game)
            if turn is False:
                turn = not turn
                c.player2move(board, turn, game)

    def player1move(self, board, turn, game):
        while True:
            coordinate1 = input("What white piece would you like to move?: ")
            y_axis = abs((ord(coordinate1[0].upper())-64)-8)
            x_axis = int(coordinate1[1])-1
            currentpiece = board[y_axis][x_axis]

            if currentpiece.isupper():
                break
            else:
                print("Please input a valid move. is white")

        print(currentpiece)
        c.movevalidation(board, coordinate1, currentpiece)
        c.playerturn(turn, board, game)

    def player2move(self, board, turn, game):
        while True:
            coordinate1 = input("What black piece would you like to move?: ")
            y_axis = abs((ord(coordinate1[0].upper())-64)-8)
            x_axis = int(coordinate1[1])-1
            currentpiece = board[y_axis][x_axis]

            if currentpiece.islower():
                break
            else:
                print("Please input a valid move. is black")

        print(currentpiece)
        c.movevalidation(board, coordinate1, currentpiece)
        c.playerturn(turn, board, game)

    def coordYhelper(self, coordinate):
        return abs((ord(coordinate[0].upper())-64)-8)

    def coordXhelper(self, coordinate):
        return int(coordinate[1])-1

    def movevalidation(self, board, coordinate1, currentpiece):
        while True:
            coordinate2 = input("Where is the piece moving to?: ")

            y1_axis = self.coordYhelper(coordinate1)
            x1_axis = self.coordXhelper(coordinate1)

            y2_axis = self.coordYhelper(coordinate2)
            x2_axis = self.coordXhelper(coordinate2)

            if currentpiece.lower() == "p":
                self.pawnmove(y1_axis, x1_axis, y2_axis, x2_axis, board)
                break

            if currentpiece.lower() == "h":
                self.knightmove(y1_axis, x1_axis, y2_axis, x2_axis, board)
                break

            if currentpiece.lower() == "b":
                self.bishopmove(y1_axis, x1_axis, y2_axis, x2_axis, board)
                break

            if currentpiece.lower() == "r":
                self.rookmove(y1_axis, x1_axis, y2_axis, x2_axis, board)
                return

            if currentpiece.lower() == "k":
                self.kingmove(y1_axis, x1_axis, y2_axis, x2_axis, board)
                break

            if currentpiece.lower() == "q":
                self.queenmove(y1_axis, x1_axis, y2_axis, x2_axis, board)
                break

    def sign(self, x):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        else:
            return 1

    def pawnmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        pathlength = abs(y1_axis - y2_axis)
        currentpiece = board[y1_axis][x1_axis]

        # black piece
        if board[y1_axis][x1_axis].islower():
            if board[y2_axis][x2_axis].isupper() and y2_axis == y1_axis+1 and (x2_axis == x1_axis + 1 or x2_axis == x1_axis - 1):
                board[y1_axis][x1_axis] = '-'
                board[y2_axis][x2_axis] = currentpiece
            if y1_axis == 1 and pathlength == 2:
                if board[y1_axis+1][x1_axis] == '-' and board[y1_axis+2][x1_axis] == '-':
                    board[y1_axis][x1_axis] = '-'
                    board[y2_axis][x2_axis] = currentpiece
            elif pathlength == 1:
                if board[y1_axis+1][x1_axis] == '-':
                    board[y1_axis][x1_axis] = '-'
                    board[y2_axis][x2_axis] = currentpiece

        # white piece
        if board[y1_axis][x1_axis].isupper():
            if board[y2_axis][x2_axis].islower() and y2_axis == y1_axis-1 and (x2_axis == x1_axis + 1 or x2_axis == x1_axis - 1):
                board[y1_axis][x1_axis] = '-'
                board[y2_axis][x2_axis] = currentpiece
            if y1_axis == 6 and pathlength == 2:
                if board[y1_axis-1][x1_axis] == '-' and board[y1_axis-2][x1_axis] == '-':
                    board[y1_axis][x1_axis] = '-'
                    board[y2_axis][x2_axis] = currentpiece
            elif pathlength == 1:
                if board[y1_axis-1][x1_axis] == '-':
                    board[y1_axis][x1_axis] = '-'
                    board[y2_axis][x2_axis] = currentpiece
        c.printboard(board)

    # Proper Rules
    def bishopmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        pathlength = abs(y1_axis - y2_axis)
        incx, incy = c.sign(x2_axis-x1_axis), c.sign(y2_axis-y1_axis)
        if (incx == 0 or incy == 0):
            print("Invalid move. Please input a new move.0")
            return
        x, y = x1_axis, y1_axis
        print(incx, incy)
        for i in range(1, pathlength):
            x += incx
            y += incy
            print(y+1, x+1)
            if (board[y][x] == "-" and (y != y2_axis and x != x2_axis)):
                continue
            else:
                print("Invalid move. Please input a new move.1")
                return

        if board[y1_axis][x1_axis].isupper():
            if board[y2_axis][x2_axis].islower() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
            else:
                print("Invalid move. Please input a new move.2")
        elif board[y1_axis][x1_axis].islower():
            if board[y2_axis][x2_axis].isupper() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
            else:
                print("Invalid move. Please input a new move.2")
        else:
            print("Invalid move. Please input a new move.3")
            return
        c.printboard(board)

    # Proper Rules
    def knightmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        if (abs(x1_axis - x2_axis) == 1 and abs(y1_axis - y2_axis) == 2) or (abs(x1_axis - x2_axis) == 2 and abs(y1_axis - y2_axis) == 1):
            if(board[y1_axis][x1_axis].isupper()):
                if(board[y2_axis][x2_axis] == "-" or board[y2_axis][x2_axis].islower()):
                    board[y2_axis][x2_axis] = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    c.printboard(board)
                    return
            if(board[y1_axis][x1_axis].islower()):
                if(board[y2_axis][x2_axis] == "-" or board[y2_axis][x2_axis].isupper()):
                    board[y2_axis][x2_axis] = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    c.printboard(board)
                    return
            else:
                print("Invalid target.")
                return
        print("Please input valid move.")
        return

    # Proper Rules
    def rookmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        while x1_axis != x2_axis and y1_axis != y2_axis:
            print("Please input a valid move coordinate.")
            coordinate2 = input("Where is the piece moving to?: ")
            y2_axis = self.coordYhelper(coordinate2)
            x2_axis = self.coordXhelper(coordinate2)

        pathlength = abs(y1_axis - y2_axis)
        incx, incy = c.sign(x2_axis-x1_axis), c.sign(y2_axis-y1_axis)
        x, y = x1_axis, y1_axis

        for i in range(1, pathlength):
            x += incx
            y += incy
            if (board[y][x] == "-" and (y == y2_axis or x == x2_axis)):
                continue
            else:
                print("Invalid move. Please input a new move.")
                return c.rookmove(y1_axis, x1_axis, y2_axis, x2_axis, board)

        if board[y1_axis][x1_axis].isupper():
            if board[y2_axis][x2_axis].islower() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
            else:
                print("Invalid move. Please input a new move.")
        else:
            if board[y2_axis][x2_axis].isupper() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
            else:
                print("Invalid move. Please input a new move.")
        c.printboard(board)

    def queenmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        while x1_axis != x2_axis and y1_axis != y2_axis:
            print("Please input a valid move coordinate.")
            coordinate2 = input("Where is the piece moving to?: ")
            y2_axis = self.coordYhelper(coordinate2)
            x2_axis = self.coordXhelper(coordinate2)

        pathlength = abs(y1_axis - y2_axis)
        incx, incy = c.sign(x2_axis-x1_axis), c.sign(y2_axis-y1_axis)
        x, y = x1_axis, y1_axis

        for i in range(1, pathlength):
            x += incx
            y += incy
            if (board[y][x] == "-" and (y == y2_axis or x == x2_axis)):
                continue
            else:
                print("Invalid move. Please input a new move.")
                return c.rookmove(y1_axis, x1_axis, y2_axis, x2_axis, board)

        if board[y1_axis][x1_axis].isupper():
            if board[y2_axis][x2_axis].islower() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
            else:
                print("Invalid move. Please input a new move.")
        else:
            if board[y2_axis][x2_axis].isupper() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
            else:
                print("Invalid move. Please input a new move.")
        c.printboard(board)

    def kingmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        def sign(x): return (1, -1)[x < 0]

        pathlength = abs(y1_axis - y2_axis)
        incx, incy = sign(x2_axis-x1_axis), sign(y2_axis-y1_axis)
        x, y = x1_axis, y1_axis

        for i in range(1, pathlength):
            x += incx
            y += incy
            print(y+1, x+1)
            if (board[y][x] == "-"):
                continue
            else:
                print("Invalid move. Please input a new move.")
                return

        if board[y2_axis][x2_axis].islower():
            currentpiece = board[y1_axis][x1_axis]
            board[y1_axis][x1_axis] = "-"
            board[y2_axis][x2_axis] = currentpiece
        else:
            print("Invalid move. Please input a new move.")
            return
        c.printboard(board)

        return


c = Chess()
c.printboard(c.board)
c.playerturn(True, True, c.board)
