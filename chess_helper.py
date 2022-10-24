

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
