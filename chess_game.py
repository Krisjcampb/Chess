import os
import math
import copy


class Chess:
    board = [
        ["-", "h", "p", "k", "q", "p", "h", "-"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "r", "r", "-", "r", "K", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["P", "P", "P", "Q", "P", "P", "P", "P"],
        ["R", "H", "B", "K", "Q", "B", "H", "R"],
    ]
    checkboard = [
        ["-", "h", "p", "k", "q", "p", "h", "-"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "r", "r", "-", "r", "K", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-"],
        ["P", "P", "P", "Q", "P", "P", "P", "P"],
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
                cl.player1move(board, turn, game)
            if turn is False:
                turn = not turn
                cl.player2move(board, turn, game)

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
        cl.movevalidation(board, coordinate1, currentpiece)
        cl.playerturn(turn, board, game)

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
        cl.movevalidation(board, coordinate1, currentpiece)
        cl.playerturn(turn, board, game)

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

    # Not Done
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
        cl.printboard(board)

    # Done
    def bishopmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
        incx, incy = cl.sign(x2_axis-x1_axis), cl.sign(y2_axis-y1_axis)
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
        cl.printboard(board)

    # Done
    def knightmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        if (abs(x1_axis - x2_axis) == 1 and abs(y1_axis - y2_axis) == 2) or (abs(x1_axis - x2_axis) == 2 and abs(y1_axis - y2_axis) == 1):
            if(board[y1_axis][x1_axis].isupper()):
                if(board[y2_axis][x2_axis] == "-" or board[y2_axis][x2_axis].islower()):
                    board[y2_axis][x2_axis] = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    cl.printboard(board)
                    return
            if(board[y1_axis][x1_axis].islower()):
                if(board[y2_axis][x2_axis] == "-" or board[y2_axis][x2_axis].isupper()):
                    board[y2_axis][x2_axis] = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    cl.printboard(board)
                    return
            else:
                print("Invalid target.")
                return
        print("Please input valid move.")
        return

    # Done
    def rookmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        while x1_axis != x2_axis and y1_axis != y2_axis:
            print("Please input a valid move coordinate.")
            coordinate2 = input("Where is the piece moving to?: ")
            y2_axis = self.coordYhelper(coordinate2)
            x2_axis = self.coordXhelper(coordinate2)

        pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
        incx, incy = cl.sign(x2_axis-x1_axis), cl.sign(y2_axis-y1_axis)
        x, y = x1_axis, y1_axis

        for i in range(1, pathlength):
            x += incx
            y += incy
            if (board[y][x] == "-" and (y == y2_axis or x == x2_axis)):
                continue
            else:
                print("Invalid move. Please input a new move.")
                return cl.rookmove(y1_axis, x1_axis, y2_axis, x2_axis, board)

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
        cl.printboard(board)

    # Done
    def queenmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
        incx, incy = cl.sign(x2_axis-x1_axis), cl.sign(y2_axis-y1_axis)
        x, y = x1_axis, y1_axis

        if(x1_axis == x2_axis or y1_axis == y2_axis):
            for i in range(1, pathlength):
                x += incx
                y += incy
                if (board[y][x] == "-" and (y == y2_axis or x == x2_axis)):
                    continue
                else:
                    print("Invalid move. Please input a new move.")
                    return cl.queenmove(y1_axis, x1_axis, y2_axis, x2_axis, board)
        else:
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
        cl.printboard(board)

    # Not Done
    def kingmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        def sign(x): return (1, -1)[x < 0]

        pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
        incx, incy = sign(x2_axis-x1_axis), sign(y2_axis-y1_axis)
        x, y = x1_axis, y1_axis

        if pathlength != 1:
            print("Invalid move.")
            return
        for i in range(1, pathlength):
            x += incx
            y += incy
            print(y+1, x+1)
            if (board[y][x] == "-"):
                continue
            else:
                print("Invalid move. Please input a new move.1")
                return

        if board[y2_axis][x2_axis].islower() or board[y2_axis][x2_axis] == "-":
            currentpiece = board[y1_axis][x1_axis]
            board[y1_axis][x1_axis] = "-"
            board[y2_axis][x2_axis] = currentpiece
        else:
            print("Invalid move. Please input a new move.2")
            return
        cl.printboard(board)

        return

    # 1.) Find if a piece is attacking a king by checking all enemy piece movement possibilities COMPLETE

    # 2.) If king is being attacked check all ally movement possibilities and check if king is still in check
    # Create a duplicate board that is only used when king is in check and check if each piece
    # 3.) If king is still in check declare checkmate
    def kingcheck(self, board):
        check = False
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].lower() == 'p' and board[i][j].islower():
                    if i+1 < 8 and j-1 > 0:
                        if board[i+1][j-1] == 'K':
                            print("Check")
                    if i+1 < 8 and j+1 < 8:
                        if board[i+1][j+1] == 'K':
                            print("Check")
                if board[i][j].lower() == 'h' and board[i][j].islower():
                    if i+2 < 8 and j+1 < 8:
                        if board[i+2][j+1] == 'K':
                            print("Check")
                    if i+2 < 8 and j-1 > 0:
                        if board[i+2][j-1] == 'K':
                            print("Check")
                    if i-2 > 0 and j+1 < 8:
                        if board[i-2][j+1] == 'K':
                            print("Check")
                    if i-2 > 0 and j-1 < 8:
                        if board[i-2][j-1] == 'K':
                            print("Check")
                    if i+1 < 8 and j+2 < 8:
                        if board[i+1][j+2] == 'K':
                            print("Check")
                    if i-1 > 0 and j+2 < 8:
                        if board[i-1][j+2] == 'K':
                            print("Check")
                    if i+1 < 8 and j-2 > 0:
                        if board[i+1][j-2] == 'K':
                            print("Check")
                    if i-1 > 0 and j-2 > 0:
                        if board[i-1][j-2] == 'K':
                            print("Check")
                if board[i][j].lower() == 'b' and board[i][j].islower():
                    leftup = True
                    leftdown = True
                    rightup = True
                    rightdown = True
                    for c in range(1, 7):
                        if leftup == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False

                        if leftdown == True:
                            if j-c < 0 and i-c < 0 and board[i-c][j-c] == 'K':
                                print("Check")
                            if j-c > 7 or i-c < 0 or board[i-c][j-c].islower() or board[i-c][j-c].isupper():
                                leftdown = False

                        if rightup == True:
                            if j+c < 8 and i+c < 8 and board[i+c][j+c] == 'K':
                                print("Check")
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].islower() or board[i+c][j+c].isupper():
                                rightup = False

                        if rightdown == True:
                            if j+c < 8 and i-c > 0 and board[i-c][j+c] == 'K':
                                print("Check")
                            if j+c > 7 or i-c < 0 and board[i-c][j+c].islower() or board[i-c][j+c].isupper():
                                rightdown = False
                if board[i][j].lower() == 'r' and board[i][j].islower():
                    up = True
                    left = True
                    right = True
                    down = True
                    for c in range(1, 7):
                        if right == True:
                            if board[i][j+c] == 'K' and j+c < 8:
                                print("Check")
                                check = True
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if left == True:
                            if board[i][j-c] == 'K' and j-c > -1:
                                print("Check")
                                check = True
                            if board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
                        if up == True:
                            if board[i+c][j] == 'K' and i+c < 8:
                                print("Check")
                                check = True
                            if board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if down == True:
                            if board[i-c][j] == 'K' and i-c > 0:
                                print("Check")
                                check = True
                            if board[i-c][j].islower() or board[i-c][j].isupper():
                                down = False
                    if check == True:
                        print("Not Check")
                if board[i][j].lower() == 'q' and board[i][j].islower():
                    upleft = True
                    up = True
                    upright = True
                    right = True
                    downright = True
                    down = True
                    downleft = True
                    left = True

                    for c in range(1, 7):
                        if upleft == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'K':
                                print("Check")
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if upright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                upright = False
                        if right == True:
                            if j+c < 8 and board[i][j+c] == 'K':
                                print("Check")
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if downright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downright = False
                        if down == True:
                            if i-c > -1 and board[i-c][j] == 'K':
                                print("Check")
                            if i-c < 0 or board[i-c][j].islower() or board[i-c][j].isupper():
                                down = False
                        if downleft == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downleft = False
                        if left == True:
                            if j-c > -1 and board[i][j-c] == 'K':
                                print("Check")
                            if j-c < 0 or board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
                if board[i][j].lower() == 'p' and board[i][j].isupper():
                    if i-1 > 0 and j-1 > 0:
                        if board[i-1][j-1] == 'k':
                            print("Check")
                    if i-1 > 0 and j+1 < 8:
                        if board[i-1][j+1] == 'k':
                            print("Check")
                if board[i][j].lower() == 'h' and board[i][j].isupper():
                    if i+2 < 8 and j+1 < 8:
                        if board[i+2][j+1] == 'k':
                            print("Check")
                    if i+2 < 8 and j-1 > 0:
                        if board[i+2][j-1] == 'k':
                            print("Check")
                    if i-2 > 0 and j+1 < 8:
                        if board[i-2][j+1] == 'k':
                            print("Check")
                    if i-2 > 0 and j-1 < 8:
                        if board[i-2][j-1] == 'k':
                            print("Check")
                    if i+1 < 8 and j+2 < 8:
                        if board[i+1][j+2] == 'k':
                            print("Check")
                    if i-1 > 0 and j+2 < 8:
                        if board[i-1][j+2] == 'k':
                            print("Check")
                    if i+1 < 8 and j-2 > 0:
                        if board[i+1][j-2] == 'k':
                            print("Check")
                    if i-1 > 0 and j-2 > 0:
                        if board[i-1][j-2] == 'k':
                            print("Check")
                if board[i][j].lower() == 'b' and board[i][j].isupper():
                    leftup = True
                    leftdown = True
                    rightup = True
                    rightdown = True
                    for c in range(1, 7):
                        if leftup == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False

                        if leftdown == True:
                            if j-c < 0 and i-c < 0 and board[i-c][j-c] == 'k':
                                print("Check")
                            if j-c > 7 or i-c < 0 or board[i-c][j-c].islower() or board[i-c][j-c].isupper():
                                leftdown = False

                        if rightup == True:
                            if j+c < 8 and i+c < 8 and board[i+c][j+c] == 'k':
                                print("Check")
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].islower() or board[i+c][j+c].isupper():
                                rightup = False

                        if rightdown == True:
                            if j+c < 8 and i-c > 0 and board[i-c][j+c] == 'k':
                                print("Check")
                            if j+c > 7 or i-c < 0 and board[i-c][j+c].islower() or board[i-c][j+c].isupper():
                                rightdown = False
                if board[i][j].lower() == 'r' and board[i][j].isupper():
                    up = True
                    left = True
                    right = True
                    down = True
                    for c in range(1, 7):
                        if right == True:
                            if j+c < 8 and board[i][j+c] == 'k':
                                print("Check")
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if left == True:
                            if board[i][j-c] == 'k' and j-c > -1:
                                print("Check")
                            if board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'k':
                                print("Check")
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if down == True:
                            if board[i-c][j] == 'k' and i-c > 0:
                                print("Check")
                            if i-c < 0 or board[i-c][j].islower() or board[i-c][j].isupper():
                                down = False
                if board[i][j].lower() == 'q' and board[i][j].isupper():
                    upleft = True
                    up = True
                    upright = True
                    right = True
                    downright = True
                    down = True
                    downleft = True
                    left = True

                    for c in range(1, 7):
                        if upleft == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'k':
                                print("Check")
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if upright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                upright = False
                        if right == True:
                            if j+c < 8 and board[i][j+c] == 'k':
                                print("Check")
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if downright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downright = False
                        if down == True:
                            if i-c > -1 and board[i-c][j] == 'k':
                                print("Check")
                            if i-c < 0 or board[i-c][j].islower() or board[i-c][j].isupper():
                                down = False
                        if downleft == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downleft = False
                        if left == True:
                            if j-c > -1 and board[i][j-c] == 'k':
                                print("Check")
                            if j-c < 0 or board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
        return check

    def kingcheckmate(self, board):
        checkmate = False
        for i in range(len(board)):
            for j in range(len(board)):
                # if board[i][j].lower() == 'p' and board[i][j].islower():
                #     if i+1 < 8 and j-1 > 0:
                #         if board[i+1][j-1] == 'K':
                #             print("Check")
                #     if i+1 < 8 and j+1 < 8:
                #         if board[i+1][j+1] == 'K':
                #             print("Check")
                # if board[i][j].lower() == 'h' and board[i][j].islower():
                #     if i+2 < 8 and j+1 < 8:
                #         if board[i+2][j+1] == 'K':
                #             print("Check")
                #     if i+2 < 8 and j-1 > 0:
                #         if board[i+2][j-1] == 'K':
                #             print("Check")
                #     if i-2 > 0 and j+1 < 8:
                #         if board[i-2][j+1] == 'K':
                #             print("Check")
                #     if i-2 > 0 and j-1 < 8:
                #         if board[i-2][j-1] == 'K':
                #             print("Check")
                #     if i+1 < 8 and j+2 < 8:
                #         if board[i+1][j+2] == 'K':
                #             print("Check")
                #     if i-1 > 0 and j+2 < 8:
                #         if board[i-1][j+2] == 'K':
                #             print("Check")
                #     if i+1 < 8 and j-2 > 0:
                #         if board[i+1][j-2] == 'K':
                #             print("Check")
                #     if i-1 > 0 and j-2 > 0:
                #         if board[i-1][j-2] == 'K':
                #             print("Check")
                # if board[i][j].lower() == 'b' and board[i][j].islower():
                #     leftup = True
                #     leftdown = True
                #     rightup = True
                #     rightdown = True
                #     for c in range(1, 7):
                #         if leftup == True:
                #             if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                #                 print("Check")
                #             if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                #                 leftup = False

                #         if leftdown == True:
                #             if j-c < 0 and i-c < 0 and board[i-c][j-c] == 'K':
                #                 print("Check")
                #             if j-c > 7 or i-c < 0 or board[i-c][j-c].islower() or board[i-c][j-c].isupper():
                #                 leftdown = False

                #         if rightup == True:
                #             if j+c < 8 and i+c < 8 and board[i+c][j+c] == 'K':
                #                 print("Check")
                #             if j+c > 7 or i+c > 7 or board[i+c][j+c].islower() or board[i+c][j+c].isupper():
                #                 rightup = False

                #         if rightdown == True:
                #             if j+c < 8 and i-c > 0 and board[i-c][j+c] == 'K':
                #                 print("Check")
                #             if j+c > 7 or i-c < 0 and board[i-c][j+c].islower() or board[i-c][j+c].isupper():
                #                 rightdown = False
                # if board[i][j].lower() == 'r' and board[i][j].islower():
                #     up = True
                #     left = True
                #     right = True
                #     down = True
                #     for c in range(1, 7):
                #         if right == True:
                #             if j+c > 7 or board[i][j+c].islower():
                #                 right = False
                #                 cl.checkboard[i][j+c] = 'R'
                #                 print(cl.checkboard)
                #                 if cl.kingcheck(cl.checkboard) == False:
                #                     print("Checking!")
                #             elif j+c > 7 or board[i][j+c].isupper():
                #                 right = False
                #             else:
                #                 cl.checkboard[i][j+c] = 'R'
                #                 if cl.kingcheck(cl.checkboard) == False:
                #                     print("Checking!")
                #             cl.checkboard = board
                #         if left == True:
                #             if j-c < 0 or board[i][j-c].islower():
                #                 right = False
                #                 cl.checkboard[i][j-c] = 'R'
                #                 if cl.kingcheck(cl.checkboard) == False:
                #                     print("Checking!")
                #             if j-c < 0 or board[i][j-c].isupper():
                #                 right = False
                #             else:
                #                 cl.checkboard[i][j-c] = 'R'
                #                 if cl.kingcheck(cl.checkboard) == False:
                #                     print("Checking!")
                #             cl.checkboard = board
                #         if up == True:
                #             if i+c > 7 or board[i+c][j].islower():
                #                 right = False
                #                 cl.checkboard[i+c][j] = 'R'
                #                 if cl.kingcheck(cl.checkboard) == False:
                #                     print("Checking!")
                #             if i+c > 7 or board[i+c][j].isupper():
                #                 right = False
                #             else:
                #                 cl.checkboard[i+c][j] = 'R'
                #                 if cl.kingcheck(cl.checkboard) == False:
                #                     print("Checking!")
                #             cl.checkboard = board
                #         if down == True:
                #             if i-c < 0 or board[i-c][j].islower():
                #                 right = False
                #                 cl.checkboard[i-c][j] = 'R'
                #                 if cl.kingcheck(cl.checkboard) == False:
                #                     print("Checking!")
                #             if i-c < 0 or board[i][j+c].isupper():
                #                 right = False
                #             else:
                #                 cl.checkboard[i-c][j] = 'R'
                #                 if cl.kingcheck(cl.checkboard) == False:
                #                     print("Checking!")
                #             cl.checkboard = board
                # if board[i][j].lower() == 'q' and board[i][j].islower():
                #     upleft = True
                #     up = True
                #     upright = True
                #     right = True
                #     downright = True
                #     down = True
                #     downleft = True
                #     left = True

                #     for c in range(1, 7):
                #         if upleft == True:
                #             if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                #                 print("Check")
                #             if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                #                 leftup = False
                #         if up == True:
                #             if i+c < 8 and board[i+c][j] == 'K':
                #                 print("Check")
                #             if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                #                 up = False
                #         if upright == True:
                #             if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                #                 print("Check")
                #             if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                #                 upright = False
                #         if right == True:
                #             if j+c < 8 and board[i][j+c] == 'K':
                #                 print("Check")
                #             if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                #                 right = False
                #         if downright == True:
                #             if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                #                 print("Check")
                #             if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                #                 downright = False
                #         if down == True:
                #             if i-c > -1 and board[i-c][j] == 'K':
                #                 print("Check")
                #             if i-c < 0 or board[i-c][j].islower() or board[i-c][j].isupper():
                #                 down = False
                #         if downleft == True:
                #             if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                #                 print("Check")
                #             if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                #                 downleft = False
                #         if left == True:
                #             if j-c > -1 and board[i][j-c] == 'K':
                #                 print("Check")
                #             if j-c < 0 or board[i][j-c].islower() or board[i][j-c].isupper():
                #                 left = False
                if board[i][j].lower() == 'p' and board[i][j].isupper():
                    if i-1 < 0 or board[i-1][j] == "-":
                        cl.checkboard[i-1][j] = 'P'
                        cl.printboard(cl.checkboard)
                        if cl.kingcheck(cl.checkboard) == False:
                            print("Checking!")
                        cl.checkboard[i-1][j] = board[i-1][j]
                    if j-1 > 0 and i-1 > 0 and board[i-1][j-1].islower():
                        cl.checkboard[i-1][j-1] = 'P'
                        cl.printboard(cl.checkboard)
                        if cl.kingcheck(cl.checkboard) == False:
                            print("Checking!")
                        cl.checkboard[i-1][j-1] = board[i-1][j-1]
                    if j+1 < 7 and i-1 > 0 and board[i-1][j+1].islower():
                        cl.checkboard[i-1][j+1] = 'P'
                        cl.printboard(cl.checkboard)
                        if cl.kingcheck(cl.checkboard) == False:
                            print("Checking!")
                        cl.checkboard[i-1][j+1] = board[i-1][j+1]
                if board[i][j].lower() == 'h' and board[i][j].isupper():
                    if i+2 < 8 and j+1 < 8:
                        if not board[i+2][j+1].isupper():
                            cl.checkboard[i+2][j+1] = 'H'
                            cl.printboard(cl.checkboard)
                            if cl.kingcheck(cl.checkboard) == False:
                                print("Checking!")
                        cl.checkboard[i+2][j+1] = board[i+2][j+1]
                    if i+2 < 8 and j-1 > 0:
                        if not board[i+2][j-1].isupper():
                            cl.checkboard[i+2][j-1] = 'H'
                            cl.printboard(cl.checkboard)
                            if cl.kingcheck(cl.checkboard) == False:
                                print("Checking!")
                        cl.checkboard[i+2][j-1] = board[i+2][j-1]
                    if i-2 > 0 and j+1 < 8:
                        if not board[i-2][j+1].isupper():
                            cl.checkboard[i-2][j+1] = 'H'
                            cl.printboard(cl.checkboard)
                            if cl.kingcheck(cl.checkboard) == False:
                                print("Checking!")
                        cl.checkboard[i-2][j+1] = board[i-2][j+1]
                    if i-2 > 0 and j-1 < 8:
                        if not board[i-2][j-1].isupper():
                            cl.checkboard[i-2][j-1] = 'H'
                            cl.printboard(cl.checkboard)
                            if cl.kingcheck(cl.checkboard) == False:
                                print("Checking!")
                        cl.checkboard[i-2][j-1] = board[i-2][j-1]
                    if i+1 < 8 and j+2 < 8:
                        if not board[i+1][j+2].isupper():
                            cl.checkboard[i+1][j+2] = 'H'
                            cl.printboard(cl.checkboard)
                            if cl.kingcheck(cl.checkboard) == False:
                                print("Checking!")
                        cl.checkboard[i+1][j+2] = board[i+1][j+2]
                    if i-1 > 0 and j+2 < 8:
                        if not board[i-1][j+2].isupper():
                            cl.checkboard[i-1][j+2] = 'H'
                            cl.printboard(cl.checkboard)
                            if cl.kingcheck(cl.checkboard) == False:
                                print("Checking!")
                        cl.checkboard[i-1][j+2] = board[i-1][j+2]
                    if i+1 < 8 and j-2 > 0:
                        if not board[i+1][j-2].isupper():
                            cl.checkboard[i+1][j-2] = 'H'
                            cl.printboard(cl.checkboard)
                            if cl.kingcheck(cl.checkboard) == False:
                                print("Checking!")
                        cl.checkboard[i+1][j-2] = board[i+1][j-2]
                    if i-1 > 0 and j-2 > 0:
                        if not board[i-1][j-2].isupper():
                            cl.checkboard[i-1][j-2] = 'H'
                            cl.printboard(cl.checkboard)
                            if cl.kingcheck(cl.checkboard) == False:
                                print("Checking!")
                        cl.checkboard[i-1][j-2] = board[i-1][j-2]
                if board[i][j].lower() == 'b' and board[i][j].isupper():
                    leftup = True
                    leftdown = True
                    rightup = True
                    rightdown = True
                    for c in range(1, 7):
                        if leftup == True:
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].isupper():
                                leftup = False
                            elif board[i+c][j-c].islower():
                                leftup = False
                                cl.checkboard[i+c][j-c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j-c] = '-'
                            else:
                                cl.checkboard[i+c][j-c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j-c] = '-'

                        if leftdown == True:
                            if j-c < 0 or i-c < 0 or board[i-c][j-c].isupper():
                                leftdown = False
                            elif board[i-c][j-c].islower():
                                leftdown = False
                                cl.checkboard[i-c][j-c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j-c] = '-'
                            else:
                                cl.checkboard[i-c][j-c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j-c] = '-'

                        if rightup == True:
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].isupper():
                                rightup = False
                            elif board[i+c][j+c].islower():
                                rightup = False
                                cl.checkboard[i+c][j+c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j+c] = '-'
                            else:
                                cl.checkboard[i+c][j+c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j+c] = '-'

                        if rightdown == True:
                            if j+c > 7 or i-c < 0 or board[i-c][j+c].isupper():
                                rightdown = False
                            elif board[i-c][j+c].islower():
                                rightdown = False
                                cl.checkboard[i-c][j+c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j+c] = '-'
                            else:
                                cl.checkboard[i-c][j+c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j+c] = '-'
                if board[i][j].lower() == 'r' and board[i][j].isupper():
                    up = True
                    left = True
                    right = True
                    down = True
                    for c in range(1, 7):
                        if right == True:
                            if j+c > 7 or board[i][j+c].isupper():
                                right = False
                            elif board[i][j+c].islower():
                                right = False
                                cl.checkboard[i][j+c] = 'R'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i][j+c] = '-'
                            else:
                                cl.checkboard[i][j+c] = 'R'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i][j+c] = '-'
                        if left == True:
                            if j-c < 0 or board[i][j-c].isupper():
                                left = False
                            elif board[i][j-c].islower():
                                left = False
                                cl.checkboard[i][j-c] = 'R'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i][j-c] = '-'
                            else:
                                cl.checkboard[i][j-c] = 'R'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i][j-c] = '-'
                        if up == True:
                            if i+c > 7 or board[i+c][j].isupper():
                                up = False
                            elif board[i+c][j].islower():
                                up = False
                                cl.checkboard[i+c][j] = 'R'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j] = '-'
                            else:
                                cl.checkboard[i+c][j] = 'R'
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j] = '-'
                        if down == True:
                            if i-c < 0 or board[i-c][j].isupper():
                                down = False
                            elif board[i-c][j].islower():
                                down = False
                                cl.checkboard[i-c][j] = 'R'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j] = '-'
                            else:
                                cl.checkboard[i-c][j] = 'R'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j] = '-'
                if board[i][j].lower() == 'q' and board[i][j].isupper():
                    leftup = True
                    up = True
                    rightup = True
                    right = True
                    rightdown = True
                    down = True
                    leftdown = True
                    left = True

                    for c in range(1, 7):
                        if right == True:
                            if j+c > 7 or board[i][j+c].isupper():
                                right = False
                            elif board[i][j+c].islower():
                                right = False
                                cl.checkboard[i][j+c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i][j+c] = board[i][j+c]
                            else:
                                cl.checkboard[i][j+c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i][j+c] = board[i][j+c]
                        if left == True:
                            if j-c < 0 or board[i][j-c].isupper():
                                left = False
                            elif board[i][j-c].islower():
                                left = False
                                cl.checkboard[i][j-c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i][j-c] = board[i][j-c]
                            else:
                                cl.checkboard[i][j-c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i][j-c] = board[i][j-c]
                        if up == True:
                            if i+c > 7 or board[i+c][j].isupper():
                                up = False
                            elif board[i+c][j].islower():
                                up = False
                                cl.checkboard[i+c][j] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j] = board[i+c][j]
                            else:
                                cl.checkboard[i+c][j] = 'Q'
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j] = board[i+c][j]
                        if down == True:
                            if i-c < 0 or board[i-c][j].isupper():
                                down = False
                            elif board[i-c][j].islower():
                                down = False
                                cl.checkboard[i-c][j] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j] = board[i-c][j]
                            else:
                                cl.checkboard[i-c][j] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j] = board[i-c][j]
                        if leftup == True:
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].isupper():
                                leftup = False
                            elif board[i+c][j-c].islower():
                                leftup = False
                                cl.checkboard[i+c][j-c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j-c] = board[i+c][j-c]
                            else:
                                cl.checkboard[i+c][j-c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j-c] = board[i+c][j-c]

                        if leftdown == True:
                            if j-c < 0 or i-c < 0 or board[i-c][j-c].isupper():
                                leftdown = False
                            elif board[i-c][j-c].islower():
                                leftdown = False
                                cl.checkboard[i-c][j-c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j-c] = board[i-c][j-c]
                            else:
                                cl.checkboard[i-c][j-c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j-c] = board[i-c][j-c]

                        if rightup == True:
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].isupper():
                                rightup = False
                            elif board[i+c][j+c].islower():
                                rightup = False
                                cl.checkboard[i+c][j+c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j+c] = board[i+c][j+c]
                            else:
                                cl.checkboard[i+c][j+c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i+c][j+c] = board[i+c][j+c]

                        if rightdown == True:
                            if j+c > 7 or i-c < 0 or board[i-c][j+c].isupper():
                                rightdown = False
                            elif board[i-c][j+c].islower():
                                rightdown = False
                                cl.checkboard[i-c][j+c] = 'Q'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j+c] = board[i-c][j+c]
                            else:
                                cl.checkboard[i-c][j+c] = 'B'
                                cl.printboard(cl.checkboard)
                                if cl.kingcheck(cl.checkboard) == False:
                                    print("Checking!")
                                cl.checkboard[i-c][j+c] = board[i-c][j+c]
        return


cl = Chess()
cl.kingcheckmate(cl.board)
cl.kingcheck(cl.board)
# cl.printboard(cl.board)
#cl.playerturn(True, True, cl.board)
