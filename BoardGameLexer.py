# Generated from BoardGame.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,14,97,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,7,1,7,
        1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,11,4,11,80,8,11,11,11,12,11,81,1,12,1,12,5,12,86,
        8,12,10,12,12,12,89,9,12,1,13,4,13,92,8,13,11,13,12,13,93,1,13,1,
        13,0,0,14,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,25,13,27,14,1,0,4,1,0,48,57,3,0,65,90,95,95,97,122,4,0,48,57,
        65,90,95,95,97,122,3,0,9,10,13,13,32,32,99,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,
        0,25,1,0,0,0,0,27,1,0,0,0,1,29,1,0,0,0,3,34,1,0,0,0,5,36,1,0,0,0,
        7,38,1,0,0,0,9,48,1,0,0,0,11,53,1,0,0,0,13,56,1,0,0,0,15,58,1,0,
        0,0,17,60,1,0,0,0,19,62,1,0,0,0,21,70,1,0,0,0,23,79,1,0,0,0,25,83,
        1,0,0,0,27,91,1,0,0,0,29,30,5,103,0,0,30,31,5,97,0,0,31,32,5,109,
        0,0,32,33,5,101,0,0,33,2,1,0,0,0,34,35,5,58,0,0,35,4,1,0,0,0,36,
        37,5,59,0,0,37,6,1,0,0,0,38,39,5,84,0,0,39,40,5,105,0,0,40,41,5,
        99,0,0,41,42,5,84,0,0,42,43,5,97,0,0,43,44,5,99,0,0,44,45,5,84,0,
        0,45,46,5,111,0,0,46,47,5,101,0,0,47,8,1,0,0,0,48,49,5,109,0,0,49,
        50,5,111,0,0,50,51,5,118,0,0,51,52,5,101,0,0,52,10,1,0,0,0,53,54,
        5,97,0,0,54,55,5,116,0,0,55,12,1,0,0,0,56,57,5,40,0,0,57,14,1,0,
        0,0,58,59,5,44,0,0,59,16,1,0,0,0,60,61,5,41,0,0,61,18,1,0,0,0,62,
        63,5,112,0,0,63,64,5,108,0,0,64,65,5,97,0,0,65,66,5,121,0,0,66,67,
        5,101,0,0,67,68,5,114,0,0,68,69,5,49,0,0,69,20,1,0,0,0,70,71,5,112,
        0,0,71,72,5,108,0,0,72,73,5,97,0,0,73,74,5,121,0,0,74,75,5,101,0,
        0,75,76,5,114,0,0,76,77,5,50,0,0,77,22,1,0,0,0,78,80,7,0,0,0,79,
        78,1,0,0,0,80,81,1,0,0,0,81,79,1,0,0,0,81,82,1,0,0,0,82,24,1,0,0,
        0,83,87,7,1,0,0,84,86,7,2,0,0,85,84,1,0,0,0,86,89,1,0,0,0,87,85,
        1,0,0,0,87,88,1,0,0,0,88,26,1,0,0,0,89,87,1,0,0,0,90,92,7,3,0,0,
        91,90,1,0,0,0,92,93,1,0,0,0,93,91,1,0,0,0,93,94,1,0,0,0,94,95,1,
        0,0,0,95,96,6,13,0,0,96,28,1,0,0,0,4,0,81,87,93,1,6,0,0
    ]

class BoardGameLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    INT = 12
    ID = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'game'", "':'", "';'", "'TicTacToe'", "'move'", "'at'", "'('", 
            "','", "')'", "'player1'", "'player2'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "ID", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "INT", "ID", "WS" ]

    grammarFileName = "BoardGame.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

