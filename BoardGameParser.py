# Generated from BoardGame.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,3,1,22,8,1,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,
        1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,1,1,0,10,11,40,0,15,1,0,0,0,
        2,21,1,0,0,0,4,23,1,0,0,0,6,28,1,0,0,0,8,30,1,0,0,0,10,41,1,0,0,
        0,12,43,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,17,15,
        1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,22,3,4,2,0,20,22,3,8,4,0,21,
        19,1,0,0,0,21,20,1,0,0,0,22,3,1,0,0,0,23,24,5,1,0,0,24,25,5,2,0,
        0,25,26,3,6,3,0,26,27,5,3,0,0,27,5,1,0,0,0,28,29,5,4,0,0,29,7,1,
        0,0,0,30,31,5,5,0,0,31,32,5,2,0,0,32,33,3,10,5,0,33,34,5,6,0,0,34,
        35,5,7,0,0,35,36,3,12,6,0,36,37,5,8,0,0,37,38,3,12,6,0,38,39,5,9,
        0,0,39,40,5,3,0,0,40,9,1,0,0,0,41,42,7,0,0,0,42,11,1,0,0,0,43,44,
        5,12,0,0,44,13,1,0,0,0,2,17,21
    ]

class BoardGameParser ( Parser ):

    grammarFileName = "BoardGame.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'game'", "':'", "';'", "'TicTacToe'", 
                     "'move'", "'at'", "'('", "','", "')'", "'player1'", 
                     "'player2'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INT", "ID", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_game = 2
    RULE_gameType = 3
    RULE_move = 4
    RULE_player = 5
    RULE_coordinate = 6

    ruleNames =  [ "program", "statement", "game", "gameType", "move", "player", 
                   "coordinate" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    INT=12
    ID=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.StatementContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.StatementContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = BoardGameParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def game(self):
            return self.getTypedRuleContext(BoardGameParser.GameContext,0)


        def move(self):
            return self.getTypedRuleContext(BoardGameParser.MoveContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = BoardGameParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.game()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.move()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gameType(self):
            return self.getTypedRuleContext(BoardGameParser.GameTypeContext,0)


        def getRuleIndex(self):
            return BoardGameParser.RULE_game

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGame" ):
                listener.enterGame(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGame" ):
                listener.exitGame(self)




    def game(self):

        localctx = BoardGameParser.GameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_game)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(BoardGameParser.T__0)
            self.state = 24
            self.match(BoardGameParser.T__1)
            self.state = 25
            self.gameType()
            self.state = 26
            self.match(BoardGameParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GameTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BoardGameParser.RULE_gameType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGameType" ):
                listener.enterGameType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGameType" ):
                listener.exitGameType(self)




    def gameType(self):

        localctx = BoardGameParser.GameTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_gameType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(BoardGameParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def player(self):
            return self.getTypedRuleContext(BoardGameParser.PlayerContext,0)


        def coordinate(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BoardGameParser.CoordinateContext)
            else:
                return self.getTypedRuleContext(BoardGameParser.CoordinateContext,i)


        def getRuleIndex(self):
            return BoardGameParser.RULE_move

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMove" ):
                listener.enterMove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMove" ):
                listener.exitMove(self)




    def move(self):

        localctx = BoardGameParser.MoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_move)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(BoardGameParser.T__4)
            self.state = 31
            self.match(BoardGameParser.T__1)
            self.state = 32
            self.player()
            self.state = 33
            self.match(BoardGameParser.T__5)
            self.state = 34
            self.match(BoardGameParser.T__6)
            self.state = 35
            self.coordinate()
            self.state = 36
            self.match(BoardGameParser.T__7)
            self.state = 37
            self.coordinate()
            self.state = 38
            self.match(BoardGameParser.T__8)
            self.state = 39
            self.match(BoardGameParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlayerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BoardGameParser.RULE_player

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlayer" ):
                listener.enterPlayer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlayer" ):
                listener.exitPlayer(self)




    def player(self):

        localctx = BoardGameParser.PlayerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_player)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            _la = self._input.LA(1)
            if not(_la==10 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CoordinateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BoardGameParser.INT, 0)

        def getRuleIndex(self):
            return BoardGameParser.RULE_coordinate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCoordinate" ):
                listener.enterCoordinate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCoordinate" ):
                listener.exitCoordinate(self)




    def coordinate(self):

        localctx = BoardGameParser.CoordinateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_coordinate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(BoardGameParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





