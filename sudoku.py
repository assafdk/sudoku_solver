
constrains = [[0, 0, 0, 4, 0, 6, 0, 1, 0],
              [0, 0, 3, 5, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 9, 0, 0, 0, 0],
              [0, 0, 9, 1, 0, 0, 0, 6, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 0, 0, 0, 3, 8, 0, 0],
              [0, 0, 0, 0, 7, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 9, 1, 0, 0],
              [0, 6, 0, 2, 0, 4, 0, 0, 0]]

N=9
w, h = N, N;
NUMBER_OF_BOXES = N // 3

# Creates a list containing 9 lists, each of 9 items, all set to 0
board = [[0 for x in range(w)] for y in range(h)]

cur_spot = {}
cur_spot['row'] = 0
cur_spot['col'] = 0


def nextSpot(cur_spot, width, heigth):
    if cur_spot == None:
        return None

    ret_spot = {}
    ret_spot['col'] = cur_spot['col']
    ret_spot['row'] = cur_spot['row']

    if (cur_spot['col'] == width-1):
        if (cur_spot['row'] == heigth-1):
            return None
        ret_spot['row'] = cur_spot['row']+1
        ret_spot['col'] = 0
        return ret_spot

    ret_spot['col']+=1
    return ret_spot


def isFull(board, w, h):
    for i in range(0,w):
        for j in range(0, h):
            if board[j][i] == 0:
                return False
    return True


def placeNumber(board, cur_spot, i):

    board[cur_spot['row']][cur_spot['col']] = i
    return

def isRowLegal(row, board, w, h):
    seen = [0 for x in range(N)]
    for i in range(0,w):
        if board[row][i] == 0:
            continue
        if seen[board[row][i]-1] == 1:
            return False
        seen[board[row][i]-1] = 1
    return True

def isColLegal(col, board, w, h):
    seen = [0 for x in range(N)]
    for i in range(0,h):
        if board[i][col] == 0:
            continue
        if seen[board[i][col]-1] == 1:
            return False
        seen[board[i][col]-1] = 1
    return True

def isBoxLegal(box_row_serial,box_col_serial, board, w, h):
    seen = [0 for x in range(N)]
    for i in range(box_row_serial*N/3,(box_row_serial+1)*N/3):
        for j in range(box_col_serial*N/3,(box_col_serial+1)*N/3):
            if board[i][j] == 0:
                continue
            if seen[board[i][j]-1] == 1:
                return False
            seen[board[i][j]-1] = 1
    return True

def areAllRowsLegal(board, w, h):
    for row in range(0,h):
        if not isRowLegal(row, board, w, h):
            return False
    return True

def areAllColsLegal(board, w, h):
    for col in range(0,h):
        if not isColLegal(col, board, w, h):
            return False
    return True

def areAllBoxesLegal(board, w, h):
    for box_row in range(0, 3):
        for box_col in range(0, 3):
            if not isBoxLegal(box_row, box_col, board, w, h):
                return False
    return True

def isLegal(board, w, h):
    if not areAllRowsLegal(board, w, h):
        return False
    if not areAllColsLegal(board, w, h):
        return False
    if not areAllBoxesLegal(board, w, h):
        return False
    return True


def solve(board, cur_spot, constrains):
    if (isLegal(board, w, h)):

        if (isFull(board, w, h)):
            # legal & full = done
            return True

        if constrains[cur_spot['row']][cur_spot['col']] > 0:
            return solve(board, nextSpot(cur_spot,w,h), constrains)

        # legal but not full = we're getting there -> next step
        for i in range(1,10):
            placeNumber(board, cur_spot, i)
            if solve(board, nextSpot(cur_spot,w,h), constrains):
                return True
        placeNumber(board, cur_spot, 0)
        return False

    # illegal move - backtrack!
    return False

def printboard(board):
    for i in range(0,9):
        for j in range(0,9):
            print board[i][j],
            if j % 3 == 2:
                print "|",
        print ""
        if i % 3 == 2:
            print "---------------------"

board = constrains[:][:]
solve(board,cur_spot, constrains)
printboard(board)

blank_constrains = \
              [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]