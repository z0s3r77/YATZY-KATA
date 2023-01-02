import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)
    assert 6 == Yatzy.chance(1, 1, 1, 1, 2)

def test_ones():
    #Debe devolver la suma total de los 1
    assert 2 == Yatzy.ones(1,2,3,4,1)
    assert 4 == Yatzy.ones(1,1,1,1,5)

def test_twos():
    #Debe devolver la suma total de los 2
    assert 4 == Yatzy.twos(2,2,4,5,1)
    assert 6 == Yatzy.twos(2,2,2,1,4)

def test_threes():
    #Debe devolver la suma total de los 3
    assert 3 == Yatzy.threes(3,1,2,5,2)
    assert 9 == Yatzy.threes(3,2,3,1,3)



def test_yatzy():
    assert 50 == Yatzy.yatzy([1,1,1,1,1])
    assert 0 == Yatzy.yatzy([1,1,1,2,1])
    assert 0 == Yatzy.yatzy([2,4,1,5,3])

def test_fours():
    assert 4 == Yatzy.fours(2,4,1,5,5)
    assert 12 == Yatzy.fours(4,4,4,2,1)


def test_five():
    assert 5 == Yatzy.fives(5,2,4,2,1)
    assert 15 == Yatzy.fives(5,5,5,1,2)


def test_sixes():
    assert 12 == Yatzy.sixes(6,6,1,2,3)
    assert 18 == Yatzy.sixes(5,1,6,6,6)

# @pytest.fixture
# def inyector():
#     # Es el setup de unittest o de JUnit
#     tirada = Yatzy(1, 2, 3, 4, 5)
#     return tirada


# def test_fours(inyector):
#     # Es necesario un objeto ya creado
#     valorEsperado = 4
#     # No puedo testear con fixtures = inyeccion de dependencias
#     # los metodos estaticos como chance()
#     assert valorEsperado == inyector.fours()
