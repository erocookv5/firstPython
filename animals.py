# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Creare la classe Animale con attributi:
    a) mammifero (un booleano)
    b) numero di zampe (2, 4, 6, 8)
    c) domestico (un booleano)

derivare una classe Cagnolino con aggiunta di:
    d) nome
    e) vaccinazione (booleano)
    f) nome padrone

generare una lista di 7 animali a caso con padroni a caso presi da una lista come:
    padroni = ["Gigi". "Toni", "Nino"]
    
ottenere il numero complessivo delle zampe nella lista
ottenere il numero di padroni <<differenti>>
"""

import random

owners = ("Lino", "Gino", "Tino", "Pino") #tuple
legsRange = (2, 4, 6, 8) #tuple

class Animal:
    numberLegs = 0
    def __init__(self, isPet = True, isMammal = True, legs = 4): # constructor with default values
        self.isPet = isPet
        self.isMammal = isMammal
        self.legs = legs
        self.owner = owners[random.randint(0, 3)]
        Animal.numberLegs = Animal.numberLegs + self.legs
    def __str__(self): 
        print("is it a Pet?: {}; is it a Mammal?: {}; number of legs: {}; owner: {}".format(self.isPet, self.isMammal, self.legs, self.owner))
    def printNumberLegs(self):
        print("Total number of legs: {}".format(Animal.numberLegs))
        

class Dog(Animal):
    def __init__(self, name = "Thesaurus", isVaccinated = True): # constructor with default values
        super().__init__() # parent constructor is inherited and called with its own default values
        self.name = name
        self.isVaccinated = isVaccinated 
    def __str__(self):
        print("is it a Pet?: {}; is it a Mammal?: {}; number of legs: {}; owner: {}; name: {}; isVaccinated: {}".format(self.isPet, self.isMammal, self.legs, self.owner, self.name, self.isVaccinated))

# creating animal instances and dog instances 
godzilla = Animal(False, False, legsRange[0])
godzilla.__str__()
kong = Animal(False, True)
kong.__str__()
tarantula = Animal(False, False, legsRange[3])
tarantula.__str__()
balto = Dog("Balto")
balto.__str__()
pluto = Dog("Pluto")
pluto.__str__()
rex = Dog("Rex")
rex.__str__()
lassie = Dog("Lassie", False)
lassie.__str__()
lassie.printNumberLegs()
    
animals = (godzilla, kong, tarantula, balto, pluto, rex, lassie)
uniqueOwners = []
for ow in owners:
    count = 0
    for a in animals:
        if a.owner == ow:
            count = count + 1
    if count == 1:
        uniqueOwners.append(ow)
print(uniqueOwners)
            
            
    















