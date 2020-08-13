# coding: utf-8

# Imports

# Additional code
import core.chessparts as cp

# Class

class Player():
    """
        Generic class to manage players
    """

    # Methods
    def __init__(self, color, user_id):
        """
            Player constructor
        """
        # Instance properties
        self.color = color
        self.user_id = user_id
        self.movement_counter = 0

        # Create the player parts depending on his id
        if self.user_id == 1:
            #                                         X  Y
            self.chess_pieces = [cp.Rook(self.color, (1, 1)), cp.Knight(self.color, (2, 1)), 
                                cp.Bishop(self.color, (3, 1)), cp.King(self.color, (4, 1)), 
                                cp.Queen(self.color, (5, 1)), cp.Bishop(self.color, (6, 1)), 
                                cp.Knight(self.color, (7, 1)), cp.Rook(self.color, (8, 1)),
                                cp.Pawn(self.color, (1, 2)), cp.Pawn(self.color, (2, 2)),
                                cp.Pawn(self.color, (3, 2)), cp.Pawn(self.color, (4, 2)),
                                cp.Pawn(self.color, (5, 2)), cp.Pawn(self.color, (6, 2)),
                                cp.Pawn(self.color, (7, 2)), cp.Pawn(self.color, (8, 2))]
        else:
            self.chess_pieces = [cp.Rook(self.color, (1, 8)), cp.Knight(self.color, (2, 8)), 
                                cp.Bishop(self.color, (3, 8)), cp.King(self.color, (4, 8)), 
                                cp.Queen(self.color, (5, 8)), cp.Bishop(self.color, (6, 8)), 
                                cp.Knight(self.color, (7, 8)), cp.Rook(self.color, (8, 8)),
                                cp.Pawn(self.color, (1, 7)), cp.Pawn(self.color, (2, 7)),
                                cp.Pawn(self.color, (3, 7)), cp.Pawn(self.color, (4, 7)),
                                cp.Pawn(self.color, (5, 7)), cp.Pawn(self.color, (6, 7)),
                                cp.Pawn(self.color, (7, 7)), cp.Pawn(self.color, (8, 7))]
