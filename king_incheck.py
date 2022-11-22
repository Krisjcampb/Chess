from boardstate import *

class KingCheckVerify:

    def __init__(self):
        self.boardstate = Board()
    def kingcheck(self, board):
        check = False
        kingtype = "white"
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].lower() == 'p' and board[i][j].islower():
                    if i+1 < 8 and j-1 > 0:
                        if board[i+1][j-1] == 'K':
                            check = True
                            print("Check")
                    if i+1 < 8 and j+1 < 8:
                        if board[i+1][j+1] == 'K':
                            check = True
                            print("Check")
                if board[i][j].lower() == 'h' and board[i][j].islower():
                    if i+2 < 8 and j+1 < 8:
                        if board[i+2][j+1] == 'K':
                            check = True
                            print("Check")
                    if i+2 < 8 and j-1 > 0:
                        if board[i+2][j-1] == 'K':
                            check = True
                            print("Check")
                    if i-2 > 0 and j+1 < 8:
                        if board[i-2][j+1] == 'K':
                            check = True
                            print("Check")
                    if i-2 > 0 and j-1 < 8:
                        if board[i-2][j-1] == 'K':
                            check = True
                            print("Check")
                    if i+1 < 8 and j+2 < 8:
                        if board[i+1][j+2] == 'K':
                            check = True
                            print("Check")
                    if i-1 > 0 and j+2 < 8:
                        if board[i-1][j+2] == 'K':
                            check = True
                            print("Check")
                    if i+1 < 8 and j-2 > 0:
                        if board[i+1][j-2] == 'K':
                            check = True
                            print("Check")
                    if i-1 > 0 and j-2 > 0:
                        if board[i-1][j-2] == 'K':
                            print("Check")
                            return check, True
                if board[i][j].lower() == 'b' and board[i][j].islower():
                    leftup = True
                    leftdown = True
                    rightup = True
                    rightdown = True
                    for c in range(1, 7):
                        if leftup == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False

                        if leftdown == True:
                            if j-c < 0 and i-c < 0 and board[i-c][j-c] == 'K':
                                check = True
                                print("Check")
                            if j-c > 7 or i-c < 0 or board[i-c][j-c].islower() or board[i-c][j-c].isupper():
                                leftdown = False

                        if rightup == True:
                            if j+c < 8 and i+c < 8 and board[i+c][j+c] == 'K':
                                check = True
                                print("Check")
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].islower() or board[i+c][j+c].isupper():
                                rightup = False

                        if rightdown == True:
                            if j+c < 8 and i-c > 0 and board[i-c][j+c] == 'K':
                                check = True
                                print("Check")
                            if j+c > 7 or i-c < 0 and board[i-c][j+c].islower() or board[i-c][j+c].isupper():
                                rightdown = False
                if board[i][j].lower() == 'r' and board[i][j].islower():
                    up = True
                    left = True
                    right = True
                    down = True
                    for c in range(0, 7):
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
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'K':
                                check = True
                                print("Check")
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if upright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                upright = False
                        if right == True:
                            if j+c < 8 and board[i][j+c] == 'K':
                                check = True
                                print("Check")
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if downright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downright = False
                        if down == True:
                            if i-c > -1 and board[i-c][j] == 'K':
                                check = True
                                print("Check")
                            if i-c < 0 or board[i-c][j].islower() or board[i-c][j].isupper():
                                down = False
                        if downleft == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downleft = False
                        if left == True:
                            if j-c > -1 and board[i][j-c] == 'K':
                                check = True
                                print("Check")
                            if j-c < 0 or board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
                if board[i][j].lower() == 'p' and board[i][j].isupper():
                    if i-1 > 0 and j-1 > 0:
                        if board[i-1][j-1] == 'k':
                            check = True
                            print("Check")
                    if i-1 > 0 and j+1 < 8:
                        if board[i-1][j+1] == 'k':
                            check = True
                            print("Check")
                if board[i][j].lower() == 'h' and board[i][j].isupper():
                    if i+2 < 8 and j+1 < 8:
                        if board[i+2][j+1] == 'k':
                            check = True
                            print("Check")
                    if i+2 < 8 and j-1 > -1:
                        if board[i+2][j-1] == 'k':
                            check = True
                            print("Check")
                    if i-2 > -1 and j+1 < 8:
                        if board[i-2][j+1] == 'k':
                            check = True
                            print("Check")
                    if i-2 > -1 and j-1 < 8:
                        if board[i-2][j-1] == 'k':
                            check = True
                            print("Check")
                    if i+1 < 8 and j+2 < 8:
                        if board[i+1][j+2] == 'k':
                            check = True
                            print("Check")
                    if i-1 > -1 and j+2 < 8:
                        if board[i-1][j+2] == 'k':
                            check = True
                            print("Check")
                    if i+1 < 8 and j-2 > -1:
                        if board[i+1][j-2] == 'k':
                            check = True
                            print("Check")
                    if i-1 > -1 and j-2 > -1:
                        if board[i-1][j-2] == 'k':
                            check = True
                            print("Check")
                if board[i][j].lower() == 'b' and board[i][j].isupper():
                    leftup = True
                    leftdown = True
                    rightup = True
                    rightdown = True
                    for c in range(1, 7):
                        if leftup == True:
                            if j-c > -1 and i+c < 8 and board[i+c][j-c] == 'k':
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False

                        if leftdown == True:
                            if j-c > -1 and i-c > -1 and board[i-c][j-c] == 'k':
                                check = True
                                print("Check")
                            if j-c < 0 or i-c < 0 or board[i-c][j-c].islower() or board[i-c][j-c].isupper():
                                leftdown = False

                        if rightup == True:
                            if j+c < 8 and i+c < 8 and board[i+c][j+c] == 'k':
                                check = True
                                print("Check")
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].islower() or board[i+c][j+c].isupper():
                                rightup = False

                        if rightdown == True:
                            if j+c < 8 and i-c > 0 and board[i-c][j+c] == 'k':
                                check = True
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
                                check = True
                                print("Check")
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if left == True:
                            if board[i][j-c] == 'k' and j-c > -1:
                                check = True
                                print("Check")
                            if board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'k':
                                check = True
                                print("Check")
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if down == True:
                            if board[i-c][j] == 'k' and i-c > 0:
                                check = True
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
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'k':
                                check = True
                                print("Check")
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if upright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                upright = False
                        if right == True:
                            if j+c < 8 and board[i][j+c] == 'k':
                                check = True
                                print("Check")
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if downright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downright = False
                        if down == True:
                            if i-c > -1 and board[i-c][j] == 'k':
                                check = True
                                print("Check")
                            if i-c < 0 or board[i-c][j].islower() or board[i-c][j].isupper():
                                down = False
                        if downleft == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                check = True
                                print("Check")
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downleft = False
                        if left == True:
                            if j-c > -1 and board[i][j-c] == 'k':
                                check = True
                                print("Check")
                            if j-c < 0 or board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
        return check

    def kingcheckmate(self, board):
        checkmate = False
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].lower() == 'p' and board[i][j].isupper():
                    if i-1 < 0 or board[i-1][j] == "-":
                        self.boardstate.checkboard[i-1][j] = 'p'
                        self.boardstate.printboard(self.boardstate.checkboard)
                        if self.kingcheck(self.boardstate.checkboard) == False:
                            print("Checking!")
                        self.boardstate.checkboard[i-1][j] = board[i-1][j]
                    if j-1 > 0 and i-1 > 0 and board[i-1][j-1].isupper():
                        self.boardstate.checkboard[i-1][j-1] = 'p'
                        self.boardstate.printboard(self.boardstate.checkboard)
                        if self.kingcheck(self.boardstate.checkboard) == False:
                            print("Checking!")
                        self.boardstate.checkboard[i-1][j-1] = board[i-1][j-1]
                    if j+1 < 7 and i-1 > 0 and board[i-1][j+1].isupper():
                        self.boardstate.checkboard[i-1][j+1] = 'p'
                        self.boardstate.printboard(self.boardstate.checkboard)
                        if self.kingcheck(self.boardstate.checkboard) == False:
                            print("Checking!")
                        self.boardstate.checkboard[i-1][j+1] = board[i-1][j+1]
                if board[i][j].lower() == 'h' and board[i][j].isupper():
                    if i+2 < 8 and j+1 < 8:
                        if not board[i+2][j+1].islower():
                            self.boardstate.checkboard[i+2][j+1] = 'h'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i+2][j+1] = board[i+2][j+1]
                    if i+2 < 8 and j-1 > 0:
                        if not board[i+2][j-1].islower():
                            self.boardstate.checkboard[i+2][j-1] = 'h'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i+2][j-1] = board[i+2][j-1]
                    if i-2 > 0 and j+1 < 8:
                        if not board[i-2][j+1].islower():
                            self.boardstate.checkboard[i-2][j+1] = 'h'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i-2][j+1] = board[i-2][j+1]
                    if i-2 > 0 and j-1 < 8:
                        if not board[i-2][j-1].islower():
                            self.boardstate.checkboard[i-2][j-1] = 'h'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i-2][j-1] = board[i-2][j-1]
                    if i+1 < 8 and j+2 < 8:
                        if not board[i+1][j+2].islower():
                            self.boardstate.checkboard[i+1][j+2] = 'h'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i+1][j+2] = board[i+1][j+2]
                    if i-1 > 0 and j+2 < 8:
                        if not board[i-1][j+2].islower():
                            self.boardstate.checkboard[i-1][j+2] = 'h'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i-1][j+2] = board[i-1][j+2]
                    if i+1 < 8 and j-2 > 0:
                        if not board[i+1][j-2].islower():
                            self.boardstate.checkboard[i+1][j-2] = 'h'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i+1][j-2] = board[i+1][j-2]
                    if i-1 > 0 and j-2 > 0:
                        if not board[i-1][j-2].islower():
                            self.boardstate.checkboard[i-1][j-2] = 'h'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i-1][j-2] = board[i-1][j-2]
                if board[i][j].lower() == 'b' and board[i][j].islower():
                    leftup = True
                    leftdown = True
                    rightup = True
                    rightdown = True
                    for c in range(1, 7):
                        if leftup == True:
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower():
                                leftup = False
                            elif board[i+c][j-c].isupper():
                                leftup = False
                                self.boardstate.checkboard[i+c][j-c] = 'b'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j-c] = board[i+c][j-c]
                            else:
                                self.boardstate.checkboard[i+c][j-c] = 'b'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j-c] = board[i+c][j-c]

                        if leftdown == True:
                            if j-c < 0 or i-c < 0 or board[i-c][j-c].islower():
                                leftdown = False
                            elif board[i-c][j-c].isupper():
                                leftdown = False
                                self.boardstate.checkboard[i-c][j-c] = 'b'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j-c] = board[i-c][j-c]
                            else:
                                self.boardstate.checkboard[i-c][j-c] = 'b'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j-c] = board[i-c][j-c]

                        if rightup == True:
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].islower():
                                rightup = False
                            elif board[i+c][j+c].isupper():
                                rightup = False
                                self.boardstate.checkboard[i+c][j+c] = 'b'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j+c] = board[i+c][j+c]
                            else:
                                self.boardstate.checkboard[i+c][j+c] = 'b'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j+c] = board[i+c][j+c]

                        if rightdown == True:
                            if j+c > 7 or i-c < 0 or board[i-c][j+c].islower():
                                rightdown = False
                            elif board[i-c][j+c].isupper():
                                rightdown = False
                                self.boardstate.checkboard[i-c][j+c] = 'b'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j+c] = board[i-c][j+c]
                            else:
                                self.boardstate.checkboard[i-c][j+c] = 'b'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j+c] = board[i-c][j+c]
                if board[i][j].lower() == 'r' and board[i][j].islower():
                    up = True
                    left = True
                    right = True
                    down = True
                    for c in range(1, 7):
                        if right == True:
                            if j+c > 7 or board[i][j+c].islower():
                                right = False
                            elif board[i][j+c].isupper():
                                right = False
                                self.boardstate.checkboard[i][j+c] = 'r'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j+c] = board[i][j+c]
                            else:
                                self.boardstate.checkboard[i][j+c] = 'r'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j+c] = board[i][j+c]
                        if left == True:
                            if j-c < 0 or board[i][j-c].islower():
                                left = False
                            elif board[i][j-c].isupper():
                                left = False
                                self.boardstate.checkboard[i][j-c] = 'r'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j-c] = board[i][j-c]
                            else:
                                self.boardstate.checkboard[i][j-c] = 'r'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j-c] = board[i][j-c]
                        if up == True:
                            if i+c > 7 or board[i+c][j].islower():
                                up = False
                            elif board[i+c][j].isupper():
                                up = False
                                self.boardstate.checkboard[i+c][j] = 'r'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j] = board[i+c][j]
                            else:
                                self.boardstate.checkboard[i+c][j] = 'r'
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j] = board[i+c][j]
                        if down == True:
                            if i-c < 0 or board[i-c][j].islower():
                                down = False
                            elif board[i-c][j].isupper():
                                down = False
                                self.boardstate.checkboard[i-c][j] = 'r'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j] = board[i-c][j]
                            else:
                                self.boardstate.checkboard[i-c][j] = 'r'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j] = board[i-c][j]
                if board[i][j].lower() == 'q' and board[i][j].islower():
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
                            if j+c > 7 or board[i][j+c].islower():
                                right = False
                            elif board[i][j+c].isupper():
                                right = False
                                self.boardstate.checkboard[i][j+c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j+c] = board[i][j+c]
                            else:
                                self.boardstate.checkboard[i][j+c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j+c] = board[i][j+c]
                        if left == True:
                            if j-c < 0 or board[i][j-c].islower():
                                left = False
                            elif board[i][j-c].isupper():
                                left = False
                                self.boardstate.checkboard[i][j-c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j-c] = board[i][j-c]
                            else:
                                self.boardstate.checkboard[i][j-c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j-c] = board[i][j-c]
                        if up == True:
                            if i+c > 7 or board[i+c][j].islower():
                                up = False
                            elif board[i+c][j].isupper():
                                up = False
                                self.boardstate.checkboard[i+c][j] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j] = board[i+c][j]
                            else:
                                self.boardstate.checkboard[i+c][j] = 'q'
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j] = board[i+c][j]
                        if down == True:
                            if i-c < 0 or board[i-c][j].islower():
                                down = False
                            elif board[i-c][j].isupper():
                                down = False
                                self.boardstate.checkboard[i-c][j] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j] = board[i-c][j]
                            else:
                                self.boardstate.checkboard[i-c][j] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j] = board[i-c][j]
                        if leftup == True:
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower():
                                leftup = False
                            elif board[i+c][j-c].isupper():
                                leftup = False
                                self.boardstate.checkboard[i+c][j-c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j-c] = board[i+c][j-c]
                            else:
                                self.boardstate.checkboard[i+c][j-c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j-c] = board[i+c][j-c]

                        if leftdown == True:
                            if j-c < 0 or i-c < 0 or board[i-c][j-c].islower():
                                leftdown = False
                            elif board[i-c][j-c].isupper():
                                leftdown = False
                                self.boardstate.checkboard[i-c][j-c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j-c] = board[i-c][j-c]
                            else:
                                self.boardstate.checkboard[i-c][j-c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j-c] = board[i-c][j-c]

                        if rightup == True:
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].islower():
                                rightup = False
                            elif board[i+c][j+c].isupper():
                                rightup = False
                                self.boardstate.checkboard[i+c][j+c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j+c] = board[i+c][j+c]
                            else:
                                self.boardstate.checkboard[i+c][j+c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j+c] = board[i+c][j+c]

                        if rightdown == True:
                            if j+c > 7 or i-c < 0 or board[i-c][j+c].islower():
                                rightdown = False
                            elif board[i-c][j+c].isupper():
                                rightdown = False
                                self.boardstate.checkboard[i-c][j+c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j+c] = board[i-c][j+c]
                            else:
                                self.boardstate.checkboard[i-c][j+c] = 'q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j+c] = board[i-c][j+c]
                ##############################################################################################################
                if board[i][j].lower() == 'p' and board[i][j].isupper():
                    if i-1 < 0 or board[i-1][j] == "-":
                        self.boardstate.checkboard[i-1][j] = 'P'
                        self.boardstate.printboard(self.boardstate.checkboard)
                        if self.kingcheck(self.boardstate.checkboard) == False:
                            print("Checking!")
                        self.boardstate.checkboard[i-1][j] = board[i-1][j]
                    if j-1 > 0 and i-1 > 0 and board[i-1][j-1].islower():
                        self.boardstate.checkboard[i-1][j-1] = 'P'
                        self.boardstate.printboard(self.boardstate.checkboard)
                        if self.kingcheck(self.boardstate.checkboard) == False:
                            print("Checking!")
                        self.boardstate.checkboard[i-1][j-1] = board[i-1][j-1]
                    if j+1 < 7 and i-1 > 0 and board[i-1][j+1].islower():
                        self.boardstate.checkboard[i-1][j+1] = 'P'
                        self.boardstate.printboard(self.boardstate.checkboard)
                        if self.kingcheck(self.boardstate.checkboard) == False:
                            print("Checking!")
                        self.boardstate.checkboard[i-1][j+1] = board[i-1][j+1]
                if board[i][j].lower() == 'h' and board[i][j].isupper():
                    if i+2 < 8 and j+1 < 8:
                        if not board[i+2][j+1].isupper():
                            self.boardstate.checkboard[i+2][j+1] = 'H'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i+2][j+1] = board[i+2][j+1]
                    if i+2 < 8 and j-1 > 0:
                        if not board[i+2][j-1].isupper():
                            self.boardstate.checkboard[i+2][j-1] = 'H'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i+2][j-1] = board[i+2][j-1]
                    if i-2 > 0 and j+1 < 8:
                        if not board[i-2][j+1].isupper():
                            self.boardstate.checkboard[i-2][j+1] = 'H'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i-2][j+1] = board[i-2][j+1]
                    if i-2 > 0 and j-1 < 8:
                        if not board[i-2][j-1].isupper():
                            self.boardstate.checkboard[i-2][j-1] = 'H'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i-2][j-1] = board[i-2][j-1]
                    if i+1 < 8 and j+2 < 8:
                        if not board[i+1][j+2].isupper():
                            self.boardstate.checkboard[i+1][j+2] = 'H'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i+1][j+2] = board[i+1][j+2]
                    if i-1 > 0 and j+2 < 8:
                        if not board[i-1][j+2].isupper():
                            self.boardstate.checkboard[i-1][j+2] = 'H'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i-1][j+2] = board[i-1][j+2]
                    if i+1 < 8 and j-2 > 0:
                        if not board[i+1][j-2].isupper():
                            self.boardstate.checkboard[i+1][j-2] = 'H'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i+1][j-2] = board[i+1][j-2]
                    if i-1 > 0 and j-2 > 0:
                        if not board[i-1][j-2].isupper():
                            self.boardstate.checkboard[i-1][j-2] = 'H'
                            self.boardstate.printboard(self.boardstate.checkboard)
                            if self.kingcheck(self.boardstate.checkboard) == False:
                                print("Checking!")
                        self.boardstate.checkboard[i-1][j-2] = board[i-1][j-2]
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
                                self.boardstate.checkboard[i+c][j-c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j-c] = '-'
                            else:
                                self.boardstate.checkboard[i+c][j-c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j-c] = '-'

                        if leftdown == True:
                            if j-c < 0 or i-c < 0 or board[i-c][j-c].isupper():
                                leftdown = False
                            elif board[i-c][j-c].islower():
                                leftdown = False
                                self.boardstate.checkboard[i-c][j-c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j-c] = '-'
                            else:
                                self.boardstate.checkboard[i-c][j-c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j-c] = '-'

                        if rightup == True:
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].isupper():
                                rightup = False
                            elif board[i+c][j+c].islower():
                                rightup = False
                                self.boardstate.checkboard[i+c][j+c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j+c] = '-'
                            else:
                                self.boardstate.checkboard[i+c][j+c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j+c] = '-'

                        if rightdown == True:
                            if j+c > 7 or i-c < 0 or board[i-c][j+c].isupper():
                                rightdown = False
                            elif board[i-c][j+c].islower():
                                rightdown = False
                                self.boardstate.checkboard[i-c][j+c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j+c] = '-'
                            else:
                                self.boardstate.checkboard[i-c][j+c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j+c] = '-'
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
                                self.boardstate.checkboard[i][j+c] = 'R'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j+c] = '-'
                            else:
                                self.boardstate.checkboard[i][j+c] = 'R'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j+c] = '-'
                        if left == True:
                            if j-c < 0 or board[i][j-c].isupper():
                                left = False
                            elif board[i][j-c].islower():
                                left = False
                                self.boardstate.checkboard[i][j-c] = 'R'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j-c] = '-'
                            else:
                                self.boardstate.checkboard[i][j-c] = 'R'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j-c] = '-'
                        if up == True:
                            if i+c > 7 or board[i+c][j].isupper():
                                up = False
                            elif board[i+c][j].islower():
                                up = False
                                self.boardstate.checkboard[i+c][j] = 'R'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j] = '-'
                            else:
                                self.boardstate.checkboard[i+c][j] = 'R'
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j] = '-'
                        if down == True:
                            if i-c < 0 or board[i-c][j].isupper():
                                down = False
                            elif board[i-c][j].islower():
                                down = False
                                self.boardstate.checkboard[i-c][j] = 'R'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j] = '-'
                            else:
                                self.boardstate.checkboard[i-c][j] = 'R'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j] = '-'
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
                                self.boardstate.checkboard[i][j+c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j+c] = board[i][j+c]
                            else:
                                self.boardstate.checkboard[i][j+c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j+c] = board[i][j+c]
                        if left == True:
                            if j-c < 0 or board[i][j-c].isupper():
                                left = False
                            elif board[i][j-c].islower():
                                left = False
                                self.boardstate.checkboard[i][j-c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j-c] = board[i][j-c]
                            else:
                                self.boardstate.checkboard[i][j-c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i][j-c] = board[i][j-c]
                        if up == True:
                            if i+c > 7 or board[i+c][j].isupper():
                                up = False
                            elif board[i+c][j].islower():
                                up = False
                                self.boardstate.checkboard[i+c][j] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j] = board[i+c][j]
                            else:
                                self.boardstate.checkboard[i+c][j] = 'Q'
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j] = board[i+c][j]
                        if down == True:
                            if i-c < 0 or board[i-c][j].isupper():
                                down = False
                            elif board[i-c][j].islower():
                                down = False
                                self.boardstate.checkboard[i-c][j] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j] = board[i-c][j]
                            else:
                                self.boardstate.checkboard[i-c][j] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j] = board[i-c][j]
                        if leftup == True:
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].isupper():
                                leftup = False
                            elif board[i+c][j-c].islower():
                                leftup = False
                                self.boardstate.checkboard[i+c][j-c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j-c] = board[i+c][j-c]
                            else:
                                self.boardstate.checkboard[i+c][j-c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j-c] = board[i+c][j-c]

                        if leftdown == True:
                            if j-c < 0 or i-c < 0 or board[i-c][j-c].isupper():
                                leftdown = False
                            elif board[i-c][j-c].islower():
                                leftdown = False
                                self.boardstate.checkboard[i-c][j-c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j-c] = board[i-c][j-c]
                            else:
                                self.boardstate.checkboard[i-c][j-c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j-c] = board[i-c][j-c]

                        if rightup == True:
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].isupper():
                                rightup = False
                            elif board[i+c][j+c].islower():
                                rightup = False
                                self.boardstate.checkboard[i+c][j+c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j+c] = board[i+c][j+c]
                            else:
                                self.boardstate.checkboard[i+c][j+c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i+c][j+c] = board[i+c][j+c]

                        if rightdown == True:
                            if j+c > 7 or i-c < 0 or board[i-c][j+c].isupper():
                                rightdown = False
                            elif board[i-c][j+c].islower():
                                rightdown = False
                                self.boardstate.checkboard[i-c][j+c] = 'Q'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j+c] = board[i-c][j+c]
                            else:
                                self.boardstate.checkboard[i-c][j+c] = 'B'
                                self.boardstate.printboard(self.boardstate.checkboard)
                                if self.kingcheck(self.boardstate.checkboard) == False:
                                    print("Checking!")
                                self.boardstate.checkboard[i-c][j+c] = board[i-c][j+c]
        return checkmate
