from boardstate import *

class KingCheckVerify:

    def __init__(self):
        self.boardstate = Board()
    def kingcheck(self, board, kingstate):
        check = False
        whitecheck = False
        blackcheck = False
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j].lower() == 'p' and board[i][j].islower():
                    if i+1 < 8 and j-1 > 0:
                        if board[i+1][j-1] == 'K':
                            check, whitecheck = True, True                            
                    if i+1 < 8 and j+1 < 8:
                        if board[i+1][j+1] == 'K':
                            check, whitecheck = True, True                            
                if board[i][j].lower() == 'h' and board[i][j].islower():
                    if i+2 < 8 and j+1 < 8:
                        if board[i+2][j+1] == 'K':
                            check, whitecheck = True, True                            
                    if i+2 < 8 and j-1 > 0:
                        if board[i+2][j-1] == 'K':
                            check, whitecheck = True, True                            
                    if i-2 > 0 and j+1 < 8:
                        if board[i-2][j+1] == 'K':
                            check, whitecheck = True, True                            
                    if i-2 > 0 and j-1 < 8:
                        if board[i-2][j-1] == 'K':
                            check, whitecheck = True, True                            
                    if i+1 < 8 and j+2 < 8:
                        if board[i+1][j+2] == 'K':
                            check, whitecheck = True, True                            
                    if i-1 > 0 and j+2 < 8:
                        if board[i-1][j+2] == 'K':
                            check, whitecheck = True, True                            
                    if i+1 < 8 and j-2 > 0:
                        if board[i+1][j-2] == 'K':
                            check, whitecheck = True, True                            
                    if i-1 > 0 and j-2 > 0:
                        if board[i-1][j-2] == 'K':
                            check, whitecheck = True, True                            
                if board[i][j].lower() == 'b' and board[i][j].islower():
                    leftup = True
                    leftdown = True
                    rightup = True
                    rightdown = True
                    for c in range(1, 7):
                        if leftup == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                check, whitecheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False

                        if leftdown == True:
                            if j-c < 0 and i-c < 0 and board[i-c][j-c] == 'K':
                                check, whitecheck = True, True                                
                            if j-c > 7 or i-c < 0 or board[i-c][j-c].islower() or board[i-c][j-c].isupper():
                                leftdown = False

                        if rightup == True:
                            if j+c < 8 and i+c < 8 and board[i+c][j+c] == 'K':
                                check, whitecheck = True, True                                
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].islower() or board[i+c][j+c].isupper():
                                rightup = False

                        if rightdown == True:
                            if j+c < 8 and i-c > 0 and board[i-c][j+c] == 'K':
                                check, whitecheck = True, True                                
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
                                check, whitecheck = True, True
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if left == True:
                            if board[i][j-c] == 'K' and j-c > -1:                                
                                check, whitecheck = True, True
                            if board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
                        if up == True:
                            if board[i+c][j] == 'K' and i+c < 8:                                
                                check, whitecheck = True, True
                            if board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if down == True:
                            if board[i-c][j] == 'K' and i-c > 0:                                
                                check, whitecheck = True, True
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
                                check, whitecheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'K':
                                check, whitecheck = True, True                                
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if upright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                check, whitecheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                upright = False
                        if right == True:
                            if j+c < 8 and board[i][j+c] == 'K':
                                check, whitecheck = True, True                                
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if downright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                check, whitecheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downright = False
                        if down == True:
                            if i-c > -1 and board[i-c][j] == 'K':
                                check, whitecheck = True, True                                
                            if i-c < 0 or board[i-c][j].islower() or board[i-c][j].isupper():
                                down = False
                        if downleft == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'K':
                                check, whitecheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downleft = False
                        if left == True:
                            if j-c > -1 and board[i][j-c] == 'K':
                                check, whitecheck = True, True                                
                            if j-c < 0 or board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
                if board[i][j].lower() == 'p' and board[i][j].isupper():
                    if i-1 > 0 and j-1 > 0:
                        if board[i-1][j-1] == 'k':
                            check, blackcheck = True, True                            
                    if i-1 > 0 and j+1 < 8:
                        if board[i-1][j+1] == 'k':
                            check, blackcheck = True, True                           
                if board[i][j].lower() == 'h' and board[i][j].isupper():
                    if i+2 < 8 and j+1 < 8:
                        if board[i+2][j+1] == 'k':
                            check, blackcheck = True, True                            
                    if i+2 < 8 and j-1 > -1:
                        if board[i+2][j-1] == 'k':
                            check, blackcheck = True, True                            
                    if i-2 > -1 and j+1 < 8:
                        if board[i-2][j+1] == 'k':
                            check, blackcheck = True, True                            
                    if i-2 > -1 and j-1 < 8:
                        if board[i-2][j-1] == 'k':
                            check, blackcheck = True, True                            
                    if i+1 < 8 and j+2 < 8:
                        if board[i+1][j+2] == 'k':
                            check, blackcheck = True, True                            
                    if i-1 > -1 and j+2 < 8:
                        if board[i-1][j+2] == 'k':
                            check, blackcheck = True, True                            
                    if i+1 < 8 and j-2 > -1:
                        if board[i+1][j-2] == 'k':
                            check, blackcheck = True, True                            
                    if i-1 > -1 and j-2 > -1:
                        if board[i-1][j-2] == 'k':
                            check, blackcheck = True, True                            
                if board[i][j].lower() == 'b' and board[i][j].isupper():
                    leftup = True
                    leftdown = True
                    rightup = True
                    rightdown = True
                    for c in range(1, 7):
                        if leftup == True:
                            if j-c > -1 and i+c < 8 and board[i+c][j-c] == 'k':
                                check, blackcheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False

                        if leftdown == True:
                            if j-c > -1 and i-c > -1 and board[i-c][j-c] == 'k':
                                check, blackcheck = True, True                                
                            if j-c < 0 or i-c < 0 or board[i-c][j-c].islower() or board[i-c][j-c].isupper():
                                leftdown = False

                        if rightup == True:
                            if j+c < 8 and i+c < 8 and board[i+c][j+c] == 'k':
                                check, blackcheck = True, True                                
                            if j+c > 7 or i+c > 7 or board[i+c][j+c].islower() or board[i+c][j+c].isupper():
                                rightup = False

                        if rightdown == True:
                            if j+c < 8 and i-c > 0 and board[i-c][j+c] == 'k':
                                check, blackcheck = True, True                                
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
                                check, blackcheck = True, True                                
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if left == True:
                            if board[i][j-c] == 'k' and j-c > -1:
                                check, blackcheck = True, True                                
                            if board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'k':
                                check, blackcheck = True, True                                
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if down == True:
                            if board[i-c][j] == 'k' and i-c > 0:
                                check, blackcheck = True, True                                
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
                                check, blackcheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                leftup = False
                        if up == True:
                            if i+c < 8 and board[i+c][j] == 'k':
                                check, blackcheck = True, True                                
                            if i+c > 7 or board[i+c][j].islower() or board[i+c][j].isupper():
                                up = False
                        if upright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                check, blackcheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                upright = False
                        if right == True:
                            if j+c < 8 and board[i][j+c] == 'k':
                                check, blackcheck = True, True                                
                            if j+c > 7 or board[i][j+c].islower() or board[i][j+c].isupper():
                                right = False
                        if downright == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                check, blackcheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downright = False
                        if down == True:
                            if i-c > -1 and board[i-c][j] == 'k':
                                check, blackcheck = True, True                                
                            if i-c < 0 or board[i-c][j].islower() or board[i-c][j].isupper():
                                down = False
                        if downleft == True:
                            if j-c > 0 and i+c < 8 and board[i+c][j-c] == 'k':
                                check, blackcheck = True, True                                
                            if j-c < 0 or i+c > 7 or board[i+c][j-c].islower() or board[i+c][j-c].isupper():
                                downleft = False
                        if left == True:
                            if j-c > -1 and board[i][j-c] == 'k':
                                check, blackcheck = True, True                                
                            if j-c < 0 or board[i][j-c].islower() or board[i][j-c].isupper():
                                left = False
        if (check == True and kingstate == False):
            input("Check")
            print(self.kingcheckmate(self.boardstate.checkboard, whitecheck))
            
        return [check, whitecheck, blackcheck]

    def kingcheckmate(self, checkboard, kingtype):
        checkmate = True
        board = self.boardstate.board

        for i in range(len(checkboard)):
            for j in range(len(checkboard)):
                checkboard[i][j] = board[i][j]
                
        for i in range(len(checkboard)):
            for j in range(len(checkboard)):
                if(kingtype == False):
                    if checkboard[i][j].lower() == 'p' and checkboard[i][j].islower():
                        if i == 1 and checkboard[i+1][j] == '-' and checkboard[i+2][j] == '-':
                            checkboard[i+2][j], checkboard[i][j] = 'p', '-'
                            if self.kingcheck(checkboard, True)[0] == False:
                                checkmate = False
                            checkboard[i+2][j], checkboard[i][j] = self.boardstate.board[i+2][j], self.boardstate.board[i][j]
                        if i+1 < 0 or checkboard[i+1][j] == "-":
                            checkboard[i+1][j], checkboard[i][j] = 'p', '-'
                            if self.kingcheck(checkboard, True)[0] == False:
                                checkmate = False
                            checkboard[i+1][j], checkboard[i][j] = self.boardstate.board[i+1][j], self.boardstate.board[i][j]
                        if j-1 > 0 and i+1 > 0 and checkboard[i+1][j-1].isupper():
                            checkboard[i+1][j-1] = 'p'
                            checkboard[i][j] = '-'
                            if self.kingcheck(checkboard, True)[0] == False:
                                checkmate = False
                            checkboard[i+1][j-1], checkboard[i][j] = self.boardstate.board[i+1][j-1], self.boardstate.board[i][j]
                        if j+1 < 7 and i+1 > 0 and checkboard[i+1][j+1].isupper():
                            checkboard[i+1][j+1], checkboard[i][j] = 'p', '-'
                            if self.kingcheck(checkboard, True)[0] == False:
                                checkmate = False
                            checkboard[i+1][j+1], checkboard[i][j] = self.boardstate.board[i+1][j+1], self.boardstate.board[i][j]
                    if checkboard[i][j].lower() == 'h' and checkboard[i][j].islower():
                        if i+2 < 8 and j+1 < 8:
                            if not checkboard[i+2][j+1].islower():
                                checkboard[i][j] = '-'
                                checkboard[i+2][j+1] = 'h'
                                
                                # if self.kingcheck(checkboard, True)[0] == False:
                                #     checkmate = False
                            checkboard[i][j] = 'h'
                            checkboard[i+2][j+1] = board[i+2][j+1]
                        if i+2 < 8 and j-1 >= 0:
                            if not checkboard[i+2][j-1].islower():
                                checkboard[i+2][j-1] = 'h'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i+2][j-1] = self.boardstate.board[i+2][j-1]
                        if i-2 > 0 and j+1 < 8:
                            if not checkboard[i-2][j+1].islower():
                                checkboard[i-2][j+1] = 'h'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i-2][j+1] = self.boardstate.board[i-2][j+1]
                        if i-2 > 0 and j-1 < 8:
                            if not checkboard[i-2][j-1].islower():
                                checkboard[i-2][j-1] = 'h'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i-2][j-1] = self.boardstate.board[i-2][j-1]
                        if i+1 < 8 and j+2 < 8:
                            if not checkboard[i+1][j+2].islower():
                                checkboard[i+1][j+2] = 'h'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i+1][j+2] = self.boardstate.board[i+1][j+2]
                        if i-1 > 0 and j+2 < 8:
                            if not checkboard[i-1][j+2].islower():
                                checkboard[i-1][j+2] = 'h'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i-1][j+2] = self.boardstate.board[i-1][j+2]
                        if i+1 < 8 and j-2 > 0:
                            if not checkboard[i+1][j-2].islower():
                                checkboard[i+1][j-2] = 'h'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i+1][j-2] = self.boardstate.board[i+1][j-2]
                        if i-1 > 0 and j-2 > 0:
                            if not checkboard[i-1][j-2].islower():
                                checkboard[i-1][j-2] = 'h'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i-1][j-2] = self.boardstate.board[i-1][j-2]
                    if checkboard[i][j].lower() == 'b' and checkboard[i][j].islower():
                        leftup = True
                        leftdown = True
                        rightup = True
                        rightdown = True
                        for c in range(1, 7):
                            if leftup == True:
                                if j-c < 0 or i+c > 7 or checkboard[i+c][j-c].islower():
                                    leftup = False
                                elif checkboard[i+c][j-c].isupper():
                                    leftup = False
                                    checkboard[i+c][j-c] = 'b'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j-c] = self.boardstate.board[i+c][j-c]
                                else:
                                    checkboard[i+c][j-c] = 'b'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j-c] = self.boardstate.board[i+c][j-c]

                            if leftdown == True:
                                if j-c < 0 or i-c < 0 or checkboard[i-c][j-c].islower():
                                    leftdown = False
                                elif checkboard[i-c][j-c].isupper():
                                    leftdown = False
                                    checkboard[i-c][j-c] = 'b'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j-c] = self.boardstate.board[i-c][j-c]
                                else:
                                    checkboard[i-c][j-c] = 'b'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j-c] = self.boardstate.board[i-c][j-c]

                            if rightup == True:
                                if j+c > 7 or i+c > 7 or checkboard[i+c][j+c].islower():
                                    rightup = False
                                elif checkboard[i+c][j+c].isupper():
                                    rightup = False
                                    checkboard[i+c][j+c] = 'b'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j+c] = self.boardstate.board[i+c][j+c]
                                else:
                                    checkboard[i+c][j+c] = 'b'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j+c] = self.boardstate.board[i+c][j+c]

                            if rightdown == True:
                                if j+c > 7 or i-c < 0 or checkboard[i-c][j+c].islower():
                                    rightdown = False
                                elif checkboard[i-c][j+c].isupper():
                                    rightdown = False
                                    checkboard[i-c][j+c] = 'b'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j+c] = self.boardstate.board[i-c][j+c]
                                else:
                                    checkboard[i-c][j+c] = 'b'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j+c] = self.boardstate.board[i-c][j+c]
                    if checkboard[i][j].lower() == 'r' and checkboard[i][j].islower():
                        up = True
                        left = True
                        right = True
                        down = True
                        for c in range(1, 7):
                            if right == True:
                                if j+c > 7 or checkboard[i][j+c].islower():
                                    right = False
                                elif checkboard[i][j+c].isupper():
                                    right = False
                                    checkboard[i][j+c] = 'r'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j+c] = self.boardstate.board[i][j+c]
                                else:
                                    checkboard[i][j+c] = 'r'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j+c] = self.boardstate.board[i][j+c]
                            if left == True:
                                if j-c < 0 or checkboard[i][j-c].islower():
                                    left = False
                                elif checkboard[i][j-c].isupper():
                                    left = False
                                    checkboard[i][j-c] = 'r'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j-c] = self.boardstate.board[i][j-c]
                                else:
                                    checkboard[i][j-c] = 'r'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j-c] = self.boardstate.board[i][j-c]
                            if up == True:
                                if i+c > 7 or checkboard[i+c][j].islower():
                                    up = False
                                elif checkboard[i+c][j].isupper():
                                    up = False
                                    checkboard[i+c][j] = 'r'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j] = self.boardstate.board[i+c][j]
                                else:
                                    checkboard[i+c][j] = 'r'
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j] = self.boardstate.board[i+c][j]
                            if down == True:
                                if i-c < 0 or checkboard[i-c][j].islower():
                                    down = False
                                elif checkboard[i-c][j].isupper():
                                    down = False
                                    checkboard[i-c][j] = 'r'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j] = self.boardstate.board[i-c][j]
                                else:
                                    checkboard[i-c][j] = 'r'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j] = self.boardstate.board[i-c][j]
                    if checkboard[i][j].lower() == 'q' and checkboard[i][j].islower():
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
                                if j+c > 7 or checkboard[i][j+c].islower():
                                    right = False
                                elif checkboard[i][j+c].isupper():
                                    right = False
                                    checkboard[i][j+c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j+c] = self.boardstate.board[i][j+c]
                                else:
                                    checkboard[i][j+c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j+c] = self.boardstate.board[i][j+c]
                            if left == True:
                                if j-c < 0 or checkboard[i][j-c].islower():
                                    left = False
                                elif checkboard[i][j-c].isupper():
                                    left = False
                                    checkboard[i][j-c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j-c] = self.boardstate.board[i][j-c]
                                else:
                                    checkboard[i][j-c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j-c] = self.boardstate.board[i][j-c]
                            if up == True:
                                if i+c > 7 or checkboard[i+c][j].islower():
                                    up = False
                                elif checkboard[i+c][j].isupper():
                                    up = False
                                    checkboard[i+c][j] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j] = self.boardstate.board[i+c][j]
                                else:
                                    checkboard[i+c][j] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j] = self.boardstate.board[i+c][j]
                            if down == True:
                                if i-c < 0 or checkboard[i-c][j].islower():
                                    down = False
                                elif checkboard[i-c][j].isupper():
                                    down = False
                                    checkboard[i-c][j] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j] = self.boardstate.board[i-c][j]
                                else:
                                    checkboard[i-c][j] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j] = self.boardstate.board[i-c][j]
                            if leftup == True:
                                if j-c < 0 or i+c > 7 or checkboard[i+c][j-c].islower():
                                    leftup = False
                                elif checkboard[i+c][j-c].isupper():
                                    leftup = False
                                    checkboard[i+c][j-c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j-c] = self.boardstate.board[i+c][j-c]
                                else:
                                    checkboard[i+c][j-c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j-c] = self.boardstate.board[i+c][j-c]

                            if leftdown == True:
                                if j-c < 0 or i-c < 0 or checkboard[i-c][j-c].islower():
                                    leftdown = False
                                elif checkboard[i-c][j-c].isupper():
                                    leftdown = False
                                    checkboard[i-c][j-c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j-c] = self.boardstate.board[i-c][j-c]
                                else:
                                    checkboard[i-c][j-c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j-c] = self.boardstate.board[i-c][j-c]

                            if rightup == True:
                                if j+c > 7 or i+c > 7 or checkboard[i+c][j+c].islower():
                                    rightup = False
                                elif checkboard[i+c][j+c].isupper():
                                    rightup = False
                                    checkboard[i+c][j+c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j+c] = self.boardstate.board[i+c][j+c]
                                else:
                                    checkboard[i+c][j+c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j+c] = self.boardstate.board[i+c][j+c]

                            if rightdown == True:
                                if j+c > 7 or i-c < 0 or checkboard[i-c][j+c].islower():
                                    rightdown = False
                                elif checkboard[i-c][j+c].isupper():
                                    rightdown = False
                                    checkboard[i-c][j+c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j+c] = self.boardstate.board[i-c][j+c]
                                else:
                                    checkboard[i-c][j+c] = 'q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j+c] = self.boardstate.board[i-c][j+c]
                else:
                    if checkboard[i][j].lower() == 'p' and checkboard[i][j].isupper():
                        if i == 6 and checkboard[i-1][j] == '-' and checkboard[i-2][j] == '-':
                            checkboard[i-2][j], checkboard[i][j] = 'P', '-'
                            if self.kingcheck(checkboard, True)[0] == False:
                                checkmate = False
                            checkboard[i-2][j], checkboard[i][j] = self.boardstate.board[i-2][j], self.boardstate.board[i][j]
                        if i-1 < 7 and checkboard[i-1][j] == "-":
                            checkboard[i-1][j], checkboard[i][j] = 'P', '-'
                            if self.kingcheck(checkboard, True)[0] == False:
                                checkmate = False
                            checkboard[i-1][j], checkboard[i][j] = self.boardstate.board[i-1][j], self.boardstate.board[i][j]
                        if j-1 > 0 and i-1 > 0 and checkboard[i-1][j-1].islower():
                            checkboard[i-1][j-1] = 'P'
                            checkboard[i][j] = '-'
                            if self.kingcheck(checkboard, True)[0] == False:
                                checkmate = False
                            checkboard[i-1][j-1], checkboard[i][j] = self.boardstate.board[i-1][j-1], self.boardstate.board[i][j]
                        if j+1 < 7 and i-1 > 0 and checkboard[i-1][j+1].islower():
                            checkboard[i-1][j+1], checkboard[i][j] = 'P', '-'
                            if self.kingcheck(checkboard, True)[0] == False:
                                checkmate = False
                            checkboard[i-1][j+1], checkboard[i][j] = self.boardstate.board[i-1][j+1], self.boardstate.board[i][j]
                    if checkboard[i][j].lower() == 'h' and checkboard[i][j].isupper():
                        if i+2 < 8 and j+1 < 8:
                            if not checkboard[i+2][j+1].isupper():
                                checkboard[i+2][j+1] = 'H'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i+2][j+1] = self.boardstate.board[i+2][j+1]
                        if i+2 < 8 and j-1 > 0:
                            if not checkboard[i+2][j-1].isupper():
                                checkboard[i+2][j-1] = 'H'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i+2][j-1] = self.boardstate.board[i+2][j-1]
                        if i-2 > 0 and j+1 < 8:
                            if not checkboard[i-2][j+1].isupper():
                                checkboard[i-2][j+1] = 'H'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i-2][j+1] = self.boardstate.board[i-2][j+1]
                        if i-2 > 0 and j-1 < 8:
                            if not checkboard[i-2][j-1].isupper():
                                checkboard[i-2][j-1] = 'H'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i-2][j-1] = self.boardstate.board[i-2][j-1]
                        if i+1 < 8 and j+2 < 8:
                            if not checkboard[i+1][j+2].isupper():
                                checkboard[i+1][j+2] = 'H'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i+1][j+2] = self.boardstate.board[i+1][j+2]
                        if i-1 > 0 and j+2 < 8:
                            if not checkboard[i-1][j+2].isupper():
                                checkboard[i-1][j+2] = 'H'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i-1][j+2] = self.boardstate.board[i-1][j+2]
                        if i+1 < 8 and j-2 > 0:
                            if not checkboard[i+1][j-2].isupper():
                                checkboard[i+1][j-2] = 'H'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i+1][j-2] = self.boardstate.board[i+1][j-2]
                        if i-1 > 0 and j-2 > 0:
                            if not checkboard[i-1][j-2].isupper():
                                checkboard[i-1][j-2] = 'H'
                                
                                if self.kingcheck(checkboard, True)[0] == False:
                                    checkmate = False
                            checkboard[i-1][j-2] = self.boardstate.board[i-1][j-2]
                    if checkboard[i][j].lower() == 'b' and checkboard[i][j].isupper():
                        leftup = True
                        leftdown = True
                        rightup = True
                        rightdown = True
                        for c in range(1, 7):
                            if leftup == True:
                                if j-c < 0 or i+c > 7 or checkboard[i+c][j-c].isupper():
                                    leftup = False
                                elif checkboard[i+c][j-c].islower():
                                    leftup = False
                                    checkboard[i+c][j-c] = 'B'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j-c] = '-'
                                else:
                                    checkboard[i+c][j-c] = 'B'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j-c] = '-'

                            if leftdown == True:
                                if j-c < 0 or i-c < 0 or checkboard[i-c][j-c].isupper():
                                    leftdown = False
                                elif checkboard[i-c][j-c].islower():
                                    leftdown = False
                                    checkboard[i-c][j-c] = 'B'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j-c] = '-'
                                else:
                                    checkboard[i-c][j-c] = 'B'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j-c] = '-'

                            if rightup == True:
                                if j+c > 7 or i+c > 7 or checkboard[i+c][j+c].isupper():
                                    rightup = False
                                elif checkboard[i+c][j+c].islower():
                                    rightup = False
                                    checkboard[i+c][j+c] = 'B'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j+c] = '-'
                                else:
                                    checkboard[i+c][j+c] = 'B'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j+c] = '-'

                            if rightdown == True:
                                if j+c > 7 or i-c < 0 or checkboard[i-c][j+c].isupper():
                                    rightdown = False
                                elif checkboard[i-c][j+c].islower():
                                    rightdown = False
                                    checkboard[i-c][j+c] = 'B'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j+c] = '-'
                                else:
                                    checkboard[i-c][j+c] = 'B'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j+c] = '-'
                    if checkboard[i][j].lower() == 'r' and checkboard[i][j].isupper():
                        up = True
                        left = True
                        right = True
                        down = True
                        for c in range(1, 7):
                            if right == True:
                                if j+c > 7 or checkboard[i][j+c].isupper():
                                    right = False
                                elif checkboard[i][j+c].islower():
                                    right = False
                                    checkboard[i][j+c] = 'R'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j+c] = '-'
                                else:
                                    checkboard[i][j+c] = 'R'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j+c] = '-'
                            if left == True:
                                if j-c < 0 or checkboard[i][j-c].isupper():
                                    left = False
                                elif checkboard[i][j-c].islower():
                                    left = False
                                    checkboard[i][j-c] = 'R'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j-c] = '-'
                                else:
                                    checkboard[i][j-c] = 'R'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j-c] = '-'
                            if up == True:
                                if i+c > 7 or checkboard[i+c][j].isupper():
                                    up = False
                                elif checkboard[i+c][j].islower():
                                    up = False
                                    checkboard[i+c][j] = 'R'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j] = '-'
                                else:
                                    checkboard[i+c][j] = 'R'
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j] = '-'
                            if down == True:
                                if i-c < 0 or checkboard[i-c][j].isupper():
                                    down = False
                                elif checkboard[i-c][j].islower():
                                    down = False
                                    checkboard[i-c][j] = 'R'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j] = '-'
                                else:
                                    checkboard[i-c][j] = 'R'
                                    
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j] = '-'
                    if checkboard[i][j].lower() == 'q' and checkboard[i][j].isupper():
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
                                if j+c > 7 or checkboard[i][j+c].isupper():
                                    right = False
                                elif checkboard[i][j+c].islower():
                                    right = False
                                    checkboard[i][j+c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j+c] = self.boardstate.board[i][j+c]
                                else:
                                    checkboard[i][j+c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j+c] = self.boardstate.board[i][j+c]
                            if left == True:
                                if j-c < 0 or checkboard[i][j-c].isupper():
                                    left = False
                                elif checkboard[i][j-c].islower():
                                    left = False
                                    checkboard[i][j-c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j-c] = self.boardstate.board[i][j-c]
                                else:
                                    checkboard[i][j-c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i][j-c] = self.boardstate.board[i][j-c]
                            if up == True:
                                if i+c > 7 or checkboard[i+c][j].isupper():
                                    up = False
                                elif checkboard[i+c][j].islower():
                                    up = False
                                    checkboard[i+c][j] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j] = self.boardstate.board[i+c][j]
                                else:
                                    checkboard[i+c][j] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j] = self.boardstate.board[i+c][j]
                            if down == True:
                                if i-c < 0 or checkboard[i-c][j].isupper():
                                    down = False
                                elif checkboard[i-c][j].islower() and checkboard[i-c][j] != 'k':
                                    down = False
                                    checkboard[i-c][j] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j] = self.boardstate.board[i-c][j]
                                else:
                                    checkboard[i-c][j] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j] = self.boardstate.board[i-c][j]
                            if leftup == True:
                                if j-c < 0 or i+c > 7 or checkboard[i+c][j-c].isupper():
                                    leftup = False
                                elif checkboard[i+c][j-c].islower():
                                    leftup = False
                                    checkboard[i+c][j-c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j-c] = self.boardstate.board[i+c][j-c]
                                else:
                                    checkboard[i+c][j-c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j-c] = self.boardstate.board[i+c][j-c]

                            if leftdown == True:
                                if j-c < 0 or i-c < 0 or checkboard[i-c][j-c].isupper():
                                    leftdown = False
                                elif checkboard[i-c][j-c].islower():
                                    leftdown = False
                                    checkboard[i-c][j-c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j-c] = self.boardstate.board[i-c][j-c]
                                else:
                                    checkboard[i-c][j-c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j-c] = self.boardstate.board[i-c][j-c]

                            if rightup == True:
                                if j+c > 7 or i+c > 7 or checkboard[i+c][j+c].isupper():
                                    rightup = False
                                elif checkboard[i+c][j+c].islower():
                                    rightup = False
                                    checkboard[i+c][j+c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j+c] = self.boardstate.board[i+c][j+c]
                                else:
                                    checkboard[i+c][j+c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i+c][j+c] = self.boardstate.board[i+c][j+c]

                            if rightdown == True:
                                if j+c > 7 or i-c < 0 or checkboard[i-c][j+c].isupper():
                                    rightdown = False
                                elif checkboard[i-c][j+c].islower():
                                    rightdown = False
                                    checkboard[i-c][j+c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j+c] = self.boardstate.board[i-c][j+c]
                                else:
                                    checkboard[i-c][j+c] = 'Q'
                                    self.boardstate.printboard(checkboard)
                                    if self.kingcheck(checkboard, True)[0] == False:
                                        checkmate = False
                                    checkboard[i-c][j+c] = self.boardstate.board[i-c][j+c]
        self.boardstate.printboard(self.boardstate.board)
        if checkmate == True:
            return input("Checkmate")
        else:
            return input("Not Checkmate")
