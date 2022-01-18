import random

class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
        self.turn = 0

    def show_stats( self ):
        return(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n") 

    def attack ( self , ninja ):
        ninja.health -= random.randrange(0,self.strength)
        return self

class Captain(Pirate):
    def __init__(self, name):
        super().__init__(name)
        self.drunk = True 
    def show_stats(self):
        return(f"{super().show_stats()}Drunk: {self.drunk}\n")

    def attack(self, opponent ):
        super().attack(opponent)
        if self.drunk:
            opponent.health -= 15

captain_seadog = Captain("captain_seadog")