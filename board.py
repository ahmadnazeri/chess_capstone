## DeepYellowJ - Version 0.1 (c) 2016 Ahmad Nazeri
#    Board - board.py
#
# This file creates the chess board.
# and displays the board and moves
# pieces.

# Import classes from other files
from ezgraphics import *
from piece import Piece

# Constants used graphics
SIZE = 8
SQUARESIZE = 70
COLOR1 = "red"
COLOR2 = "white"

class Board:
    # Constructor of Board
    def __init__(self):
        self._board = [[None for i in range(SIZE)]for j in range(SIZE)]
        self._window = False
        self._canvas = False

    # Moves piece from one position (current)
    # to another position (new).
    #
    # Parameters:
    #   current    - String
    #   new        - String
    # Returns:
    #   pieceTaken - Piece
    def move(self, current, new):
        # Used to draw square and piece
        canvas = self._canvas
        # Gets the row and column for current and new
        # to be used to move piece
        currentRow, currentColumn = self.findRowAndColumn(current)
        newRow, newColumn = self.findRowAndColumn(new)

        # Moves the pieces
        piece = self._board[currentColumn][currentRow]
        piece.changedMoved() # Identifies that piece has been moved
        pieceTaken = self._board[newColumn][newRow]
        self._board[newColumn][newRow] = piece
        # Makes the current spot empty (None)
        self._board[currentColumn][currentRow] = None

        # Determines the color of current square
        if (currentColumn+currentRow)%2 == 0:
            currentColor = COLOR1
        else:
            currentColor = COLOR2

        # Determines the color of new square
        if (newColumn+newRow)%2 == 0:
            newColor = COLOR1
        else:
            newColor = COLOR2

        # Redraw the squares
        self.drawSquare(SQUARESIZE*(currentColumn+1), SQUARESIZE*(currentRow+1), currentColor)
        self.drawSquare(SQUARESIZE*(newColumn+1), SQUARESIZE*(newRow+1), newColor)

        # Gets name of the piece and corresponding image
        piece = piece.getColor()+piece.getName()
        piecePic = GraphicsImage("pieces/"+piece+".png")

        # Draws the piece            
        canvas.drawImage(3/2*SQUARESIZE+(newColumn)*SQUARESIZE-32, \
                         (newRow+1)*SQUARESIZE+5, piecePic)

        return pieceTaken

    # Moves piece from one position (current)
    # to another position (new). This is used
    # solely by the DeepYellowJ. It is similar
    # to self.move but this one doesn't redraw
    # the squares or piece.
    #
    # Parameters:
    #   current    - String
    #   new        - String
    # Returns:
    #   pieceTaken - Piece
    def move2(self, current, new):
        currentRow, currentColumn = self.findRowAndColumn(current)
        newRow, newColumn = self.findRowAndColumn(new)

        piece = self._board[currentColumn][currentRow]
        piece.changedMoved()
        pieceTaken = self._board[newColumn][newRow]
        self._board[newColumn][newRow] = piece
        self._board[currentColumn][currentRow] = None

        return pieceTaken

    # Puts a piece in a position.
    #
    # Parameters:
    #   pieceName - String
    #   color     - String
    #   position  - String
    def putPiece(self, pieceName, color, position):
        row, column = self.findRowAndColumn(position)
        self._board[column][row] = Piece(pieceName, color, 5)
    
    # Gets the piece at a given position.
    #
    # Parameters:
    #   position - String
    # Returns:
    #   piece    - Piece
    def getPiece(self, position):
        row, column = self.findRowAndColumn(position)
        piece = self._board[column][row]
        return piece

    # Sets the board in the starting position.
    # And makes calls to draw board and pieces  
    def initialize(self):
        # Creates the Graphics Window & canvas
        self._window = GraphicsWindow((SIZE-1)*100, (SIZE-1)*100)
        self._canvas = self._window.canvas()

        # Used to initialize the pieces
        color = ["b", "w"]
        piece = ["K", "Q", "R", "N", "B", "P"]

        # Create the pieces for black
        self._board[0][0] = Piece(piece[2], color[0], 5)
        self._board[1][0] = Piece(piece[3], color[0], 3)
        self._board[2][0] = Piece(piece[4], color[0], 3)
        self._board[3][0] = Piece(piece[1], color[0], 9)
        self._board[4][0] = Piece(piece[0], color[0], 100)
        self._board[5][0] = Piece(piece[4], color[0], 3)
        self._board[6][0] = Piece(piece[3], color[0], 3)
        self._board[7][0] = Piece(piece[2], color[0], 5)

        # Create the black pawns
        for i in range(SIZE):
            self._board[i][1] = Piece(piece[5], color[0], 1)

        # Create the pieces for white
        self._board[0][7] = Piece(piece[2], color[1], 5)
        self._board[1][7] = Piece(piece[3], color[1], 3)
        self._board[2][7] = Piece(piece[4], color[1], 3)
        self._board[3][7] = Piece(piece[1], color[1], 9)
        self._board[4][7] = Piece(piece[0], color[1], 100)
        self._board[5][7] = Piece(piece[4], color[1], 3)
        self._board[6][7] = Piece(piece[3], color[1], 3)
        self._board[7][7] = Piece(piece[2], color[1], 5)

        # Create the white pawns
        for i in range(SIZE):
            self._board[i][6] = Piece(piece[5], color[1], 1)

        # Make calls to draw board and pieces
        self.drawBoard()
        self.drawPieces()

    # Draws every piece on the board.
    def drawPieces(self):
        canvas = self._canvas
        
        for i in range(SIZE):
            for j in range(SIZE):
                piece = self._board[i][j]

                if piece != None:
                    piece = piece.getColor()+piece.getName()
                    # Gets image file (png) from pieces folder
                    piecePic = GraphicsImage("pieces/"+piece+".png")
                    
                    canvas.drawImage(3/2*SQUARESIZE+(i)*SQUARESIZE-32, \
                                (j+1)*SQUARESIZE+5, piecePic)

    # Draws the board
    def drawBoard(self):
        self._window.setTitle("DeepYellowJ")
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        canvas = self._canvas
        canvas.setBackground("green")

        # Draws the Title: DeepYellowJ
        canvas.setTextFont("times", "bold", 24)
        canvas.drawText(260, 5, "DeepYellowJ")

        # Changes the font and size for headers
        canvas.setTextFont("times", "bold", 16)
        
        canvas.setLineWidth(3)

        for i in range(SIZE):
            # Write the letters for column identification
            canvas.drawText(3/2*SQUARESIZE+(i)*SQUARESIZE-10, \
                            SQUARESIZE-30, columns[i])
            canvas.drawText(3/2*SQUARESIZE+(i)*SQUARESIZE-10, \
                            9*SQUARESIZE+10, columns[i])

            # Write the numbers for row identification
            canvas.drawText(SQUARESIZE-30, 3/2*SQUARESIZE+i*SQUARESIZE-10, \
                            (SIZE-i))
            canvas.drawText(9*SQUARESIZE+15, 3/2*SQUARESIZE+i*SQUARESIZE-10, \
                            (SIZE-i))
            
            for j in range(SIZE):
                # Used to determine the color of board
                if ((i+j)%2 == 0):
                    color = (COLOR1)
                else:
                    color = (COLOR2)

                # Draws a square
                self.drawSquare(SQUARESIZE*(j+1), SQUARESIZE*(i+1), color)

    # Resets the board setup
    def resetBoard(self):
        self._board =[[None for i in range(SIZE)]for j in range(SIZE)]
        self.initialize()

    # Used to find the row and column of each position
    #
    # Parameters:
    #   position      - String
    # Returns:
    #   (row, column) - int
    def findRowAndColumn(self, position):
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        
        column = columns.index(position[0])
        row = SIZE - int(position[1])

        return row, column

    # Used to draw individual squares
    #
    # Parameters:
    #   x     - int
    #   y     - int
    #   color - String
    def drawSquare(self, x, y, color):
        canvas = self._canvas

        canvas.setFill(color)
        canvas.setOutline("black")
        canvas.drawRect(x, y, SQUARESIZE, SQUARESIZE)
