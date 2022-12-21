import os
import math
import copy
import sys

from chess_helper import Chess_Helper
from king_incheck import KingCheckVerify
from piece_moves import PieceMovement
from boardstate import Board


class Chess:
    def __init__(self):
        self.boardstate = Board()
        self.chess_helper = Chess_Helper()
        self.king_incheck = KingCheckVerify()
        self.piece_moves = PieceMovement()
        self.boardstate.printboard(self.boardstate.board)

    def startgame(self):
        cl.playerturn(True, True, self.boardstate.board)

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
            if coordinate1[0].isalpha() and coordinate1[1].isnumeric() and len(coordinate1) == 2:
                y_axis = abs((ord(coordinate1[0].upper())-64)-8)
                x_axis = int(coordinate1[1])-1
            else:
                return self.player1move(board, turn, game)
            if y_axis > 7 or x_axis > 7 or y_axis < 0 or x_axis < 0:
                print(y_axis, x_axis)
                return self.player1move(board, turn, game)

            currentpiece = board[y_axis][x_axis]
            if currentpiece.isupper():
                break
            else:
                return self.player1move(board, turn, game)

        print(currentpiece)
        cl.movevalidation(board, coordinate1, currentpiece)
        cl.playerturn(turn, board, game)

    def player2move(self, board, turn, game):
        while True:
            coordinate1 = input("What black piece would you like to move?: ")
            if coordinate1[0].isalpha() and coordinate1[1].isnumeric() and len(coordinate1) == 2:
                y_axis = abs((ord(coordinate1[0].upper())-64)-8)
                x_axis = int(coordinate1[1])-1
            else:
                return self.player2move(board, turn, game)
            if y_axis > 7 or x_axis > 7 or y_axis < 0 or x_axis < 0:
                print(y_axis, x_axis)
                return self.player2move(board, turn, game)

            currentpiece = board[y_axis][x_axis]
            if currentpiece.islower():
                break
            else:
                return self.player2move(board, turn, game)
        print(currentpiece)
        cl.movevalidation(board, coordinate1, currentpiece)
        cl.playerturn(turn, board, game)

    def movevalidation(self, board, coordinate1, currentpiece):
        while True:
            coordinate2 = input("Where is the piece moving to?: ")

            y1_axis = self.chess_helper.coordYhelper(coordinate1)
            x1_axis = self.chess_helper.coordXhelper(coordinate1)

            y2_axis = self.chess_helper.coordYhelper(coordinate2)
            x2_axis = self.chess_helper.coordXhelper(coordinate2)
            origpiece = board[y1_axis][x1_axis]
            nextpiece = board[y2_axis][x2_axis]
            board[y2_axis][x2_axis] = origpiece
            board[y1_axis][x1_axis] = "-"

            #White Check
            if origpiece.isupper():
                if self.king_incheck.kingcheck(self.boardstate.board, False) == [True, True, False]:
                    board[y2_axis][x2_axis] = nextpiece
                    board[y1_axis][x1_axis] = origpiece
                    self.boardstate.printboard(board)
                    cl.playerturn(True, True, board)
            #Black Check
            elif origpiece.islower():
                if self.king_incheck.kingcheck(self.boardstate.board, False) == [True, False, True]:
                    board[y2_axis][x2_axis] = nextpiece
                    board[y1_axis][x1_axis] = origpiece
                    self.boardstate.printboard(board)
                    cl.playerturn(False, True, board)
            #Both in Check
            elif self.king_incheck.kingcheck(self.boardstate.board, False) == [True, True, True]:
                input("hello")
                board[y2_axis][x2_axis] = nextpiece
                board[y1_axis][x1_axis] = origpiece
                if board[y1_axis][x1_axis].isupper():
                    cl.playerturn(True, True, board)
                else:
                    cl.playerturn(False, True, board)
            board[y2_axis][x2_axis] = nextpiece
            board[y1_axis][x1_axis] = origpiece

            if currentpiece.lower() == "p":
                if (currentpiece.islower() and self.piece_moves.pawnmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player2move(board, False, True)
                elif(currentpiece.isupper() and self.piece_moves.pawnmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player1move(board, True, True)
                break

            if currentpiece.lower() == "h":
                if (currentpiece.islower() and self.piece_moves.knightmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player2move(board, False, True)

                if(currentpiece.isupper() and self.piece_moves.knightmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player1move(board, True, True)
                break

            if currentpiece.lower() == "b":
                if (currentpiece.islower() and self.piece_moves.bishopmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player2move(board, False, True)
                if(currentpiece.isupper() and self.piece_moves.bishopmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player1move(board, True, True)
                break

            if currentpiece.lower() == "r":
                if (currentpiece.islower() and self.piece_moves.rookmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player2move(board, False, True)
                if(currentpiece.isupper() and self.piece_moves.rookmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player1move(board, True, True)
                break

            if currentpiece.lower() == "k":
                if (currentpiece.islower() and self.piece_moves.kingmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player2move(board, False, True)
                if (currentpiece.isupper() and self.piece_moves.kingmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player1move(board, True, True)
                break

            if currentpiece.lower() == "q":
                if (currentpiece.islower() and self.piece_moves.queenmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player2move(board, False, True)
                if(currentpiece.isupper() and self.piece_moves.queenmove(y1_axis, x1_axis, y2_axis, x2_axis, board) == False):
                    return self.player1move(board, True, True)
                break


cl = Chess()
cl.startgame()
