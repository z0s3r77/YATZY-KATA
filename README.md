# Refactorización Yatzy

Este kata trata sobre refactorizar y desarrollar mediante TDD un programa propuesto en el libro [The Coding Dojo Handbook, a practical guide to creating a space where good programmers can become great programmers](https://leanpub.com/codingdojohandbook) de Emily Bache.

### Reglas a seguir en el Kata

Yatzy es un juego de dados. Cada jugador tira 5 dados de 6 caras. Pueden volver a tirar los dados hasta tres veces.

Supongamos que tiramos y sale:

  5,2,1,4,2
  
 Se pueden mantener los 2 (-,2,-,-,2) y volver a tirar el resto (5,-,1,4,-):
 
  2,2,6,3,2
  
 Se pueden mantener los 2 (2,2,-,-,2) y volver a tirar el resto (-,-,6,3,-):
 
  2,2,1,2,2
  
Una vez se está satisfecho con la tirada, se deben poner los dados en una categoria que se mencionan a continuación:

  - Ones, twos,threes,fours,fives,sixes
  - Chance
  - Yatzy
  - Score_pair,two_pair
  - Three_of_a_kind, four_of_a_kind
  - SmallStraight, largeStraight
  - FullHouse
  
Cada categoria, devuelve una serie de puntos que veremos a continuación.

La tarea del Kata consiste en poner una tirada en una categoria. __No se debe programar tiradas random__. El juego NO se juega dejando que la computadora elija el
categoría de puntuación más alta para una tirada dada.


## Categorías

### Chance:
El jugador anota la suma de todos los dados, sin importar lo que lea.
Por ejemplo:
  
- 1,1,3,3,6 colocado en "chance" puntúa 14 (1+1+3+3+6)
- 4,5,5,6,1 colocado en "chance" puntúa 21 (4+5+5+6+1)

### Yatzy:
Si todos los dados tienen el mismo número,
el jugador anota 50 puntos.
Por ejemplo:
  
- 1,1,1,1,1 colocado en "yatzy" puntúa 50
- 1,1,1,2,1 colocado en "yatzy" puntúa 0

### Ones, whos, threes, fours, fives, sixes:
El jugador anota la suma de los dados que lee uno,
dos, tres, cuatro, cinco o seis, respectivamente.
Por ejemplo:

- 1,1,2,4,4 colocados en "fours" puntúa 8 (4+4)
- 2,3,2,5,1 colocado en "twos" puntúa 4 (2+2)
- 3,3,3,4,5 colocados en "ones" puntuaciones 0

### Pair:
El jugador anota la suma de los dos dados iguales más altos.
Por ejemplo, cuando se coloca en "pair":
  
- 3,3,3,4,4 puntuaciones 8 (4+4)
- 1,1,6,2,6 puntuaciones 12 (6+6)
- 3,3,3,4,1 puntuaciones 6 (3+3)
- 3,3,3,3,1 puntuaciones 6 (3+3)

### Two pairs:
Si hay dos pares de dados con el mismo número, el
jugador anota la suma de estos dados.
Por ejemplo, cuando se coloca en "Two pairs":
  
- 1,1,2,3,3 puntuaciones 8 (1+1+3+3)
- 1,1,2,3,4 puntuaciones 0
- 1,1,2,2,2 puntuaciones 6 (1+1+2+2)

###Three of a kind:
Si hay tres dados con el mismo número, el jugador
anota la suma de estos dados.
Por ejemplo, cuando se coloca en "Three of a kind":
    
- 3,3,3,4,5 puntuaciones 9 (3+3+3)
- 3,3,4,5,6 puntuaciones 0
- 3,3,3,3,1 puntúa 9 (3+3+3)

### Four of a kind:
Si hay cuatro dados con el mismo número, el jugador
anota la suma de estos dados.
Por ejemplo, cuando se coloca en "Four of a kind":
  
- 2,2,2,2,5 puntúa 8 (2+2+2+2)
- 2,2,2,5,5 puntuaciones 0
- 2,2,2,2,2 puntúa 8 (2+2+2+2)

### Small straight:
Cuando se coloca en "Small straight", si los dados dicen

   1,2,3,4,5,
   
el jugador anota 15 (la suma de todos los dados).

### Large straight:
Cuando se coloca en "Large straight", si los dados dicen

   2,3,4,5,6,
   
el jugador anota 20 (la suma de todos los dados).

### Full house:
Si los dados son dos de una clase y tres de una clase, el
jugador anota la suma de todos los dados.
Por ejemplo, cuando se coloca en "Full house":
   
- 1,1,2,2,2 puntúa 8 (1+1+2+2+2)
- 2,2,3,3,4 puntuaciones 0
- 4,4,4,4,4 puntuaciones 0


