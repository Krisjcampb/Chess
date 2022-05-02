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
		print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in board]))
		c.playerturn(True, True, board)

	def playerturn(self, turn, game, board):
		while game == True:
			if turn is True:
				turn = not turn
				c.player1move(board, turn, game)
			if turn is False:
				turn = not turn
				c.player2move(board, turn, game)
	
	def player1move(self, board, turn, game):
		#input move using chess coordinates
		coordinate1 = input("What piece would you like to move?: ")
		y_axis = ord(coordinate1[0].upper())-64
		x_axis = int(coordinate1[1])-1
		currentpiece = board[abs(y_axis - 8)][x_axis]
		print(currentpiece)

		#check valid input
		#board mutation
		print("white")
		c.playerturn(turn, board, game)
		
	def player2move(self, board, turn, game):
		print("black")
		c.playerturn(turn, board, game)



c = Chess()
c.printboard(c.board)