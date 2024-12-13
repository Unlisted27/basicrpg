#imports
from utils import components #Imports the main juicy of this thing. Components are all of the custom objects that I've made
from utils import generators #Generators. This is a bunch of generator functions for different things. They will be pretty self descriptive
from starter_pack import starter_pack
import random
#OBJECTS

#lists

#other
class combat: #UNUSED
    def __init__(self,fighter_1,fighter_2):
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.round = 0
    def initiative_roll(self):
        initiative_1 = random.randint(0,10) + self.fighter_1.initiative
        initiative_2 = random.randint(0,10) + self.fighter_2.initiative
        print("-ROLLING FOR TURN-")
        print(self.fighter_1.name + ": " + str(initiative_1))
        print(self.fighter_2.name + ": " + str(initiative_2))
        #Arrange by initiative
        if initiative_1 < initiative_2:
            placeholder = self.fighter_1
            self.fighter_1 = self.fighter_2
            self.fighter_2 = placeholder
    def turn(self): #Not used
        self.round += 1
        print("~~~~~~~~~~~~")
        print("|ROUND: "+ str(self.round))
        print("~~~~~~~~~~~~")
        print("-"+self.fighter_1.name+" attacks!-")
        attacks_1 = self.fighter_1.attacks()
        attacks_1.punch(self.fighter_2)
        print(self.fighter_1.name + "HEALTH: "+str(self.fighter_1.health))
        print(self.fighter_2.name + "HEALTH: "+str(self.fighter_2.health))
    def fight_to_death(self):
        while self.fighter_1.health > 0 and self.fighter_2.health > 0:
            self.round += 1
            print("~~~~~~~~~~~~")
            print("|ROUND: "+ str(self.round))
            print("~~~~~~~~~~~~")
            print("-"+self.fighter_1.name+" attacks!-")
            attacks_1 = self.fighter_1.attacks()
            attacks_1.punch(self.fighter_2)
            print(self.fighter_1.name + "HEALTH: "+str(self.fighter_1.health))
            print(self.fighter_2.name + "HEALTH: "+str(self.fighter_2.health))
            placeholder = self.fighter_1
            self.fighter_1 = self.fighter_2
            self.fighter_2 = placeholder
            input("[PRESS ENTER TO PROGRESS]")

#COMMANDS Ok im too fuckin tired to deal with this. Just need error handling mainly
#SCRE THIS SHIT. IM REWORKING THIS GAMES ENTIRE CMDS THINGY AND INPUT SYSTEM
#print(player.name) 
print("welcome, player!")
starter_pack.characters.player.create_random()
starter_pack.characters.player.printstats()
starter_pack.characters.player.aquire(starter_pack.items.foods.bread)
starter_pack.characters.player.printinvent()