import sys
from antlr4 import *
from BoardGameLexer import BoardGameLexer
from BoardGameParser import BoardGameParser
from BoardGameListener import BoardGameListener

class BoardGameInterpreter(BoardGameListener):
    def __init__(self):
        self.board = None
        self.game_type = None

    def enterGame(self, ctx:BoardGameParser.GameContext):
        self.game_type = ctx.gameType().getText()
        print(f"Game Type: {self.game_type}")

        if self.game_type == 'TicTacToe':
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.print_board_tictactoe()

    def enterMove(self, ctx: BoardGameParser.MoveContext):
        if self.game_type == 'TicTacToe':
            self.handle_tictactoe_move(ctx)

    def handle_tictactoe_move(self, ctx:BoardGameParser.MoveContext):
        player = ctx.player().getText()
        x = int(ctx.coordinate(0).getText())
        y = int(ctx.coordinate(1).getText())

        if not self.is_valid_move(x,y):
            print("Invalid move. Try again.")
            return

        if player == 'player1':
            self.board[x][y] = 'X'
        elif player == 'player2':
            self.board[x][y] = 'O'

        print(f"{player} moves to ({x},{y})")
        self.print_board_tictactoe()

        if self.check_winner('X'):
            print("Player 1 wins!")
        elif self.check_winner('0'):
            print("Player 2 wins!")
        elif self.is_board_full():
            print("It's a draw!")

    def print_board_tictactoe(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
        print()

    def is_valid_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == ' '

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Check rows
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Check columns
                return True
        if all(self.board[i][i] == player for i in range(3)):  # Check diagonal
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # Check anti-diagonal
            return True
        return False

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = BoardGameLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BoardGameParser(stream)
    tree = parser.program()

    listener = BoardGameInterpreter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
