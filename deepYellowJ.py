## DeepYellowJ - Version 0.1 (c) 2016 Ahmad Nazeri
#    DeepYellowJ - deepYellowJ.py
#
# This file is the AI portion of the chess program.
# It is the main DeepYellowJ part. It finds the best
# move from all the moves in each board setup. 

# Import classes from other files
from board import Board

# Import randint for selecting random moves
from random import randint

# Board Size
SIZE = 8

class DeepYellowJ:
    # Constructor for DeepYellowJ.
    #
    # Parameters:
    #   move  - String
    #   board - Board
    def __init__(self, color, board):
        self._color = color
        self._board = board
        
    # Finds the best move at a given position.
    #
    # Returns:
    #   moves - []  
    def findMove(self):
        # Gets all possible moves
        allMoves = self.findAllMoves()

        # Used to calculate moves and f(move)
        potentialMoves = []
        potentialMovesScore = []

        # Gets 24 Random Moves
        for i in range(3*SIZE):
            movePosition = randint(0, len(allMoves)-1)
            pieceToMove = allMoves[movePosition][0]
            positionToMoveTo = allMoves[movePosition][1][randint(0, len(allMoves[movePosition][1])-1)]
            moves = [pieceToMove, positionToMoveTo]
            potentialMoves.append(moves)

        # Calculates the f-score for each selected move
        for i in range(len(potentialMoves)):
            moveScore = self.calculateMove(potentialMoves[i])
            potentialMovesScore.append(moveScore)

        # Returns the max move
        move = potentialMoves[potentialMovesScore.index(max(potentialMovesScore))]

        return move
    
    # Finds the heuristic function value for a given
    # move (move). The heuristic function currently
    # used is a modification of Claude Shannon. This
    # function was presented in his paper, "Programming
    # a Computer for Playing Chess".
    #
    # Parameters:
    #   move - String
    # Returns:
    #   f    - int  
    def calculateMove(self, move):
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        # Used to count Pawns, Bishops, Knights, Rooks, Queens, and Kings
        pieceCountSelf = [0, 0, 0, 0, 0, 0]
        pieceCountOpponent = [0, 0, 0, 0, 0, 0]

        # Used to copy board
        board = Board()

        # Copies the pieces from self._board
        for i in range(SIZE):
            for j in range(SIZE):
                square = columns[j]+str(SIZE-i)
                piece = self._board.getPiece(square)

                if piece != None:
                    board.putPiece(piece.getName(), piece.getColor, square)

        # Moves piece
        board.move2(move[0], move[1])

        # Used to count the number of each type of piece
        for i in range(SIZE):
            for j in range(SIZE):
                square = columns[j]+str(SIZE-i)
                piece = board.getPiece(square)

                if piece != None:
                    if piece.getColor() == self._color:
                        if piece.getName() == "P":
                            pieceCountSelf[0] = pieceCountSelf[0]+1
                        elif piece.getName() == "B":
                            pieceCountSelf[1] = pieceCountSelf[1]+1
                        elif piece.getName() == "N":
                            pieceCountSelf[2] = pieceCountSelf[2]+1
                        elif piece.getName() == "R":
                            pieceCountSelf[3] = pieceCountSelf[3]+1
                        elif piece.getName() == "Q":
                            pieceCountSelf[4] = pieceCountSelf[4]+1
                        elif piece.getName() == "K":
                            pieceCountSelf[5] = pieceCountSelf[5]+1
                    else:
                        if piece.getName() == "P":
                            pieceCountOpponent[0] = pieceCountOpponent[0]+1
                        elif piece.getName() == "B":
                            pieceCountOpponent[1] = pieceCountOpponent[1]+1
                        elif piece.getName() == "N":
                            pieceCountOpponent[2] = pieceCountOpponent[2]+1
                        elif piece.getName() == "R":
                            pieceCountOpponent[3] = pieceCountOpponent[3]+1
                        elif piece.getName() == "Q":
                            pieceCountOpponent[4] = pieceCountOpponent[4]+1
                        elif piece.getName() == "K":
                            pieceCountOpponent[5] = pieceCountOpponent[5]+1

        # Calculates f(move)             
        f = 200*(pieceCountSelf[5] - pieceCountOpponent[5]) + \
            9*(pieceCountSelf[4] - pieceCountOpponent[4]) + \
            5*(pieceCountSelf[3] - pieceCountOpponent[3]) + \
            3*(pieceCountSelf[2] - pieceCountOpponent[2]) + \
            3*(pieceCountSelf[1] - pieceCountOpponent[1]) + \
            1*(pieceCountSelf[0] - pieceCountOpponent[0])

        return f
    
    # Finds all moves at a given board setup.
    # 
    # Returns:
    #   allMoves - []  
    def findAllMoves(self):
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        allMoves = []

        # Goes through each square
        for i in range(SIZE):
            for j in range(SIZE):
                square = columns[j]+str(SIZE-i)
                piece = self._board.getPiece(square)

                # Checks only self's pieces
                if piece != None and piece.getColor() == self._color:
                    if piece.getName() == "P":
                        moves = [square, self.findPawnMoves(square)]
                    elif piece.getName() == "B":
                        moves = [square, self.findBishopMoves(square)]
                    elif piece.getName() == "N":
                        moves = [square, self.findKnightMoves(square)]
                    elif piece.getName() == "R":
                        moves = [square, self.findRookMoves(square)]
                    elif piece.getName() == "Q":
                        moves = [square, self.findQueenMoves(square)]
                    elif piece.getName() == "K":
                        moves = [square, self.findKingMoves(square)]

                    # If moves found, then append
                    if len(moves[1]) != 0:
                        allMoves.append(moves)

        return allMoves

    # Finds all moves at a given position (current)
    # for a given direction. Please note that the
    # parameter longDistance is used to determine if
    # piece can move multiple spaces in one move.
    #
    # Parameters:
    #   current      - String
    #   rowMove      - int
    #   columnMove   - int
    #   longDistance - Boolean (=False)
    # Returns:
    #   moves        - []    
    def findMovesForPiece(self, current, rowMove, columnMove, longDistance=False):
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        moves = []
        currentPiece = self._board.getPiece(current)

        # If piece isn't in current space
        if currentPiece != None:
            currentColor = currentPiece.getColor()
        else:
            return moves

        # If piece can move multiple spaces in one move
        if longDistance:
            currentLetter = current[0]
            currentNumber = int(current[1])
            currentLetterIndex = columns.index(currentLetter)

            # Move the piece one space
            currentLetterIndex = currentLetterIndex + columnMove
            currentNumber = currentNumber + rowMove

            # Determine if legal move
            if ((currentLetterIndex > -1 and currentLetterIndex < 8) \
                and (currentNumber > 0 and currentNumber < 9)):
                current = columns[currentLetterIndex]+str(currentNumber)
            else:
                return moves
            
            # Move piece until new/out of board/current is occupied                
            while self._board.getPiece(current) == None:
                moves.append(current)
                
                currentLetter = current[0]
                currentNumber = int(current[1])
                currentLetterIndex = columns.index(currentLetter)

                # Move one space
                currentLetterIndex = currentLetterIndex + columnMove
                currentNumber = currentNumber + rowMove

                # Checks if current is on board
                if ((currentLetterIndex > -1 and currentLetterIndex < 8) \
                    and (currentNumber > 0 and currentNumber < 9)):
                    current = columns[currentLetterIndex]+str(currentNumber)
                else:
                    return moves               

            piece = self._board.getPiece(current)

            # Checks so space is not one's own piece            
            if piece.getColor() != self._color:
                moves.append(current)

        else:
            currentLetter = current[0]
            currentNumber = int(current[1]) + rowMove
            currentLetterIndex = columns.index(currentLetter) + columnMove

            # Checks if current + move = new 
            if ((currentLetterIndex > -1 and currentLetterIndex < 8) \
                and (currentNumber > 0 and currentNumber < 9)):
                current = columns[currentLetterIndex]+str(currentNumber)
                moves.append(current)

        return moves

    # Finds all Pawn moves at a given position (square)
    #
    # Parameters:
    #   square    - String
    # Returns:
    #   pawnMoves - []
    def findPawnMoves(self, square):
        piece = self._board.getPiece(square)

        # Used to determine the direction
        # the pawn is heading
        if piece.getColor() == "b":
            constant = -1
        else:
            constant = 1        

        # Finds the moves in each direction
        move1 = self.findMovesForPiece(square, constant, 0)
        move2 = self.findMovesForPiece(square, constant, -1)
        move3 = self.findMovesForPiece(square, constant, 1)

        # Used to determine pawn can move two spaces
        if len(move1) != 0:
            piece1 = self._board.getPiece(move1[0])
        else:
            piece1 = False

        # Used to determine if pawn can take diagonal
        if len(move2) != 0:       
            piece2 = self._board.getPiece(move2[0])
        else:
            piece2 = None

        # Used to determine if pawn can take diagonal
        if len(move3) != 0:
            piece3 = self._board.getPiece(move3[0])
        else:
            piece3 = None

        # If there is piece, pawn cannot move up
        if piece1 != None:
            move1 = []

        # If opponent's piece is not diagonal, pawn
        # cannot take piece. 
        if piece2 == None or piece2.getColor() == self._color:
            move2 = []

        # If opponent's piece is not diagonal, pawn
        # cannot take piece. 
        if piece3 == None or piece3.getColor() == self._color:
            move3 = []

        # Determines if pawn can move two spaces
        if not piece.getPieceMoved() and piece1 == None:
            move4 = self.findMovesForPiece(square, 2*constant, 0)
            if len(move4) != 0:
                piece4 = self._board.getPiece(move4[0])
                if piece4 != None:
                    move4 = []
        else:
            move4 = []                    

        # Combine the move1...move4 arrays
        pawnMoves = self.combineArrays(move1, move2)
        pawnMoves = self.combineArrays(pawnMoves, move3)
        pawnMoves = self.combineArrays(pawnMoves, move4)

        # Returns all Pawn moves
        return pawnMoves

    # Finds all Bishop moves at a given position (square)
    #
    # Parameters:
    #   square      - String
    # Returns:
    #   bishopMoves - []
    def findBishopMoves(self, square):
        # Finds the moves in each direction, True is used
        # to state that it can move one space at a time
        move1 = self.findMovesForPiece(square, 1, 1, True)
        move2 = self.findMovesForPiece(square, 1, -1, True)
        move3 = self.findMovesForPiece(square, -1, -1, True)
        move4 = self.findMovesForPiece(square, -1, 1, True)

        # Combine the move1...move4 arrays
        bishopMoves = self.combineArrays(move1, move2)
        bishopMoves = self.combineArrays(bishopMoves, move3)
        bishopMoves = self.combineArrays(bishopMoves, move4)

        # Returns all Bishop moves
        return bishopMoves

    # Finds all Knight moves at a given position (square)
    #
    # Parameters:
    #   square      - String
    # Returns:
    #   knightMoves - []
    def findKnightMoves(self, square):
        # Finds the moves in each direction
        move1 = self.findMovesForPiece(square, 1, 2)
        move2 = self.findMovesForPiece(square, 1, -2)
        move3 = self.findMovesForPiece(square, -1, 2)
        move4 = self.findMovesForPiece(square, -1, -2)
        move5 = self.findMovesForPiece(square, 2, 1)
        move6 = self.findMovesForPiece(square, 2, -1)
        move7 = self.findMovesForPiece(square, -2, 1)
        move8 = self.findMovesForPiece(square, -2, -1)

        # Checks if move1...move8 is occupied by one's piece
        if len(move1) != 0:
            piece1 = self._board.getPiece(move1[0])
            if piece1 != None and piece1.getColor() == self._color:
                move1 = []
            
        if len(move2) != 0:
            piece2 = self._board.getPiece(move2[0])
            if piece2 != None and piece2.getColor() == self._color:
                move2 = []

        if len(move3) != 0:
            piece3 = self._board.getPiece(move3[0])
            if piece3 != None and piece3.getColor() == self._color:
                move3 = []

        if len(move4) != 0:
            piece4 = self._board.getPiece(move4[0])
            if piece4 != None and piece4.getColor() == self._color:
                move4 = []

        if len(move5) != 0:
            piece5 = self._board.getPiece(move5[0])
            if piece5 != None and piece5.getColor() == self._color:
                move5 = []
            
        if len(move6) != 0:
            piece6 = self._board.getPiece(move6[0])
            if piece6 != None and piece6.getColor() == self._color:
                move6 = []

        if len(move7) != 0:
            piece7 = self._board.getPiece(move7[0])
            if piece7 != None and piece7.getColor() == self._color:
                move7 = []

        if len(move8) != 0:
            piece8 = self._board.getPiece(move8[0])
            if piece8 != None and piece8.getColor() == self._color:
                move8 = []

        # Combine the move1...move8 arrays
        knightMoves = self.combineArrays(move1, move2)
        knightMoves = self.combineArrays(knightMoves, move3)
        knightMoves = self.combineArrays(knightMoves, move4)
        knightMoves = self.combineArrays(knightMoves, move5)
        knightMoves = self.combineArrays(knightMoves, move6)
        knightMoves = self.combineArrays(knightMoves, move7)
        knightMoves = self.combineArrays(knightMoves, move8)

        # Returns all Knight moves
        return knightMoves

    # Finds all Rook moves at a given position (square)
    #
    # Parameters:
    #   square    - String
    # Returns:
    #   rookMoves - []
    def findRookMoves(self, square):
        # Finds the moves in each direction, True is used
        # to state that it can move one space at a time
        move1 = self.findMovesForPiece(square, 0, 1, True)
        move2 = self.findMovesForPiece(square, 0, -1, True)
        move3 = self.findMovesForPiece(square, 1, 0, True)
        move4 = self.findMovesForPiece(square, -1, 0, True)
        
        # Combine the move1...move4 arrays
        rookMoves = self.combineArrays(move1, move2)
        rookMoves = self.combineArrays(rookMoves, move3)
        rookMoves = self.combineArrays(rookMoves, move4)

        # Returns all Rook moves
        return rookMoves

    # Finds all Queen moves at a given position (square)
    #
    # Parameters:
    #   square     - String
    # Returns:
    #   queenMoves - []
    def findQueenMoves(self, square):
        # Finds the moves in each direction, True is used
        # to state that it can move one space at a time
        move1 = self.findMovesForPiece(square, 0, 1, True)
        move2 = self.findMovesForPiece(square, 0, -1, True)
        move3 = self.findMovesForPiece(square, 1, 0, True)
        move4 = self.findMovesForPiece(square, 1, 1, True)
        move5 = self.findMovesForPiece(square, 1, -1, True)
        move6 = self.findMovesForPiece(square, -1, 0, True)
        move7 = self.findMovesForPiece(square, -1, 1, True)
        move8 = self.findMovesForPiece(square, -1, -1, True)

        # Combine the move1...move8 arrays
        queenMoves = self.combineArrays(move1, move2)
        queenMoves = self.combineArrays(queenMoves, move3)
        queenMoves = self.combineArrays(queenMoves, move4)
        queenMoves = self.combineArrays(queenMoves, move5)
        queenMoves = self.combineArrays(queenMoves, move6)
        queenMoves = self.combineArrays(queenMoves, move7)
        queenMoves = self.combineArrays(queenMoves, move8)

        # Returns all Queen moves
        return queenMoves

    # Finds all King moves at a given position (square)
    #
    # Parameters:
    #   square    - String
    # Returns:
    #   kingMoves - []
    def findKingMoves(self, square):
        # Finds the moves in each direction
        move1 = self.findMovesForPiece(square, 0, 1)
        move2 = self.findMovesForPiece(square, 0, -1)
        move3 = self.findMovesForPiece(square, 1, 0)
        move4 = self.findMovesForPiece(square, 1, 1)
        move5 = self.findMovesForPiece(square, 1, -1)
        move6 = self.findMovesForPiece(square, -1, 0)
        move7 = self.findMovesForPiece(square, -1, 1)
        move8 = self.findMovesForPiece(square, -1, -1)

        # Checks if move1...move8 is occupied by one's piece
        if len(move1) != 0:
            piece1 = self._board.getPiece(move1[0])
            if piece1 != None and piece1.getColor() == self._color:
                move1 = []
            
        if len(move2) != 0:
            piece2 = self._board.getPiece(move2[0])
            if piece2 != None and piece2.getColor() == self._color:
                move2 = []

        if len(move3) != 0:
            piece3 = self._board.getPiece(move3[0])
            if piece3 != None and piece3.getColor() == self._color:
                move3 = []

        if len(move4) != 0:
            piece4 = self._board.getPiece(move4[0])
            if piece4 != None and piece4.getColor() == self._color:
                move4 = []

        if len(move5) != 0:
            piece5 = self._board.getPiece(move5[0])
            if piece5 != None and piece5.getColor() == self._color:
                move5 = []
            
        if len(move6) != 0:
            piece6 = self._board.getPiece(move6[0])
            if piece6 != None and piece6.getColor() == self._color:
                move6 = []

        if len(move7) != 0:
            piece7 = self._board.getPiece(move7[0])
            if piece7 != None and piece7.getColor() == self._color:
                move7 = []

        if len(move8) != 0:
            piece8 = self._board.getPiece(move8[0])
            if piece8 != None and piece8.getColor() == self._color:
                move8 = []

        # Combine the move1...move8 arrays
        kingMoves = self.combineArrays(move1, move2)
        kingMoves = self.combineArrays(kingMoves, move3)
        kingMoves = self.combineArrays(kingMoves, move4)
        kingMoves = self.combineArrays(kingMoves, move5)
        kingMoves = self.combineArrays(kingMoves, move6)
        kingMoves = self.combineArrays(kingMoves, move7)
        kingMoves = self.combineArrays(kingMoves, move8)

        # Return all King moves
        return kingMoves

    # Combines two arrays. It is used to
    # combine to arrays of moves.
    # 
    # Parameters:
    #   array1 - []
    #   array2 - []
    # Returns:
    #   array1 - []
    def combineArrays(self, array1, array2):
        for i in range(len(array2)):
            array1.append(array2[i])
        return array1

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
