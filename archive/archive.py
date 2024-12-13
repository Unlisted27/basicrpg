#This is where old code goes to die
#Lol for real tho, I put everything that I made and worked at somepoint but dont wanna put in the final project, here. This could be for a number of reasons.
#BE WARNED! Some code here has the possibility to just not work, infact it is likely to not work because it's old or just never worked so I trashed it.
import random
#Put this here cause it didn't fit with how I wanted to structure my project. Also I think there are some things that just dont work, cant rly remember tho.
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