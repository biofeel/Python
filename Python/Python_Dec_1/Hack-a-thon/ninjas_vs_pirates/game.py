from classes.ninja import Ninja
from classes.pirate import Pirate, Captain

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

captian_seadog = Captain("captian_seadog")

class game:
    def __init__(self, ninja:object, pirate:object):
        self.ninja = ninja
        self.pirate = pirate
        self.is_running = False
        self.turn = 0

    def battle(self):
        self.is_running=True
        while self.is_running:
            if self.ninja.health > 0 and self.pirate.health > 0:
                if self.turn %2 == 0:
                    self.ninja.attack(self.pirate)
                else:
                    self.pirate.attack(self.ninja)
                self.turn +=1
            else:
                print(self.ninja.show_stats())
                print(self.pirate.show_stats())
                self.is_running = False
                return self

new_game = game(captian_seadog, jack_sparrow)
new_game.battle()


# michelangelo.attack(jack_sparrow)
# jack_sparrow.show_stats()

# jack_sparrow.attack(jack_sparrow)
# michelangelo.show_stats()