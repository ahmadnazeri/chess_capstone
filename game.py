## DeepYellowJ - Version 0.1 (c) 2016 Ahmad Nazeri
#    Game - game.py
#
# This file creates everything needed
# for the chess game.
# It creates:
#    1) Board
#    2) Players
#    3) LegalMoveChecker
# And it keeps track of the moves to
# look after the game is over. 

# Import classes from other files
from board import Board
from legalmovechecker import LegalMoveChecker
from player import Player
from deepYellowJ import DeepYellowJ

# Import a sleep, to pause between moves
from time import sleep

# Used to determine the size of board
SIZE = 8

# Game class is the main part of DeepYellowJ.
# It creates the board, players, and keeps track of
# whose move, what the last move, 50 moves, and previous
# 3 positions.
class Game():
    # The Constructor for Game class
    def __init__(self):
        self._gameNotation = []
        self._board = Board()
        self._player = [Player("w", True, self._board), Player("b", True, self._board)]
        self._whoseMove = 0
        self._mvChecker = LegalMoveChecker(self._board)
        self._lastMove= "" # not implemented yet
        self._move50 = 0 # not implemented yet
        self._previousPositions = [None for i in range(6)] # not implemented yet

    # Starts the Game
    def startGame(self):
        # Creates the chessboard and draws the board and pieces
        self._board.initialize()

        while not self.isGameOver():
            sleep(1) # used to pause between moves
            player = self._player[self._whoseMove] 
            moves = player.getMove() # receives move from player/DeepYellowJ

            # Checks if it is a legal move
            if self._mvChecker.isLegalMove(moves[0], moves[1]):
                # Makes the move
                self._board.move(moves[0], moves[1])
            else:
                print(moves[0] + ", " +  moves[1] + " Not Legal Move")

            # Keeps track of moves
            self._gameNotation.append((moves[0], moves[1]))
            
            # Updates whose move
            self._whoseMove = (self._whoseMove + 1)%2

    # Determines if the game is over
    # Currently, see if the King is taken
    # 
    # Returns:
    #   gameOver - Boolean
    def isGameOver(self):
        # Used to go through each square
        columns = ["A", "B", "C", "D", "E", "F", "G", "H"]
        gameOver = True

        # Goes through to find the King
        for i in range(SIZE):
            for j in range(SIZE):
                square = columns[j]+str(SIZE-i)
                piece = self._board.getPiece(square)
                player = self._player[self._whoseMove]

                # Determines if the King doesn't exist               
                if piece != None and piece.getName() == "K" and piece.getColor() == player.color():
                    gameOver = False

        return gameOver

    # Restarts the Game
    def restartGame(self):
        self._gameNotation = []
        self._board.resetBoard()
        self._player = [Player("w", True, self._board), Player("b", True, self._board)]
        self._mvChecker = LegalMoveChecker(self._board)        
        self.startGame()

# Starts the game!
g = Game()
g.startGame()
