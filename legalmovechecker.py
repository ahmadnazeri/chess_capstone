## DeepYellowJ - Version 0.1 (c) 2016 Ahmad Nazeri
#    LegalMoveChecker - legalmovechecker.py
#
# This file determines if a move is
# a legal chess move. It keeps track
# of the board.

# Used to determine the size of board
SIZE = 8

class LegalMoveChecker:
    # Constructor of LegalMoveChecker
    # 
    # Parameters:
    #   board - Board
    def __init__(self, board):
        self._board = board

    # Determines if a move is a legal
    # chess move.
    #
    # Parameters:
    #   current         - String
    #   new             - String
    # Returns:
    #   (if legal move) - Boolean          
    def isLegalMove(self, current, new):
        currentRow, currentColumn = self.findRowAndColumn(current)
        piece = self._board.getPiece(current)

        # If current position is empty,
        # return False
        if piece == None:
            return False

        # Calls the correct method for current piece
        if piece.getName() == "P":
            return self.isLegalPawnMove(current, new)
        elif piece.getName() == "B":
            return self.isLegalBishopMove(current, new)
        elif piece.getName() == "N":
            return self.isLegalKnightMove(current, new)
        elif piece.getName() == "R":
            return self.isLegalRookMove(current, new)
        elif piece.getName() == "Q":
            return self.isLegalQueenMove(current, new)
        elif piece.getName() == "K":
            return self.isLegalKingMove(current, new)
        
    # Determines if a move is a legal
    # chess move for a given piece in
    # a certain direction.
    # Note: longDistance is set to True
    # if a piece can move multiple spaces
    # in one move.
    #
    # Parameters:
    #   current         - String
    #   new             - String
    #   rowMove         - int
    #   colMove         - int
    #   longDistance    - Boolean (=False)
    # Returns:
    #   (if legal move) - Boolean
    def isLegalPieceMove(self, current, new, rowMove, colMove, longDistance = False):
        # Used to go through corresponding square(s)
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]

        currentPiece = self._board.getPiece(current)
        newPiece = self._board.getPiece(new)

        # Used to move through squares
        currentRow, currentColumn = self.findRowAndColumn(current)
        newRow, newColumn = self.findRowAndColumn(new)

        # If current piece doesn't exist,
        # then return False
        if currentPiece != None:
            currentColor = currentPiece.getColor()
        else:
            return False
        
        # Used to prevent currentPiece capturing
        # it's own piece. 
        if newPiece != None:
            newColor = newPiece.getColor()

        # If piece can move multiple spaces in one move
        if longDistance:
            currentLetter = current[0]
            currentNumber = int(current[1])
            currentLetterIndex = columns.index(currentLetter)

            # Move the piece one space
            currentLetterIndex = currentLetterIndex + colMove
            currentNumber = currentNumber + rowMove

            # Determine if legal move
            if ((currentLetterIndex > -1 and currentLetterIndex < 8) \
                and (currentNumber > 0 and currentNumber < 9)):
                current = columns[currentLetterIndex]+str(currentNumber)
            else:
                return False
            
            # Move piece until new/out of board/current is occupied
            while self._board.getPiece(current) == None and current != new:
                currentLetter = current[0]
                currentNumber = int(current[1])
                currentLetterIndex = columns.index(currentLetter)

                # Move one space
                currentLetterIndex = currentLetterIndex + colMove
                currentNumber = currentNumber + rowMove

                # Checks if current is on board
                if ((currentLetterIndex > -1 and currentLetterIndex < 8) \
                    and (currentNumber > 0 and currentNumber < 9)):
                    current = columns[currentLetterIndex]+str(currentNumber)
                else:
                    return False               

            if current == new:
                # Checks to see that new space is not occupied and pieces aren't same color
                if newPiece != None and currentPiece.getColor() == newPiece.getColor():
                    return False
                else:
                    return True
            else:
                return False
        else:
            currentLetter = current[0]
            currentNumber = int(current[1])
            currentLetterIndex = columns.index(currentLetter)

            # Checks if current + move = new            
            if ((currentRow+rowMove) == newRow and (currentColumn+colMove) == newColumn):
                # Checks to see that new space is not occupied and pieces aren't same color
                if newPiece != None and currentPiece.getColor() == newPiece.getColor():
                    return False
                else:
                    return True
            else:
                return False
        
    # Finds if Pawn at current square can
    # move to new square.
    #
    # Parameters:
    #   current              - String
    #   new                  - String
    # Returns:
    #   (if legal Pawn move) - Boolean
    def isLegalPawnMove(self, current, new):
        currentRow, currentColumn = self.findRowAndColumn(current)
        newRow, newColumn = self.findRowAndColumn(new)

        currentPiece = self._board.getPiece(current)
        newPiece = self._board.getPiece(new)

        # If current space doesn't have a piece
        if currentPiece != None:
            currentColor = currentPiece.getColor()
        else:
            return False

        # Checks if new position is occupied
        if currentColumn == newColumn and newPiece is not None:
            return False

        # Determines the direction the pawn will be moving
        if currentColor == "b":
            constant = 1
        else:
            constant = -1        

        # Checks if Pawn can move up one space
        move1 = self.isLegalPieceMove(current, new, constant, 0)

        piece1Letter = current[0]
        piece1Number = int(current[1]) + constant
        piece1 = self._board.getPiece(piece1Letter+str(piece1Number))

        # Checks so Pawn doesn't take it's own piece        
        if newPiece != None and currentPiece.getColor() != newPiece.getColor():
            move2 = self.isLegalPieceMove(current, new, constant, -1)
        else:
            move2 = False

        # Checks so Pawn doesn't take it's own piece   
        if newPiece != None and currentPiece.getColor() != newPiece.getColor():            
            move3 = self.isLegalPieceMove(current, new, constant, 1)
        else:
            move3 = False

        # Checks if Pawn can move up two spaces
        if not currentPiece.getPieceMoved():
            move4 = self.isLegalPieceMove(current, new, 2*constant, 0)
        else:
            move4 = False

        # If one direction, then it is a legal move.
        if move1 or move2 or move3 or move4:
            return True
        else:
            return False

    # Finds if Bishop at current square can
    # move to new square.
    #
    # Parameters:
    #   current                - String
    #   new                    - String
    # Returns:
    #   (if legal Bishop move) - Boolean
    def isLegalBishopMove(self, current, new):
        currentPiece = self._board.getPiece(current)
        newPiece = self._board.getPiece(new)

        # Checks so Bishop doesn't take it's own piece
        if newPiece != None and currentPiece.getColor() == newPiece.getColor():
            return False

        # Checks for all possible directions
        move1 = self.isLegalPieceMove(current, new, 1, 1, True)
        move2 = self.isLegalPieceMove(current, new, 1, -1, True)
        move3 = self.isLegalPieceMove(current, new, -1, 1, True)
        move4 = self.isLegalPieceMove(current, new, -1, -1, True)

        # If one direction, then it is a legal move.
        if move1 or move2 or move3 or move4:
            return True
        else:
            return False

    # Finds if Knight at current square can
    # move to new square.
    #
    # Parameters:
    #   current                - String
    #   new                    - String
    # Returns:
    #   (if legal Knight move) - Boolean
    def isLegalKnightMove(self, current, new):
        currentPiece = self._board.getPiece(current)
        newPiece = self._board.getPiece(new)

        # Checks so Knight doesn't take it's own piece
        if newPiece != None and currentPiece.getColor() == newPiece.getColor():
            return False

        # Checks for all possible directions
        move1 = self.isLegalPieceMove(current, new, 1, 2)
        move2 = self.isLegalPieceMove(current, new, 1, -2)
        move3 = self.isLegalPieceMove(current, new, -1, 2)
        move4 = self.isLegalPieceMove(current, new, -1, -2)
        move5 = self.isLegalPieceMove(current, new, 2, 1)
        move6 = self.isLegalPieceMove(current, new, 2, -1)
        move7 = self.isLegalPieceMove(current, new, -2, 1)
        move8 = self.isLegalPieceMove(current, new, -2, -1)

        # If one direction, then it is a legal move.
        if move1 or move2 or move3 or move4 or \
           move5 or move6 or move7 or move8:
            return True
        else:
            return False

    # Finds if Rook at current square can
    # move to new square.
    #
    # Parameters:
    #   current              - String
    #   new                  - String
    # Returns:
    #   (if legal Rook move) - Boolean
    def isLegalRookMove(self, current, new):
        currentPiece = self._board.getPiece(current)
        newPiece = self._board.getPiece(new)

        # Checks so Rook doesn't take it's own piece
        if newPiece != None and currentPiece.getColor() == newPiece.getColor():
            return False

        # Checks for all possible directions
        move1 = self.isLegalPieceMove(current, new, 0, 1, True)
        move2 = self.isLegalPieceMove(current, new, 0, -1, True)
        move3 = self.isLegalPieceMove(current, new, 1, 0, True)
        move4 = self.isLegalPieceMove(current, new, -1, 0, True)

        # If one direction, then it is a legal move.
        if move1 or move2 or move3 or move4:
            return True
        else:
            return False

    # Finds if Queen at current square can
    # move to new square.
    #
    # Parameters:
    #   current               - String
    #   new                   - String
    # Returns:
    #   (if legal Queen move) - Boolean
    def isLegalQueenMove(self, current, new):
        currentPiece = self._board.getPiece(current)
        newPiece = self._board.getPiece(new)

        # Checks so Queen doesn't take it's own piece
        if newPiece != None and currentPiece.getColor() == newPiece.getColor():
            return False

        # Checks for all possible directions
        move1 = self.isLegalPieceMove(current, new, 0, 1, True)
        move2 = self.isLegalPieceMove(current, new, 0, -1, True)
        move3 = self.isLegalPieceMove(current, new, 1, 0, True)
        move4 = self.isLegalPieceMove(current, new, -1, 0, True)
        move5 = self.isLegalPieceMove(current, new, 1, 1, True)
        move6 = self.isLegalPieceMove(current, new, 1, -1, True)
        move7 = self.isLegalPieceMove(current, new, -1, 1, True)
        move8 = self.isLegalPieceMove(current, new, -1, -1, True)

        # If one direction, then it is a legal move.
        if move1 or move2 or move3 or move4 or \
           move5 or move6 or move7 or move8:
            return True
        else:
            return False

    # Finds if King at current square can
    # move to new square.
    #
    # Parameters:
    #   current              - String
    #   new                  - String
    # Returns:
    #   (if legal King move) - Boolean
    def isLegalKingMove(self, current, new):
        currentPiece = self._board.getPiece(current)
        newPiece = self._board.getPiece(new)

        # Checks for castling
        if newPiece != None and (currentPiece.getPieceMoved() == False and newPiece.getPieceMoved() == False):
            castle1 = self.isLegalPieceMove(current, new, 0, 1, True)
            castle2 = self.isLegalPieceMove(current, new, 0, -1, True)
        else:
            castle1 = False
            castle2 = False

        # Checks so King doesn't take it's own piece
        if newPiece != None and not (castle1 or castle2) and currentPiece.getColor() == newPiece.getColor():
            return False

        # Checks for all possible directions
        move1 = self.isLegalPieceMove(current, new, 0, 1)
        move2 = self.isLegalPieceMove(current, new, 0, -1)
        move3 = self.isLegalPieceMove(current, new, 1, 0)
        move4 = self.isLegalPieceMove(current, new, -1, 0)
        move5 = self.isLegalPieceMove(current, new, 1, 1)
        move6 = self.isLegalPieceMove(current, new, 1, -1)
        move7 = self.isLegalPieceMove(current, new, -1, 1)
        move8 = self.isLegalPieceMove(current, new, -1, -1)

        # If one direction or one castle is true, then
        # it is a legal move.
        if move1 or move2 or move3 or move4 or \
           move5 or move6 or move7 or move8 or \
           castle1 or castle2:
            return True
        else:
            return False
        
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
