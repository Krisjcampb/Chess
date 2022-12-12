

class Chess_Helper:

    def sign(self, x):
        if x < 0:
            return -1
        elif x == 0:
            return 0
        else:
            return 1

    def coordYhelper(self, coordinate):
        return abs((ord(coordinate[0].upper())-64)-8)

    def coordXhelper(self, coordinate):
        return int(coordinate[1])-1

    def doubleking(self, y2_axis, x2_axis, board):
        #right down
        if(y2_axis+1 < 8 and x2_axis+1 < 8 and board[y2_axis+1][x2_axis+1] == 'k'.lower()): 
            return True 
        #down
        if(y2_axis+1 < 8 and x2_axis < 8 and board[y2_axis+1][x2_axis] == 'k'.lower()):
            return True
        #left down
        if(y2_axis+1 < 8 and x2_axis-1 < 8 and board[y2_axis+1][x2_axis-1] == 'k'.lower()):
            return True
        #right up
        if(y2_axis-1 < 8 and x2_axis+1 < 8 and board[y2_axis-1][x2_axis+1] == 'k'.lower()):
            return True
        #up
        if(y2_axis-1 < 8 and x2_axis < 8 and board[y2_axis-1][x2_axis] == 'k'.lower()):
            return True
        #up left
        if(y2_axis-1 < 8 and x2_axis-1 < 8 and board[y2_axis-1][x2_axis-1] == 'k'.lower()):
            return True
        #right
        if(y2_axis < 8 and x2_axis+1 < 8 and board[y2_axis][x2_axis+1] == 'k'.lower()):
            return True
        #left
        if(y2_axis < 8 and x2_axis-1 < 8 and board[y2_axis][x2_axis-1] == 'k'.lower()):
            return True
        return False
