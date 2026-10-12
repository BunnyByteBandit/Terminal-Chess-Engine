```python
import sys

class TerminalChess:
    """A lightweight terminal-based chess game display and board state tracker."""
    
    def __init__(self):
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        self.turn = "White"

    def print_board(self):
        print("\n   a  b  c  d  e  f  g  h")
        print("  +-----------------------+")
        for idx, row in enumerate(self.board):
            print(f"{8 - idx} | " + "  ".join(row) + f" | {8 - idx}")
        print("  +-----------------------+")
        print("   a  b  c  d  e  f  g  h\n")

    def start(self):
        print("=== Terminal Chess Engine ===")
        print("White: Uppercase | Black: Lowercase")
        self.print_board()

if __name__ == "__main__":
    game = TerminalChess()
    game.start()
