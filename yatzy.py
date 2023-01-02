class Yatzy:
    #Se ha optado por hacer todos los metodos estaticos

    #Suma el total de todos los dados
    @staticmethod
    def chance(* dice):
        return sum(dice)


    #Devulve 50 puntos si todos los dados son iguales
    @staticmethod
    def yatzy(dice):
        
        unique = dice[0]

        for die in dice:
            if die != unique:
                return 0

        return 50
    
    
    #Devuelve la suma de todos los 1
    @staticmethod
    def ones(* dices):
        sum = 0
        for diceValue in dices:
            if diceValue == 1:
                sum += diceValue
        return sum

    #Devuelve la suma de todos los 2
    @staticmethod
    def twos(* dices):
        sum = 0
        for diceValue in dices:
            if diceValue == 2:
                sum += diceValue
        return sum

    #Devuelve la suma de todos los 3
    @staticmethod
    def threes(* dices):
        sum = 0
        for diceValue in dices:
            if diceValue == 3:
                sum += diceValue
        return sum
    

    #Devuelve la suma de todos los 4
    @staticmethod
    def fours(* dices):
        sum = 0
        for diceValue in dices:
            if diceValue == 4:
                sum += diceValue
        return sum
    
    #Devuelve la suma de todos los 5
    @staticmethod
    def fives(* dices):
        sum = 0
        for diceValue in dices:
            if diceValue == 5:
                sum += diceValue
        return sum
    
   #Devuelve la suma de todos los 6
    @staticmethod
    def sixes(* dices):
        sum = 0
        for diceValue in dices:
            if diceValue == 6:
                sum += diceValue
        return sum
    


    #Devuelve la suma del par mayor en los dados
    @staticmethod
    def score_pair( * dices):

        pairs = []

        for i in dices:
            if dices.count(i) > 1:
                pairs.append(i)

        if not pairs:
            return 0

        else:
            pairs.sort()
            die = pairs.pop() * 2
            return die
        



    #Se suma el valor de dos parejas
    @staticmethod
    def two_pair( * dices):
        
        #Se cuenta cuantos dados hay de cada tipo
        counts = [0] * 6
        for die in dices:
            counts[die - 1] += 1
        

        pairsOfNumbers = 0 
        repeatingNumber = 0

        #Se encuentran las parejas y el numero de la pareja 
        #Es decir de 3,3 y sacamos el 3
        for i in range(6):
            if (counts[6-i-1] >= 2):
                pairsOfNumbers = pairsOfNumbers+1
                repeatingNumber += (6-i)
                    
        
        #Si el numero total de parejas es igual a dos
        #Se multiplica por dos ese numero de parejas
        
        if (pairsOfNumbers == 2):
            return repeatingNumber * 2
        else:
            return 0



    #Se devuelve la suma de tres dados repetidos
    @staticmethod
    def three_of_a_kind( * dices):

        for die in dices:
            if dices.count(die) >= 3: 
                return die * 3
        return 0
        


    #Se devuelve la suma de cuatro dados repetidos
    @staticmethod
    def four_of_a_kind( * dices ):
        for die in dices:
            if dices.count(die) >= 4: 
                return die * 4
        return 0
    

    

# El resultado de los dados debe serguir el orden 1,2,3,4,5
    @staticmethod
    def smallStraight(*dices):

        for i in range(5):
            if dices[i] != i + 1:
                return 0

        return 15


# El resultado de los dados debe serguir el orden 2,3,4,5,6
    @staticmethod
    def largeStraight(*dices):
        for i in range(5):
            if dices[i] != i + 2:
                return 0

        return 20
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0


tirada = Yatzy.smallStraight(1,2,3,4,5)
print(tirada)