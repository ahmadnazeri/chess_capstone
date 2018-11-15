## DeepYellowJ - Version 0.1 (c) 2016 Ahmad Nazeri
#    Piece - piece.py
#
# This file is the object class for a piece.
# The piece keeps track of name, color,
# point value, and if it has been moved.

class Piece:
    # Constructor for Piece.
    #
    # Parameters:
    #   name       - String
    #   color      - String
    #   pointValue - int
    def __init__(self, name, color, pointValue):
        self._name = name
        self._color = color
        self._pointValue = pointValue
        self._moved = False

    # Change once the piece has moved
    def changedMoved(self):
        self._moved = True
        
    # Changes the name of piece
    #
    # Parameter:
    #   name - String
    def changeName(self, name):
        self._name = name

    # Changes the point value of the piece
    #
    # Parameters:
    #   pointValue - int
    def changePointValue(self, pointValue):
        self._pointValue = pointValue

    ## USED TO RETURN PRIVATE VARIABLES
    # Returns the name of the piece
    #
    # Returns:
    #   self._name - String
    def getName(self):
        return self._name
    
    # Returns the color of the piece:
    #
    # Returns:
    #   self._color - String
    def getColor(self):
        return self._color

    # Returns the point value of piece
    # 
    # Returns:
    #   self._pointValue - int
    def getPointValue(self):
        return self._pointValue

    # Returns whether piece has moved or not
    # Returns: (boolean)
    def getPieceMoved(self):
        return self._moved
        
