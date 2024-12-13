#Whoa! Look at you! Your going into the code WITHIN THE COD!!! NO WAY! Congrats on getting here if you're a noob, I wouldnt have understood what this was like 2 days ago TBH
#If you want to take the extra leap to make your own item type, make sure that has at minimum the following properties:
#self,name,weight,description,is_pickable,item_type

#FUTURE PLAN FOR ALL ITEMS! All items will have a use() function. This will simply be what the item does. Example: food will contain code to heal the character. Character will be able to call the use function of any item.
#On this: ALL INVENTORY CHECKING AND HANDLING WILL BE HANDLED BY THE CHARACTER OBJECT
class item():
    def __init__(self,name:str,weight:int,description:str,is_pickable=True,item_type = "item",code="pass"):
        self.name = name
        self.weight = weight
        self.description = description
        self.code = code
        self.item_type = item_type
        self.is_pickable = is_pickable
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
    def __init__(self,name:str,weight:int,description:str,attack_dice:tuple[int,int],is_pickable=True,item_type = "weapon"):
        """attack_dice: tuple(dice_amount,dice_value) Ex: (2,6) = 2d6, i.e rolling two, six sided dice"""
        self.name = name
        self.weight = weight
        self.description = description
        self.attack_dice = attack_dice
        self.item_type = item_type
        self.is_pickable = is_pickable