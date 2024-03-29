from king_incheck import *
from chess_helper import *
from boardstate import *


class PieceMovement:
    def __init__(self):
        self.boardstate = Board()
        self.king_incheck = KingCheckVerify()
        self.chess_helper = Chess_Helper()

    def pawnmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
        currentpiece = board[y1_axis][x1_axis]

        # black piece
        if board[y1_axis][x1_axis].islower():
            if board[y2_axis][x2_axis].isupper() and y2_axis == y1_axis+1 and (x2_axis == x1_axis + 1 or x2_axis == x1_axis - 1):
                board[y1_axis][x1_axis] = '-'
                board[y2_axis][x2_axis] = currentpiece
            elif y1_axis == 1 and pathlength == 2 and x1_axis == x2_axis and board[y1_axis+1][x1_axis] == '-' and board[y1_axis+2][x1_axis] == '-':
                board[y1_axis][x1_axis] = '-'
                board[y2_axis][x2_axis] = currentpiece
            elif pathlength == 1 and board[y1_axis+1][x1_axis] == '-' and x2_axis == x1_axis:
                board[y1_axis][x1_axis] = '-'
                board[y2_axis][x2_axis] = currentpiece
            else:
                input("Invalid move. Please input a new move.2")
                return False
            # if self.king_incheck.kingcheck(self.boardstate.board, False) == True:
            #     print("Player 1 king is in check")
        self.boardstate.printboard(self.boardstate.board)
        # white piece
        if board[y1_axis][x1_axis].isupper():
            if board[y2_axis][x2_axis].islower() and y2_axis == y1_axis-1 and (x2_axis == x1_axis + 1 or x2_axis == x1_axis - 1):
                board[y1_axis][x1_axis] = '-'
                board[y2_axis][x2_axis] = currentpiece
            elif y1_axis == 6 and pathlength == 2 and x1_axis == x2_axis and board[y1_axis-1][x1_axis] == '-' and board[y1_axis-2][x1_axis] == '-':
                board[y1_axis][x1_axis] = '-'
                board[y2_axis][x2_axis] = currentpiece
            elif pathlength == 1 and board[y1_axis-1][x1_axis] == '-' and x2_axis == x1_axis:
                board[y1_axis][x1_axis] = '-'
                board[y2_axis][x2_axis] = currentpiece
            else:
                input("Invalid move. Please input a new move.2")
                return False
            # if self.king_incheck.kingcheck(self.boardstate.board, False) == True:
            #     print("Player 2 king is in check")
        self.boardstate.printboard(self.boardstate.board)

    # Done
    def bishopmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
        incx, incy = self.chess_helper.sign(
            x2_axis-x1_axis), self.chess_helper.sign(y2_axis-y1_axis)
        if (incx == 0 or incy == 0):
            input("Invalid move. Please input a new move.0")
            self.boardstate.printboard(board)
            return False

        x, y = x1_axis, y1_axis
        print(incx, incy)
        for i in range(1, pathlength):
            x += incx
            y += incy
            print(y+1, x+1)
            if (board[y][x] == "-" and (y != y2_axis and x != x2_axis)):
                continue
            else:
                input("Invalid move. Please input a new move.1")
                self.boardstate.printboard(board)
                return False
        self.boardstate.printboard(board)

        if board[y1_axis][x1_axis].isupper():
            if board[y2_axis][x2_axis].islower() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
                # if self.king_incheck.kingcheck(self.boardstate.board) == True:
                #     print("Player 2 king is in check")
            else:
                print("Invalid move. Please input a new move.2")
                self.boardstate.printboard(board)
                return False
        elif board[y1_axis][x1_axis].islower():
            if board[y2_axis][x2_axis].isupper() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
                # if self.king_incheck.kingcheck(self.boardstate.board) == True:
                #     print("Player 1 king is in check")
            else:
                print("Invalid move. Please input a new move.2")
                self.boardstate.printboard(board)
                return False

    # Done
    def knightmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        if (abs(x1_axis - x2_axis) == 1 and abs(y1_axis - y2_axis) == 2) or (abs(x1_axis - x2_axis) == 2 and abs(y1_axis - y2_axis) == 1):
            if(board[y1_axis][x1_axis].isupper()):
                if(board[y2_axis][x2_axis] == "-" or board[y2_axis][x2_axis].islower()):
                    board[y2_axis][x2_axis] = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    self.boardstate.printboard(board)
                    # if self.king_incheck.kingcheck(self.boardstate.board, False) == True:
                    #     input("Player 2 king is in check")
            elif(board[y1_axis][x1_axis].islower()):
                if(board[y2_axis][x2_axis] == "-" or board[y2_axis][x2_axis].isupper()):
                    board[y2_axis][x2_axis] = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    self.boardstate.printboard(board)
                    # if self.king_incheck.kingcheck(self.boardstate.board, False) == True:
                    #     input("Player 1 king is in check")
            else:
                input("Invalid target.")
                self.boardstate.printboard(board)
                return False
        self.boardstate.printboard(board)
        return

    # Done
    def rookmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        while x1_axis != x2_axis and y1_axis != y2_axis:
            print("Please input a valid move coordinate.")
            coordinate2 = input("Where is the piece moving to?: ")
            y2_axis = self.coordYhelper(coordinate2)
            x2_axis = self.coordXhelper(coordinate2)

        pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
        incx, incy = self.chess_helper.sign(
            x2_axis-x1_axis), self.chess_helper.sign(y2_axis-y1_axis)
        x, y = x1_axis, y1_axis

        for i in range(1, pathlength):
            x += incx
            y += incy
            if (board[y][x] == "-" and (y == y2_axis or x == x2_axis)):
                continue
            else:
                print("Invalid move. Please input a new move.")
                self.boardstate.printboard(board)
                return False

        if board[y1_axis][x1_axis].isupper():
            if board[y2_axis][x2_axis].islower() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
                # if self.king_incheck.kingcheck(self.boardstate.board) == True:
                #     print("Player 2 king is in check")
            else:
                print("Invalid move. Please input a new move.")
                self.boardstate.printboard(board)
                return False
        else:
            if board[y2_axis][x2_axis].isupper() or board[y2_axis][x2_axis] == "-":
                currentpiece = board[y1_axis][x1_axis]
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
                # if self.king_incheck.kingcheck(self.boardstate.board) == True:
                #     print("Player 1 king is in check")
            else:
                print("Invalid move. Please input a new move.")
                self.boardstate.printboard(board)
                return False
        self.boardstate.printboard(board)

    # Done
    def queenmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        #Diagonal
        if abs(x1_axis - x2_axis) == abs(y1_axis - y2_axis):

            pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
            incx, incy = self.chess_helper.sign(
                x2_axis-x1_axis), self.chess_helper.sign(y2_axis-y1_axis)
            x, y = x1_axis, y1_axis

            for i in range(1, pathlength):
                x += incx
                y += incy
                if (board[y][x] == "-" and (y == y2_axis or x == x2_axis)):
                    continue
                else:
                    print("Invalid move. Please input a new move.")
                    self.boardstate.printboard(board)
                    return False

            if board[y1_axis][x1_axis].isupper():
                if board[y2_axis][x2_axis].islower() or board[y2_axis][x2_axis] == "-":
                    currentpiece = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    board[y2_axis][x2_axis] = currentpiece
                    # if self.king_incheck.kingcheck(self.boardstate.board) == True:
                    #     print("Player 2 king is in check")
                else:
                    print("Invalid move. Please input a new move.")
                    self.boardstate.printboard(board)
                    return False
            else:
                if board[y2_axis][x2_axis].isupper() or board[y2_axis][x2_axis] == "-":
                    currentpiece = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    board[y2_axis][x2_axis] = currentpiece
                    # if self.king_incheck.kingcheck(self.boardstate.board) == True:
                    #     print("Player 1 king is in check")
                else:
                    print("Invalid move. Please input a new move.")
                    self.boardstate.printboard(board)
                    return False
            self.boardstate.printboard(board)
        #Horizontal, Vertical
        elif x1_axis == x2_axis or y1_axis == y2_axis:
            pathlength = max(abs(y1_axis - y2_axis), abs(x1_axis - x2_axis))
            incx, incy = self.chess_helper.sign(
                x2_axis-x1_axis), self.chess_helper.sign(y2_axis-y1_axis)
            x, y = x1_axis, y1_axis

            if(x1_axis == x2_axis or y1_axis == y2_axis):
                for i in range(1, pathlength):
                    x += incx
                    y += incy
                    if (board[y][x] == "-" and (y == y2_axis or x == x2_axis)):
                        continue
                    else:
                        input("Invalid move. Please input a new move.0")
                        self.boardstate.printboard(board)
                        return False
            else:
                for i in range(1, pathlength):
                    x += incx
                    y += incy
                    print(y+1, x+1)
                    if (board[y][x] == "-" and (y != y2_axis and x != x2_axis)):
                        continue
                    else:
                        input("Invalid move. Please input a new move.0")
                        self.boardstate.printboard(board)
                        return False
            if board[y1_axis][x1_axis].isupper():
                if board[y2_axis][x2_axis].islower() or board[y2_axis][x2_axis] == "-":
                    currentpiece = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    board[y2_axis][x2_axis] = currentpiece
                    # if self.king_incheck.kingcheck(self.boardstate.board, False) == True:
                    #     print("Player 2 king is in check")
                else:
                    input("Invalid move. Please input a new move.0")
                    self.boardstate.printboard(board)
                    return False
            elif board[y1_axis][x1_axis].islower():
                if board[y2_axis][x2_axis].isupper() or board[y2_axis][x2_axis] == "-":
                    currentpiece = board[y1_axis][x1_axis]
                    board[y1_axis][x1_axis] = "-"
                    board[y2_axis][x2_axis] = currentpiece
                    # if self.king_incheck.kingcheck(self.boardstate.board, False) == True:
                    #     print("Player 1 king is in check")
                else:
                    input("Invalid move. Please input a new move.0")
                    self.boardstate.printboard(board)
                    return False
            self.boardstate.printboard(board)
        else:
            input("Invalid move. Please input a new move.0")
            self.boardstate.printboard(board)
            return False

    # Not Done
    def kingmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
        currentpiece = board[y1_axis][x1_axis]
        nextpiece = board[y2_axis][x2_axis]
        if (abs(y1_axis-y2_axis) == 1 and abs(x1_axis - x2_axis) == 0) or (abs(y1_axis-y2_axis) == 1 and abs(x1_axis - x2_axis) == 1) or (abs(y1_axis-y2_axis) == 0 and abs(x1_axis - x2_axis) == 1):
            if board[y2_axis][x2_axis] == "-" or board[y2_axis][x2_axis].islower() and board[y1_axis][x1_axis].isupper():
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
                # if self.king_incheck.kingcheck(self.boardstate.board, False) == True:
                #     print("Player 2 king is in check")
                if self.chess_helper.doubleking(y2_axis, x2_axis, self.boardstate.board) == True:
                    board[y1_axis][x1_axis] = currentpiece
                    board[y2_axis][x2_axis] = nextpiece
                    return False
            elif board[y2_axis][x2_axis] == "-" or board[y2_axis][x2_axis].isupper() and board[y1_axis][x1_axis].islower():
                board[y1_axis][x1_axis] = "-"
                board[y2_axis][x2_axis] = currentpiece
                # if self.king_incheck.kingcheck(self.boardstate.board, False) == True:
                #     print("Player 2 king is in check")
                if self.chess_helper.doubleking(y2_axis, x2_axis, self.boardstate.board) == True:
                    board[y1_axis][x1_axis] = currentpiece
                    board[y2_axis][x2_axis] = nextpiece
                    return False
            else:
                self.boardstate.printboard(board)
        else:
            print("Invalid Move. 2")
            self.boardstate.printboard(board)
            return False
