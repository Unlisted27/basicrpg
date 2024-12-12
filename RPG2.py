#imports
from utils import generators
import random
#OBJECTS
class race():
    def __init__(self,name,strength_modifier,constitution_modifier,intelligence_modifier,agility_modifier):
        self.name = name
        self.strength_modifier = strength_modifier
        self.constitution_modifier = constitution_modifier
        self.intelligence_modifier = intelligence_modifier
        self.agility_modifier = agility_modifier
    def genrace(name):
            print("GENRACE COMING SOON")
class profession():
    def __init__(self,name):
        self.name = name
class item:
    def __init__(self,name,weight,description,code="pass",item_type = "item"):
        self.name = name
        self.weight = weight
        self.description = description
        self.code = code
        self.item_type = item_type
    class food():
        def __init__(self,name,weight,description,health,item_type = "food"):
            self.name = name
            self.weight = weight
            self.description = description
            self.health = health
            self.item_type = item_type
        def use(self,target):
            if target.health:
                target.health += self.health
    class weapon():
        def __init__(self,name,weight,description,damage,item_type = "weapon"):
            self.name = name
            self.weight = weight
            self.description = description
            self.damage = damage
            self.item_type = item_type
class map: #UNUSED
    def __init__(self,name):
        self.name = name
    class nation:
        def __init__(self,name,ruler):
            self.name = name
            self.ruler = ruler
    class land:
        def __init__(self,name,ruler):
            self.name = name
            self.ruler = ruler
    class citie:
        def __init__(self,city_name,city_ruler):
            self.city_name = city_name
            self.city_ruler = city_ruler
    class town:
        def __init__(self,town_name,town_ruler):
            self.town_name = town_name
            self.town_ruler = town_ruler
    def genmap():
        map(name = generators.genname())
class character():
    #def __init__(self,race = races.human,profession = professions.commoner,name = "DEFAULT",initiative = 0):
    def __init__(self,race,profession,name,initiative = 0,strength = 10,constitution = 10,intelligence = 10,agility = 10,armor_class = 4,health = 10):
        self.race = race
        self.profession = profession
        self.name = name
        self.initiative = initiative
        #stats
        self.strength = strength + self.race.strength_modifier
        self.constitution = constitution + self.race.constitution_modifier
        self.intelligence = intelligence + self.race.intelligence_modifier
        self.agility = agility + self.race.agility_modifier
        self.armor_class = armor_class
        self.health = health + self.race.constitution_modifier
        #other
        self.inventory = []
    def create_random(self):
        self.strength = random.randint(5,20) + self.race.strength_modifier
        self.constitution = random.randint(5,20) + self.race.constitution_modifier
        self.intelligence = random.randint(5,20) + self.race.intelligence_modifier
        self.agility = random.randint(5,20) + self.race.agility_modifier
        self.armor_class = random.randint(3,5) + self.race.agility_modifier
        self.health = random.randint(5,15) + self.race.constitution_modifier
    def attack(self,target):
        roll = random.randint(1,20)#roll for hit
        if roll > target.armor_class:
            print("Hit!")
            target.health -= 1
        else:
            print("Miss!")
    def printstats(self):
        print("|~~~~~~~~~~~~~~~~~~~")
        print("|Name: " + self.name)
        print("|Race: " + self.race.name)
        print("|Profession: " + self.profession.name)
        print("|==STATS==")
        print("|Strength: " + str(self.strength) + " (" + str(self.race.strength_modifier) + ")")
        print("|Constitution: " + str(self.constitution) + " (" + str(self.race.constitution_modifier) + ")")
        print("|Intelligence: " + str(self.intelligence) + " (" + str(self.race.intelligence_modifier) + ")")
        print("|Agility: " + str(self.agility) + " (" + str(self.race.agility_modifier) + ")")
        print("|Armor class: " + str(self.armor_class))
        print("|HEALTH: "+str(self.health))
        print("|~~~~~~~~~~~~~~~~~~~")
        print()

    def printinvent(self):
        print("|INVENTORY|")
        print("|~~~~~~~~~~~~~~~~~~~")
        for item in self.inventory:
            print("|"+item.name) 
        print("|~~~~~~~~~~~~~~~~~~~")
        print()
#lists
class races():
    human = race("human",0,0,0,0)
    goblin = race("goblin",-1,-1,-1,0)
class professions():
    commoner=profession("commoner")
class items():

    class foods():
        bread = item.food("bread",0.2,"It's just bread",1)
class characters():
    player = character(races.human,professions.commoner,generators.genname())
    player.create_random()
    goblin = character(races.goblin,professions.commoner,generators.genname())
    goblin.create_random()

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
characters.player.create_random()
characters.player.printstats()
characters.player.printinvent()
print("PLS WORK")