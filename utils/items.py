#WHoa! Look at you! Your going into the code WITHIN THE COD!!! NO WAY! Congrats on getting here if you're a noob, I wouldnt have understood what this was like 2 days ago TBH
#If you want to take the extra leap to make your own item type, make sure that has at minimum the following properties:
#self,name,weight,description,is_pickable,item_type

class item():
    def __init__(self,name:str,weight:int,description:str,is_pickable=True,item_type = "item",code="pass"):
        self.name = name
        self.weight = weight
        self.description = description
        self.code = code
        self.item_type = item_type
        self.is_pickable = is_pickable
class food():
    def __init__(self,name:str,weight:int,description:str,health,is_pickable=True,item_type = "food"):
        self.name = name
        self.weight = weight
        self.description = description
        self.health = health
        self.item_type = item_type
        self.is_pickable = is_pickable

    def use(self,target):
        if target.health:
            target.health += self.health
class weapon():
    def __init__(self,name:str,weight:int,description:str,damage,is_pickable=True,item_type = "weapon"):
        self.name = name
        self.weight = weight
        self.description = description
        self.damage = damage
        self.item_type = item_type
        self.is_pickable = is_pickable