//Grammar
grammar BoardGame;

// Root Rule
program: statement+;

//Statements
statement: game | move;

//Game
game:'game' ':' gameType ';';

//Define Games
gameType: 'TicTacToe';

//Define Moves
move: 'move' ':' player 'at' '(' coordinate ',' coordinate ')' ';';

// Players
player: 'player1' | 'player2';

// Coordinates
coordinate: INT;

//Lexer rules
INT: [0-9]+;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
WS: [ \t\r\n]+ -> skip;
