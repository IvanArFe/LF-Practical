import sys
from antlr4 import *
from BoardGameLexer import BoardGameLexer
from BoardGameParser import BoardGameParser
from BoardGameListener import BoardGameListener

class BoardGameInterpreter(BoardGameListener):
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_type = None

    def enterGame(self, ctx:BoardGameParser.GameContext):
        self.game_type = ctx.gameType().getText()
        print(f"Game Type: {self.game_type}")
        if self.game_type == 'TicTacToe':
            self.print_board()

    def enterMove(self, ctx:BoardGameParser.MoveContext):
        player = ctx.player().getText()
        x = int(ctx.coordinate(0).getText())
        y = int(ctx.coordinate(1).getText())
        if player == 'player1':
            self.board[x][y] = 'X'
        elif player == 'player2':
            self.board[x][y] = 'O'
        print(f"{player} moves to ({x},{y})")
        self.print_board()

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)
        print()

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
