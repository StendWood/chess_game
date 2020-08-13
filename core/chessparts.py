# coding: utf-8

# Imports

# Additional code

# Class
class Chessparts():
    """
        Generic class to manage chessparts
    """

    # Methods
    def __init__(self, position, color):
        """
            Chessparts constructor
        """
        # Instance properties
        self.position = position
        self.color = color


    def get_pos(self):
        print("This is the chessparts move")


    def move(self):
        pass


    def set_pos(self):
        pass


    def taken(self):
        pass


# Child Class
class King(Chessparts):
    """
        Create the King
    """

    def __init__(self, color, position):
        Chessparts.__init__(self, position, color)
        self.movements = 1
        self.name = "King"
        self.symbol = "K"
        self.check = False


class Queen(Chessparts):
    """
        Create the Queen
    """

    def __init__(self, color, position):
        Chessparts.__init__(self, position, color)
        self.movements = 1
        self.name = "Queen"
        self.symbol = "Q"


class Rook(Chessparts):
    """
        Create a Rook
    """

    def __init__(self, color, position):
        Chessparts.__init__(self, position, color)
        self.movements = 1
        self.name = "Rook"
        self.symbol = "R"


class Bishop(Chessparts):
    """
        Create a Bishop
    """

    def __init__(self, color, position):
        Chessparts.__init__(self, position, color)
        self.movements = 1
        self.name = "Bishop"
        self.symbol = "B"


class Knight(Chessparts):
    """
        Create a Knight
    """
    
    def __init__(self, color, position):
        Chessparts.__init__(self, position, color)
        self.movements = 1
        self.name = "Knight"
        self.symbol = "N"


class Pawn(Chessparts):
    """
        Create a Pawn
    """

    def __init__(self, color, position):
        Chessparts.__init__(self, position, color)
        self.movements = 1
        self.name = "Pawn"
        self.symbol = "P"
