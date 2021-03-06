"""
Create the following classes:
1. Pokemon: that has attributes of name, power (100 as default value). methods attack()
2. Electric: inherits from Pokemon
    - attack(): if attack Electric -> no change in power
                if attack Fire -> Electric increases power by 1
3. Fire: inherits from Pokemon
    - attack(): if attack Fire -> no change in power
                if attack Electric -> Fire decrease power by 1
4. test program that initialise 1 Pikachu (of type Electric), 1 charmander (of type Fire)
    - randomly generate 10 attacks from from any of the character.
    - display the final power.
"""
class Pokemon:
    def __init__(self, name="", power = 100):
        self.name = name
        self.power = power

    def __str__(self):
        return "I am {} power {}".format(self.name, self.power)

    def attack(self, other):
        return self.__str__()

x = Pokemon(name="x")
y = Pokemon(power="y")
x.attack(y)

class Electric(Pokemon):

    def attack(self, other):
        if isinstance(other, Fire):
            self.power += 1
        return self.__str__()

class Fire(Pokemon):

    def attack(self, other):
        if isinstance(other, Electric):
            self.power -= 1
        return self.__str__()

import random


characters = []
Pikachu = Electric("Pikachu")
Charmander = Fire("Charmander")
characters.append(Pikachu)
characters.append(Charmander)

for i in range(10):
    rand = random.randrange(0, 2)
    if rand == 0:
        print(characters[0].attack(characters[1]))
    else:
        print(characters[1].attack(characters[0]))



