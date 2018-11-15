from time import sleep
from board import Board
from legalmovechecker import LegalMoveChecker
from player import Player
from deepYellowJ import DeepYellowJ
from ezgraphics import *

def test():
    m1 = "D2"
    m2 = "D4"
    m3 = "H2"
    board = Board()
    board._window = GraphicsWindow((8-1)*100, (8-1)*100)
    board._canvas = board._window.canvas()
    board.drawBoard()
    board.putPiece("R", "w", m1)
    board.putPiece("Q", "b", m3)
    board.putPiece("K", "b", "D8")
    board.drawPieces()

    lC = LegalMoveChecker(board)
    dY = DeepYellowJ("w", board)
    moves = dY.findMove()
    print(moves)

    lC.updateBoard(board)
    dY.updateBoard(board)
    
    print(lC.isLegalMove(moves[0], moves[1]))
    if (lC.isLegalMove(moves[0], moves[1])):
        sleep(1)
        board.move(moves[0], moves[1])

    moves = dY.findAllMoves()
    print(moves)
    
    
    
test()
