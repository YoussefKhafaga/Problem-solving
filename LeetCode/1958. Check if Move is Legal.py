def checkRight(board, row, column, color):
    if column >= 6:
        return False
    count = 1
    board [row][column] = color
    for i in range(column+1, 8):
        if board[row][i] == ".":
            return False
        elif board[row][i] == color and count < 2:
            return False
        elif board[row][i] != color:
            count += 1
        elif board[row][i] == color and count >= 2:
            return True
    return False

def checkLeft(board, row, column, color):
    if column <= 1:
        return False
    count = 1
    board[row][column] = color
    for i in range(column-1, -1, -1):
        if board[row][i] == ".":
            return False
        elif board[row][i] == color and count < 2:
            return False
        elif board[row][i] != color:
            count += 1
        elif board[row][i] == color and count >= 2:
            return True
    return False

def checkUp(board, row, column, color):
    if row <= 1:
        return False
    count = 1
    board[row][column] = color
    for i in range(row-1, -1, -1):
        if board[i][column] == ".":
            return False
        elif board[i][column] == color and count < 2:
            return False
        elif board[i][column] != color:
            count += 1
        elif board[i][column] == color and count >= 2:
            return True
    return False

def checkDown(board, row, column, color):
    if row >= 6:
        return False
    count = 1
    board[row][column] = color
    for i in range(row+1, 8):
        if board[i][column] == ".":
            return False
        elif board[i][column] == color and count < 2:
            return False
        elif board[i][column] != color:
            count += 1
        elif board[i][column] == color and count >= 2:
            return True
    return False

def checkDiagonalUp(board, row, column, color):
    if row <= 1 or column >= 6:
        return False
    count = 1
    board[row][column] = color
    row-=1
    column+=1
    while row < 8 and column <= 7:
        if board[row][column] == color and count < 2:
            return False
        elif board[row][column] == ".":
            return False
        elif board[row][column] != color:
            count += 1
        elif board[row][column] == color and count >= 2:
            return True
        row -= 1
        column += 1
    return False

def checkDiagonalDown(board, row, column, color):
    if row >= 6 or column >= 6:
        return False
    count = 1
    board[row][column] = color
    row += 1
    column += 1
    while row >= 0 and column <= 7:
        print(row, column, count)
        if board[row][column] == ".":
            return False
        elif board[row][column] == color and count < 2:
            return False
        elif board[row][column] != color:
            count += 1
        elif board[row][column] == color and count >= 2:
            return True
        row += 1
        column += 1
    return False

def checkreverseDiagonalUp(board, row, column, color):
    if row <= 1 or column <= 1:
        return False
    count = 1
    board[row][column] = color
    row -= 1
    column -= 1
    while row >= 0 and column >= 0:
        if board[row][column] == ".":
            return False
        elif board[row][column] == color and count < 2:
            return False
        elif board[row][column] != color:
            count += 1
        elif board[row][column] == color and count >= 2:
            return True
        row -= 1
        column -= 1
    return False

def checkreverseDiagonalDown(board, row, column, color):
    if row >= 6 or column <= 1:
        return False
    count = 1
    board[row][column] = color
    row +=1
    column -= 1
    while row < 8 and column >= 0:
        print(row, column, count)
        if board[row][column] == ".":
            return False
        elif board[row][column] == color and count < 2:
            return False
        elif board[row][column] != color:
            count += 1
        elif board[row][column] == color and count >= 2:
            return True
        row += 1
        column -= 1
    return False

class Solution(object):
    def checkMove(self, board, rMove, cMove, color):
        row = rMove
        column = cMove
        if checkRight(board, row, column, color):
            return True
        print("right")
        if checkLeft(board, row, column, color):
            return True
        print("left")
        if checkUp(board, row, column, color):
            return True
        print("up")
        if checkDown(board, row, column, color):
            return True
        print("down")
        if checkDiagonalUp(board, row, column, color):
            return True
        print("diag up")
        if checkDiagonalDown(board, row, column, color):
            return True
        print("diag down")
        if checkreverseDiagonalUp(board, row, column, color):
            return True
        print("diag rev up")
        if checkreverseDiagonalDown(board, row, column, color):
            return True 
        print("diag rev down")
        return False