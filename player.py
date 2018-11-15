## DeepYellowJ - Version 0.1 (c) 2016 Ahmad Nazeri
#    Player - player.py
#
# This file is the object class for a player.
# The player keeps track of color, computer,
# piecesTaken, and DeepYellowJ.

# Import classes from other files
from deepYellowJ import DeepYellowJ

class Player:
    # Constructor for Player.
    #
    # Parameters:
    #   color    - String
    #   computer - Boolean
    #   board    - Board
    def __init__(self, color, computer, board):
        self._color = color
        self._computer = computer
        self._piecesTaken = []
        self._AI = DeepYellowJ(color, board)

    # Adds taken piece to self._piecesTaken.
    #
    # Parameter:
    #   piece - Piece  
    def addPieceTaken(self, piece):
        self._piecesTaken.append(piece)

    # Gets the color of Player.
    #
    # Return:
    #   self._color - String 
    def color(self):
        return self._color

    # Gets a move from DeepYellowJ or user.
    #
    # Return:
    #   moves - [] 
    def getMove(self):
        if self.isComputer():
            return self._AI.findMove()
        else:
            moves = input("Please enter move separated by space ")
            return moves.split()           

    # Returns if Player is computer
    #
    # Return:
    #   self._computer - Boolean
    def isComputer(self):
        return self._computer
    
