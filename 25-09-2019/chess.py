# Knight on chess

def printChessBoard(chessboard):
    for x in chessboard:
        for y in x: 
            if y == 0:
                print("- ", end="")
            elif y == 1:
                print("o ", end="")
            else:
                print("+ ", end="")
        print()

def makeChessBoard(width, length):
    x = [[0 for _ in range(width)] for _ in range(length)] # 2D list
    return x

def formatChessMove(makeChessBoard, move):
    return len(chessBoard)-int(move[1]), ord(move[0])-65

def possibleMoves(chessboard, xpos, ypos):
    move1 = (x-1, y-2)
    move2 = (x+1, y-2)
    move3 = (x-1, y+2)
    move4 = (x+1, y+2)
    move5 = (x-2, y-1)
    move6 = (x+2, y-1)
    move7 = (x-2, y+1)
    move8 = (x+2, y+1)
    return [move1, move2, move3, move4, move5, move6, move7, move8]

boardsSizeInput = input("How big is the chess boards (ex. 8x8): ").split("x")
boardsSize = (int(boardsSizeInput[0]), int(boardsSizeInput[0]))
chessMoves = input("Put your VALID chess moves: ")
chessBoard = makeChessBoard(boardsSize[0], boardsSize[1])
y, x = formatChessMove(chessBoard, chessMoves)
chessBoard[y][x] = 1
pos = possibleMoves(chessBoard, boardsSize[0], boardsSize[1])
for move in pos:
    try:
        if not (((move[1] > boardsSize[0]+1) or (move[1] < 0)) or ((move[0] > boardsSize[1]+1) or (move[0] < 0))):
            chessBoard[move[1]][move[0]] = 2
    except IndexError:
        pass
printChessBoard(chessBoard)
