from enum import Enum, unique

#El decorador unique nos permite tener variables con valores unicos
@unique
class Pips(Enum):

    ONE = 1
    TWO = 2
    THREE = 3 
    FOUR = 4
    FIVE = 5
    SIX = 6

