# Knight on chess

class Chess(object): # using class so it is easier to read & execute
    X = 0
    Y = 0

    def __init__(self, size):
        parsed = size.split("x")
        self.sizeX = int(parsed[0])
        self.sizeY = int(parsed[1])
        self.chessboard = self.makeChessboard()

    def makeChessboard(self):
        return [[0 for _ in range(self.sizeX)] for _ in range(self.sizeY)] # making the board using a 2D list

    def printChessboard(self):
        for y in self.chessboard:
            for x in y:
                if x == 0:
                    print("- ", end="")
                elif x == 1:
                    print("o ", end="")
                else:
                    print("+ ", end="")
            print()

    def parseChessMove(self, move):
        self.Y = len(self.chessboard)-int(move[1:])
        self.X = ord(move[0])-65
        self.chessboard[self.Y][self.X] = 1 # set the board to 1 (knight)

    def addPossibleMoves(self):
        for move in [(self.X-1, self.Y-2), (self.X+1, self.Y-2), (self.X-1, self.Y+2), 
                     (self.X+1, self.Y+2), (self.X-2, self.Y-1), (self.X+2, self.Y-1), 
                     (self.X-2, self.Y+1), (self.X+2, self.Y+1)]: # every possible moves for knight
            try:
                if ((move[1] >= 0) and (move[1] < self.sizeX)) and ((move[0] >= 0) and (move[0] < self.sizeY)): # checking if the move is in range of the board
                    self.chessboard[move[1]][move[0]] = 2 # set the board to 2 (move is possible)
            except IndexError:
                pass # skipping the move assignment if index is out of range

chess = Chess(input("How big is the chessboard (ex. 8x8 upto 26x26): "))
chess.parseChessMove(input("Put your VALID chess moves: "))
chess.addPossibleMoves()
chess.printChessboard()
