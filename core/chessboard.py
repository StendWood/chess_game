# coding: utf-8

# Imports
import os
import sys

# Additional code

# Variables
reset = "\033[0m"
blue = "\033[34m"
red = "\033[31m"

# Class
class Chessboard():
    """
        Generic class to manage chessboard
    """

    # Methods
    def __init__(self):
        """
            Chessboard constructor
        """
        # Instance properties
        self.p1_cemetery = []
        self.p2_cemetery = []


    def print_parts(self, p1_parts, p2_parts):
        for part in p1_parts:
            # Position to change in the terminal
            terminal_pos = f"\033[{part.position[1]};{part.position[0]}H"
            # Print the new position + color to the terminal
            print(f"{terminal_pos}{blue}{part.symbol}{reset}", end="")
        for part in p2_parts:
            terminal_pos = f"\033[{part.position[1]};{part.position[0]}H"
            print(f"{terminal_pos}{red}{part.symbol}{reset}", end="")




    def print_board(self):
        clear_console()
        for n in range(4):
            print("█ █ █ █ ")
            print(" █ █ █ █")
            
        print()

    def print_cemetery(self):
        pass

# Functions
def clear_console():
    """
        Clear the console depending on OS
    """
    if "win" in sys.platform.lower():
        # for windows
        os.system("cls")
    elif "linux" in sys.platform.lower():
        # for linux
        os.system("clear")
