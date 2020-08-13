# coding : utf-8

# Imports
from core.player import Player
from core.chessparts import Chessparts
from core.chessboard import Chessboard

# Additionnal code

# Variables
chessboard = Chessboard()
player_1 = Player("Red", 1)
player_2 = Player("Blue", 2)

def gameflow():
    chessboard.print_board()
    chessboard.print_parts(player_1.chess_pieces, player_2.chess_pieces)

# Main
if __name__ == "__main__":
    gameflow()
    input()
