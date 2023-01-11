import pytest
from src.yatzy import Yatzy

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



def test_score_pair():
    assert 8 == Yatzy.score_pair(3,3,3,4,4)
    assert 12 == Yatzy.score_pair(1,1,6,2,6)
    assert 6 == Yatzy.score_pair(3,3,3,4,1)
    assert 6 == Yatzy.score_pair(3,3,3,3,1)
    assert 0 == Yatzy.score_pair(1,2,3,4,5)

def test_two_pair():
    assert 8 == Yatzy.two_pair(1,1,2,3,3)
    assert 0 == Yatzy.two_pair(1,1,2,3,4)
    assert 6 == Yatzy.two_pair(1,1,2,2,2)
    assert 6 == Yatzy.two_pair(1,1,2,2,3)

def test_three_of_a_kind():
    assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
    assert 0 == Yatzy.three_of_a_kind(3,3,4,5,6)
    assert 9 == Yatzy.three_of_a_kind(3,3,3,3,1)


def test_four_of_a_kind():
    assert 8 == Yatzy.four_of_a_kind(2,2,2,2,5)
    assert 0 == Yatzy.four_of_a_kind(2,2,2,5,5)
    assert 8 == Yatzy.four_of_a_kind(2,2,2,2,2)


def test_smallSttraight():
    assert 15 == Yatzy.smallStraight(1,2,3,4,5)
    assert 0 == Yatzy.smallStraight(3,2,1,4,5)


def test_largeStraight():
    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(2,3,5,1,2)


def test_fullHouse():
    assert 8 == Yatzy.fullHouse(1,1,2,2,2)
    assert 0 == Yatzy.fullHouse(2,2,3,3,4)
    assert 0 == Yatzy.fullHouse(4,4,4,4,4)

