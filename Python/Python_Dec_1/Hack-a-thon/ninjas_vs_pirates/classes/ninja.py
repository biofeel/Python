import random

class Ninja:
    roster=[]
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.turn = 0
        self.__class__.roster.append(self)
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength + random.randrange(0,self.speed)
        return self
    
    @classmethod
    def meeting_of_ninjas(cls):
        for ninja in cls.roster:
            ninja.health += 20
            ninja.strength += 5

ninja1 = Ninja("ninja1")
ninja2 = Ninja("ninja2")

Ninja.meeting_of_ninjas()

ninja1.show_stats()
ninja2.show_stats()