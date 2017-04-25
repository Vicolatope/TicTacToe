# Test MyTraffic

## Objectif

Le but est de créer un jeu de TicTacToe sur une grille de 3x3 en **python3**.
La grille doit être indéxée à partir de **0**.

Exemple:
    0   1   2
  -------------
0 | X | O |   |
  -------------
1 | X |   |   |
  -------------
2 | O |   | X |
  -------------


## Input

Exemple1:
`
X x1 y1
O x2 y2
O x3 y3
`

Exemple2:
`
X x1 y1
O x2 y2
`

X et O correspondent aux joueurs.
xi et yi correspondent à la position à laquelle doit être mis le point.


## Output

Si l'input n'est pas valide, imprimer 'invalid input'

Si l'input est valide, imprimer:
- si la partie n'est pas finie: 'game not over'
- si match nul: 'no winner'
- si un des joueurs gagne: 'player X/O won'

Pour les exemples donnés:
- exemple1 imprimera 'invalid input'
- exemple2 imprimera 'game not over'


## Règles

- le joueur X commence
- les joueurs doivent alterner (un même joueur ne peut pas jouer deux fois d'affilée)
- une position ne peut pas être prise plusieurs fois
- un joueur gagne quand il possède une des verticales, horizontales ou diagonales

ressource: https://fr.wikipedia.org/wiki/Tic-tac-toe


## Fonctionnement

Le jeu doit pouvoir se lancer avec la commande suivante:
`python tictactoe.py inputfile`

Avec inputfile le chemin vers le fichier d'input.


## BONUS (non obligatoire):

- imprimer l'état de la grille à chaque étape
- reformater le code pour fonctionner avec des grilles de toute taille
