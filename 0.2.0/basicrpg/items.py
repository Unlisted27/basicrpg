#Whoa! Look at you! Your going into the code WITHIN THE CODE!!! NO WAY! Congrats on getting here if you're a noob, I wouldnt have understood what this was like 2 days ago TBH
#If you want to take the extra leap to make your own item type, make sure that has at minimum the following properties:
#self,name,weight,description,is_pickable,item_type

#FUTURE PLAN FOR ALL ITEMS! All items will have a use() function. This will simply be what the item does. Example: food will contain code to heal the character. Character will be able to call the use function of any item.
#On this: ALL INVENTORY CHECKING AND HANDLING WILL BE HANDLED BY THE CHARACTER OBJECT, example: an item use function wil NOT contain code to remove it from a character inventory

import basicrpg.basics as basics

class item():
    class value():
        def __init__(self,thing,amount):
            self.amount = amount
            self.thing = thing
    def __init__(self,name:str,weight:int,description:str,worth:tuple=None,is_pickable=True,item_type = "item"):
        """value:(thing:basicrpg.item,amount:int)"""
        self.name = name
        self.weight = weight
        self.description = description
        if worth:
            self.value(worth[0],worth[1])
        self.item_type = item_type
        self.is_pickable = is_pickable
        print(self.value.thing.name + self.value.amount)
class food():
    def __init__(self,name:str,weight:int,description:str,health:int,is_pickable=True,item_type = "food"):
        self.name = name
        self.weight = weight
        self.description = description
        self.health = health
        self.item_type = item_type
        self.is_pickable = is_pickable

    def use(self,target):
        if hasattr(target,"health"):
            target.health = min(target.health + self.health,target.max_health) #Increase the target's health by the food's health stat, but not exceeding the target's max health.
        else:
            raise AttributeError("Expected target to have attribute 'health'")       
class weapon():
    def __init__(self,name:str,weight:int,description:str,attack_dice:tuple[int,int],base_damage:int,is_pickable=True,item_type = "weapon"):
        """attack_dice: tuple(dice_amount,dice_value) Ex: attack_dice=(2,6) would be 2d6, i.e rolling two, six sided dice"""
        self.name = name #The name of the weapon (Ex: Short sword)(Ex: the Sword of King Arthur)
        self.weight = weight #The weight of the weapon in pounds
        self.description = description #A general description of the weapon, can be anything.
        self.attack_dice = attack_dice #The number and value of 'dice' that the program will 'roll'. Ex: attack_dice=(2,6) would be 2d6, i.e rolling two, six sided dice"""
        self.base_damage = base_damage #The base damage of the weapon on hit. This is not effected by the attack roll
        self.item_type = item_type #The item type. It is reccomended you keep this as 'weapon' because certain parts of the code (such as attacks) may return a type error if the item type is not what it was expecting.
        self.is_pickable = is_pickable #Whether the item is able to be picked up by a character
    def attack_role(self): #We keep this as a function here so that we can add universal things such as 
        damage = self.base_damage + basics.roll(self.attack_dice[0],self.attack_dice[1])
        return (damage)
    
    def use(self,target): #Standard item use function. This one just displays a nice message
        print(f"You examin {self.name}, it gleams with power")