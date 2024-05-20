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
La solució consistirà en un intèrpret implementat en Python que serà capaç de llegir seqüències de comandes en el llenguatge TicTacToe. Aquest, simularà el desenvolupament de partides del joc del tres en ratlla. Això inclourà la detecció de guanyadors, la gestió del tauler de joc i la visualització del seu estat durant la partida. També es té en compte la gestió de moviments invàlids per part d'algún dels jugadors.

## Contribució de cada membre
Durant el desenvolupament del projecte, no ens hem repartit les tàsques, sinó que ens hem anat ajuntant per fer el treball de manera conjunta els tres. Hem optat per organitzar-nos d'una manera en la qual els tres hem estat involucrats en totes les etapes del projecte per tal d'aprendre i contribuir de manera equitativa a totes les parts del treball.

Hem mantingut una comunicació, compartint idees, resolent problemes i prenent decisions de manera conjunta. Això ens ha permès aprendre i entendre els diversos aspectes del treball, incloent-hi la definició del llenguatge, la implementació del parser, la lògica del joc, la interfície d'usuari, la integració del sistema i les proves.

Considerem que l'aprenentatge adquirit és prou bo i, que el resultat obtingut en la pràctica implementa bastant bé els coneixements vistos a l'assignatura sobre l'ús de l'eina i les gramàtiques.


## Com instalem i executem
1. *Clone Repository*: Executar git clone https://github.com/IvanArFe/LF-Practical en el terminal per clonar el repositori a la màquina.
2. *Instal·lar l'eina ANTLR4*: Es poden seguir els passos del següent repositoru de GitHub: https://github.com/antlr/antlr4.git 
3. *Invocar Analitzador ANTLR sobre el fitxer de la gramàtica*: antlr4 BoardGame.g4
4. *Compilador Java sobre els arxius generats*: javac BoardGame*.java
5. *Generate Parser*: antlr4 -Dlanguage=Python3 BoardGame.g4
7. *ANTLR4 per poder executar en Python*: pip install antlr4-python3-runtime
8. *En cas de que no funciones cal crear entorn, Si funciona passar a pas 13*
9. Crear entorn virtual python:
10. python3 -m venv LFenv
11. source ./LFenv/bin/activate
12. pip install antlr4-python3-runtime
13. *Run Interpreter*: Executar `python3 board_game_interpreter.py <fitxer JOC>`

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

## Comanda emprada
python3 your_game.py board_file.txt

Example: 
python3 board_game_interpreter.py GAME1.txt
