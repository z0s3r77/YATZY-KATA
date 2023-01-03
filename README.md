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

### Categorias
