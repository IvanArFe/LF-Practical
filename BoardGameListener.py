# Generated from BoardGame.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BoardGameParser import BoardGameParser
else:
    from BoardGameParser import BoardGameParser

# This class defines a complete listener for a parse tree produced by BoardGameParser.
class BoardGameListener(ParseTreeListener):

    # Enter a parse tree produced by BoardGameParser#program.
    def enterProgram(self, ctx:BoardGameParser.ProgramContext):
        pass

    # Exit a parse tree produced by BoardGameParser#program.
    def exitProgram(self, ctx:BoardGameParser.ProgramContext):
        pass


    # Enter a parse tree produced by BoardGameParser#statement.
    def enterStatement(self, ctx:BoardGameParser.StatementContext):
        pass

    # Exit a parse tree produced by BoardGameParser#statement.
    def exitStatement(self, ctx:BoardGameParser.StatementContext):
        pass


    # Enter a parse tree produced by BoardGameParser#game.
    def enterGame(self, ctx:BoardGameParser.GameContext):
        pass

    # Exit a parse tree produced by BoardGameParser#game.
    def exitGame(self, ctx:BoardGameParser.GameContext):
        pass


    # Enter a parse tree produced by BoardGameParser#gameType.
    def enterGameType(self, ctx:BoardGameParser.GameTypeContext):
        pass

    # Exit a parse tree produced by BoardGameParser#gameType.
    def exitGameType(self, ctx:BoardGameParser.GameTypeContext):
        pass


    # Enter a parse tree produced by BoardGameParser#move.
    def enterMove(self, ctx:BoardGameParser.MoveContext):
        pass

    # Exit a parse tree produced by BoardGameParser#move.
    def exitMove(self, ctx:BoardGameParser.MoveContext):
        pass


    # Enter a parse tree produced by BoardGameParser#player.
    def enterPlayer(self, ctx:BoardGameParser.PlayerContext):
        pass

    # Exit a parse tree produced by BoardGameParser#player.
    def exitPlayer(self, ctx:BoardGameParser.PlayerContext):
        pass


    # Enter a parse tree produced by BoardGameParser#coordinate.
    def enterCoordinate(self, ctx:BoardGameParser.CoordinateContext):
        pass

    # Exit a parse tree produced by BoardGameParser#coordinate.
    def exitCoordinate(self, ctx:BoardGameParser.CoordinateContext):
        pass



del BoardGameParser