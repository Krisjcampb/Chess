import os
import math

class Chess:
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

	def printboard(self, board):
		##os.system("cls")
		print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in board]))

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
			coordinate1 = input("What piece would you like to move?: ")
			y_axis = abs((ord(coordinate1[0].upper())-64)-8)
			x_axis = int(coordinate1[1])-1
			currentpiece = board[y_axis][x_axis]

			if currentpiece.isupper():
				break
			else:
				print("Please input a valid move.")
				
		print(currentpiece)
		c.movevalidation(board, coordinate1, currentpiece)
		c.playerturn(turn, board, game)
		
	def player2move(self, board, turn, game):
		while True:
			coordinate1 = input("What piece would you like to move?: ")
			y_axis = abs((ord(coordinate1[0].upper())-64)-8)
			x_axis = int(coordinate1[1])-1
			currentpiece = board[y_axis][x_axis]

			if currentpiece.islower():
				break
			else:
				print("Please input a valid move.")

		print(currentpiece)
		c.movevalidation(board, coordinate1, currentpiece)
		c.playerturn(turn, board, game)

	def coordYhelper(self, coordinate):
		return abs((ord(coordinate[0].upper())-64)-8)

	def coordXhelper(self, coordinate):
		return int(coordinate[1])-1

	def movevalidation(self, board, coordinate1, currentpiece):
		sign = lambda x: (1, -1)[x<0]
		while True:
			coordinate2 = input("Where is the piece moving to?: ")

			y1_axis = self.coordYhelper(coordinate1)
			x1_axis = self.coordXhelper(coordinate1)

			y2_axis = self.coordYhelper(coordinate2)
			x2_axis = self.coordXhelper(coordinate2)

			if currentpiece.lower() == "p":
				self.pawnmove(y1_axis, x1_axis, y2_axis, x2_axis, board)

			if currentpiece.lower() == "h":
				self.knightmove(y1_axis, x1_axis, y2_axis, x2_axis, board)

			if currentpiece.lower() == "b":
				self.bishopmove(y1_axis, x1_axis, y2_axis, x2_axis, board)

			if currentpiece.lower() == "r":
				self.rookmove(y1_axis, x1_axis, y2_axis, x2_axis, board)

			if currentpiece.lower() == "k":
				self.kingmove(y1_axis, x1_axis, y2_axis, x2_axis, board)

			if currentpiece.lower() == "q":
				self.queenmove(y1_axis, x1_axis, y2_axis, x2_axis, board)
	
	def pawnmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
		sign = lambda x: (1, -1)[x<0]

		pathlength = abs(y1_axis - y2_axis)
		print(abs(x1_axis - x2_axis))
		print(y1_axis, x1_axis, y2_axis, x2_axis)

		incx = sign(x2_axis-x1_axis)
		incy = sign(y2_axis-y1_axis)

		for i in range(1, pathlength):
			x = x1_axis + incx
			y = y1_axis + incy

			if("-" in board(y, x)):
				continue
			else:
				return False
		if("-" in board(x2_axis, y2_axis)):
			return True
		if board.islower(x2_axis, y2_axis):
			currentpiece = board[y1_axis][x1_axis]
			board[y1_axis][x1_axis] = "-"
			board[y2_axis][x2_axis] = currentpiece
			c.printboard(board)
	
	def bishopmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
		return
	
	def knightmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
		return
	
	def rookmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
		return
	
	def queenmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
		return
	
	def kingmove(self, y1_axis, x1_axis, y2_axis, x2_axis, board):
		return



c = Chess()
c.printboard(c.board)
c.playerturn(True, True, c.board)