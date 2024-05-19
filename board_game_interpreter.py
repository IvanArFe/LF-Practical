import sys
from antlr4 import *
from BoardGameLexer import BoardGameLexer
from BoardGameParser import BoardGameParser
from BoardGameListener import BoardGameListener

class BoardGameInterpreter(BoardGameListener):
    #Inicialización de las variables
    def __init__(self):
        self.board = None
        self.game_type = None

    #Metodo para entrar al juego
    def enterGame(self, ctx:BoardGameParser.GameContext):
        self.game_type = ctx.gameType().getText() #Leemos el tipo de juego especificado en el fichero que se pasa por parámetro
        print(f"Game Type: {self.game_type}")

        if self.game_type == 'TicTacToe': #En este caso, al ser el TicTacToe, se inicializa el tablero con 3x3
            print("The first value corresponds to row and the second to the column --> (row, col)\n")
            self.board = [[' ' for _ in range(3)] for _ in range(3)]
            self.print_board_tictactoe() #Se printa el tablero de juego

    #Método que define el movimiento a realizar, en base al contexto
    def enterMove(self, ctx: BoardGameParser.MoveContext):
        if self.game_type == 'TicTacToe':
            self.handle_tictactoe_move(ctx)

    #Método para gestionar el movimiento a realizar cada iteración
    def handle_tictactoe_move(self, ctx:BoardGameParser.MoveContext):
        #Se lee el player correspondiente del fichero junto con sus coordenadas de movimiento
        player = ctx.player().getText()
        x = int(ctx.coordinate(0).getText())
        y = int(ctx.coordinate(1).getText())

        #Si no es movimiento válido, se indica al jugador
        if not self.is_valid_move(x,y):
            print("Invalid move. Try again.")
            return

        #Se definen los caracteres para cada jugador
        if player == 'player1':
            self.board[x][y] = 'X'
        elif player == 'player2':
            self.board[x][y] = 'O'

        #Se indica el movimiento realizaxo por cada uno de ellos
        print(f"{player} moves to ({x},{y})\n")
        self.print_board_tictactoe()

        #Comprobaciones para saber si ha ganado alguno de los jugadores o es un empate
        if self.check_winner('X'):
            print("Player 1 wins!")
        elif self.check_winner('0'):
            print("Player 2 wins!")
        elif self.is_board_full():
            print("It's a draw!")

    #Método para printar el tablero de juego
    def print_board_tictactoe(self):
        print("    0   1   2")
        print("  +---+---+---+")
        for row in range(3):
            print(f"{row} |", end="")
            for col in range(3):
                print(f" {self.board[row][col]} |", end="")
            print()
            print("  +---+---+---+")
        print()


    #Método que delimita las casillas donde puede insertar el jugador
    def is_valid_move(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == ' '

    #Se comprueba si el tablero está lleno para saber si es un empate
    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    #Método que comprueba si hay ganador
    def check_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):  # Comprueba filas
                return True
            if all(self.board[j][i] == player for j in range(3)):  # Comprueba columnas
                return True
        if all(self.board[i][i] == player for i in range(3)):  # Comprueba diagonal principal
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):  # Comprueba diagonal secundaria
            return True
        return False

def main(argv):
    #Se lee el fichero de entrada y se inicializan los objetos necesarios para el lexer y parser
    input_stream = FileStream(argv[1])
    lexer = BoardGameLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = BoardGameParser(stream)
    tree = parser.program()

    #Se inicializa el listener y el walker para recorrer el árbol
    listener = BoardGameInterpreter()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == '__main__':
    main(sys.argv)
