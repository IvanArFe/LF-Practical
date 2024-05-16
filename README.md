# LF-Practical

# TicTacToe Interpreter

## Visió general del projecte
El nostre projecte consisteix en el desenvolupament d'un intèrpret per al joc del tres en ratlla utilitzant el llenguatge TicTacToe. Aquest intèrpret permetrà als usuaris escriure seqüències de comandes que representin partides del joc i executar-les per simular el seu desenvolupament i determinar el resultat final.

### Equip
- *Membres*: Ivan Arenal Fernández, Pol Pujol Santaella, Ivet Pallàs Padró

### Llenguatge i Intèrpret
- *Llenguatge*: TicTacToe
- *Intèrpret*: Python
- *Eines*: ANTLR4 (ANTLR v4)

### Solució
La solució consistirà en un intèrpret implementat en Python que serà capaç de llegir seqüències de comandes en el llenguatge TicTacToe i simular el desenvolupament de partides del joc del tres en ratlla. Això inclourà la detecció de guanyadors, la gestió del tauler de joc i la visualització del seu estat durant la partida.

## Contribució de cada membre
Durant el desenvolupament del projecte, no ens hem repartit les tàsques, sinó que ens hem anat ajuntant per fer el treball de manera conjunta els tres. Hem optat per organitzar-nos d'una manera en la qual els tres hem estat involucrats en totes les etapes del projecte per tal d'aprendre i contribuir de manera equitativa a totes les parts del treball.

Hem mantingut una comunicació, compartint idees, resolent problemes i prenent decisions de manera conjunta. Això ens ha permès aprendre i entendre els diversos aspectes del treball, incloent-hi la definició del llenguatge, la implementació del parser, la lògica del joc, la interfície d'usuari, la integració del sistema i les proves.


## Com instalem i executem
1. *Clone Repository*: Executar git clone https://github.com/IvanArFe/LF-Practical en el terminal per clonar el repositori a la màquina.
2. *Invocar Analitzador ANTLR*: antlr4 BoardGame.g4
3. *Compilador Java*: javac BoardGame*.java 
4. *Generate Parser*: antlr4 -Dlanguage=Python3 BoardGame.g4
5. *ANTLR4 para Python*: pip install antlr4-python3-runtime
6. *Run Interpreter*: Executar `python3 board_game_interpreter.py <fitxer JOC>`

## Com utilitzem l'eina
Per utilitzar l'intèrpret, seguim aquests passos:

1. Crea un fitxer de text amb la seqüència de comandes del joc, seguint la sintaxi definida en el llenguatge TicTacToe.
2. Executa l'intèrpret proporcionant el nom del fitxer com a argument.
3. Observar la sortida de l'intèrpret, que mostrarà el tipus de joc i els moviments realitzats pels jugadors i el resultat final.

*Exemple d'ús*:
Exemple d'una partida normal (fitxer GAME1):
game: TicTacToe;
move: player1 at (0,0);
move: player2 at (1,1);
move: player1 at (0,1);
move: player2 at (2,2);
move: player1 at (0,2);


python3 board_game_interpreter.py GAME1.txt

Sortida:

Game Type: TicTacToe
 | | 
-----
 | | 
-----
 | | 
-----

player1 moves to (0,0)
X| | 
-----
 | | 
-----
 | | 
-----

player2 moves to (1,1)
X| | 
-----
 |O| 
-----
 | | 
-----

player1 moves to (0,1)
X|X| 
-----
 |O| 
-----
 | | 
-----

player2 moves to (2,2)
X|X| 
-----
 |O| 
-----
 | |O
-----

player1 moves to (0,2)
X|X|X
-----
 |O| 
-----
 | |O
-----

Player 1 wins!
