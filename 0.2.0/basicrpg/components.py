import random
from basicrpg.errors import itemNotFoundError
from basicrpg import items
#Name parts, just 3 massive lists of name parts that can be randomly put together
class name_parts():
    name_start_parts = [
    'Ada', 'Adel', 'Adri', 'Agn', 'Alf', 'Ale', 'Ali', 'Alma', 'Alo', 'Alv', 'Ama', 'Amb', 'Ana', 'And', 'Ang', 'Ann', 
    'Ans', 'Ant', 'Arn', 'Art', 'Aug', 'Aur', 'Bar', 'Bel', 'Ben', 'Ber', 'Bert', 'Bess', 'Bla', 'Blan', 'Bor', 'Bry', 
    'Cal', 'Cam', 'Car', 'Carl', 'Cas', 'Cat', 'Cha', 'Che', 'Chr', 'Clar', 'Cla', 'Cle', 'Clif', 'Cly', 'Con', 'Cor', 
    'Cyr', 'Dan', 'Dar', 'Dav', 'Deb', 'Del', 'Den', 'Dia', 'Dol', 'Dom', 'Dor', 'Dot', 'Edg', 'Edm', 'Edn', 'Edu', 
    'Edw', 'Ela', 'Ele', 'Eli', 'Eliz', 'Ell', 'Emi', 'Emm', 'Eph', 'Est', 'Ethel', 'Eug', 'Eva', 'Eve', 'Evi', 'Flo', 
    'Flora', 'Fran', 'Fre', 'Fred', 'Gab', 'Geo', 'Ger', 'Gil', 'Glad', 'Gor', 'Gra', 'Gre', 'Gus', 'Gwe', 'Har', 'Hen', 
    'Her', 'Hes', 'Hor', 'How', 'Hub', 'Hugh', 'Ina', 'Ire', 'Isa', 'Iva', 'Ivy', 'Jac', 'Jam', 'Jan', 'Jas', 'Jen', 
    'Jes', 'Jim', 'Joh', 'Jon', 'Jos', 'Jud', 'Jul', 'Jus', 'Kat', 'Ken', 'Kev', 'Kim', 'Lan', 'Lar', 'Leo', 'Les', 'Lil', 
    'Lin', 'Liz', 'Lou', 'Luc', 'Lud', 'Lut', 'Lyd', 'Lyn', 'Mar', 'Marv', 'Mat', 'Maud', 'Max', 'Meg', 'Mel', 'Mic', 
    'Mil', 'Min', 'Mit', 'Mor', 'Myr', 'Nan', 'Nel', 'Nell', 'Nev', 'Nia', 'Nor', 'Norv', 'Oli', 'Oma', 'Oph', 'Ora', 
    'Osc', 'Ott', 'Pat', 'Paul', 'Peg', 'Pet', 'Phil', 'Pru', 'Quin', 'Rad', 'Ray', 'Reb', 'Reg', 'Ren', 'Ric', 'Rob', 
    'Rod', 'Rog', 'Ron', 'Ros', 'Row', 'Roy', 'Ruf', 'Ruth', 'Sam', 'Sar', 'Sid', 'Sim', 'Sol', 'Ste', 'Stu', 'Sue', 
    'Syl', 'Ted', 'The', 'Tho', 'Tim', 'Tom', 'Ton', 'Urs', 'Vic', 'Vir', 'Viv', 'Wal', 'War', 'Wil', 'Wilf', 'Win', 
    'Wor', 'Wyn', 'Zac', 'Abel', 'Abr', 'Ach', 'Adal', 'Adolf', 'Aeth', 'Alar', 'Ald', 'Alv', 'Ambr', 'Arch', 'Arl', 'Arth', 
    'Atha', 'Audr', 'Bald', 'Beau', 'Beli', 'Bern', 'Blan', 'Brun', 'Cad', 'Cael', 'Cai', 'Cel', 'Cen', 'Chr', 'Cid', 'Cleof', 
    'Conr', 'Cons', 'Cyri', 'Dag', 'Diet', 'Diot', 'Ead', 'Eald', 'Ebra', 'Eber', 'Egbert', 'Eld', 'Elea', 'Elfr', 'Elys', 'Emm', 
    'Ermin', 'Ern', 'Eth', 'Faust', 'Fitz', 'Flav', 'Fran', 'Frem', 'Gabr', 'Gai', 'Gar', 'Geof', 'Gerar', 'Gilb', 'Godr', 'Gott', 
    'Guill', 'Gund', 'Gwen', 'Hadr', 'Hawk', 'Helo', 'Herv', 'Hild', 'Hilg', 'Holm', 'Ida', 'Inga', 'Irmi', 'Jarl', 'Jero', 'Joan', 
    'Joaq', 'Josc', 'Josia', 'Judith', 'Klem', 'Lam', 'Lamb', 'Lau', 'Leif', 'Leod', 'Leom', 'Leop', 'Loth', 'Luc', 'Ludo', 
    'Lup', 'Magn', 'Marce', 'Mart', 'Maur', 'Maxi', 'Melv', 'Mica', 'Milv', 'Nor', 'Odil', 'Odon', 'Off', 'Osm', 'Otth', 'Owin', 
    'Pasc', 'Perci', 'Petron', 'Phine', 'Piers', 'Plac', 'Rein', 'Reym', 'Richm', 'Rinal', 'Roder', 'Roel', 'Rowl', 'Sigm', 
    'Sixt', 'Stam', 'Tancr', 'Thib', 'Thorf', 'Thorv', 'Tryg', 'Ulr', 'Ursm', 'Valt', 'Vikt', 'Wald', 'Walther', 'Wit', 'Wolf', 
    'Wulf', 'Ysm', 'Zeb', 'Zim'
    ]
    name_middle_parts = [
        'bel', 'bert', 'beth', 'bald', 'dred', 'drik', 'fred', 'gald', 'gar', 'gard', 'ger', 'hard', 'helm', 'lian', 'lina', 
        'lind', 'lisa', 'man', 'mar', 'met', 'mir', 'mund', 'nad', 'nard', 'nath', 'neer', 'nel', 'nor', 'phin', 'rad', 'rick', 
        'rold', 'rud', 'ryn', 'san', 'sandra', 'son', 'ston', 'thel', 'ther', 'trid', 'vald', 'ven', 'ver', 'vin', 'wald', 
        'ward', 'win', 'wyn', 'yell', 'bel', 'belle', 'claud', 'den', 'din', 'dora', 'dyn', 'eline', 'ene', 'fan', 'gene', 
        'hilde', 'la', 'lene', 'lene', 'leth', 'lie', 'lien', 'liev', 'line', 'lisa', 'lith', 'mand', 'maria', 'mine', 'mira', 
        'mona', 'mund', 'nath', 'nelle', 'nor', 'pat', 'quin', 'rene', 'reth', 'ric', 'rin', 'rine', 'ryn', 'seb', 'sey', 
        'stan', 'ston', 'tin', 'ton', 'uel', 'vin', 'vor', 'wen', 'ylen', 'zel', 'zia', 'zor', 'ang', 'ant', 'bra', 'cia', 'con', 
        'dar', 'del', 'dor', 'dre', 'ein', 'eis', 'eus', 'fan', 'fer', 'fran', 'fri', 'gie', 'gio', 'gis', 'gie', 'han', 'hel', 
        'hin', 'jan', 'jes', 'jin', 'kar', 'kie', 'laf', 'let', 'lin', 'lis', 'lud', 'mat', 'mir', 'mor', 'nat', 'nor', 'ral', 
        'ram', 'ric', 'sie', 'sta', 'sue', 'tan', 'tor', 'tri', 'vic', 'von', 'vin', 'wyn'
    ]
    name_end_parts = [
        'a', 'ah', 'an', 'ard', 'ard', 'as', 'bel', 'bert', 'beth', 'dine', 'dine', 'dith', 'don', 'dor', 'dra', 'dred', 
        'dyn', 'e', 'el', 'el', 'en', 'er', 'et', 'eth', 'eus', 'ey', 'fred', 'ga', 'gar', 'go', 'goth', 'gus', 'ham', 'hard', 
        'helm', 'ia', 'ian', 'ias', 'ic', 'ice', 'ie', 'iel', 'ien', 'ier', 'if', 'in', 'ine', 'io', 'ion', 'is', 'isa', 'ius', 
        'la', 'line', 'lis', 'lith', 'lon', 'ma', 'mar', 'mer', 'mir', 'mond', 'mund', 'na', 'nard', 'ne', 'nel', 'neth', 
        'ney', 'ni', 'no', 'nor', 'on', 'or', 'os', 'que', 'ra', 'rad', 'ran', 'red', 'ric', 'rick', 'rid', 'ro', 'ron', 'ros', 
        'sa', 'san', 'sel', 'son', 'ston', 'ta', 'tan', 'tha', 'ther', 'thia', 'tia', 'tin', 'ton', 'uel', 'us', 'va', 'ver', 
        'vin', 'ward', 'wen', 'win', 'wyn', 'ya', 'yah', 'zar', 'zo'
    ]

class race():
    def __init__(self,name:str,strength_modifier:int,constitution_modifier:int,intelligence_modifier:int,agility_modifier:int):
        self.name = name
        self.strength_modifier = strength_modifier
        self.constitution_modifier = constitution_modifier
        self.intelligence_modifier = intelligence_modifier
        self.agility_modifier = agility_modifier
class profession():
    def __init__(self,name):
        self.name = name
class _map: #UNUSED
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
    class city:
        def __init__(self,city_name,city_ruler):
            self.city_name = city_name
            self.city_ruler = city_ruler
    class town:
        def __init__(self,town_name,town_ruler):
            self.town_name = town_name
            self.town_ruler = town_ruler
class character(): #Can be any character within the game. Everything from a side character who you meet at a lonely crossroads, to the player themselves
    def __init__(self,race,profession,name,initiative = 0,strength = 10,constitution = 10,intelligence = 10,agility = 10,armor_class = 4,max_health=10):
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
        self.max_health = max_health + self.race.constitution_modifier
        self.health = max_health
        
        #Inventory vars
        self.inventory = []
        self.max_weight = self.strength * 15
        self.current_weight = 0
        self.equiped_weapon = None
    def create_random(self):
        self.strength = random.randint(5,20) + self.race.strength_modifier
        self.constitution = random.randint(5,20) + self.race.constitution_modifier
        self.intelligence = random.randint(5,20) + self.race.intelligence_modifier
        self.agility = random.randint(5,20) + self.race.agility_modifier
        self.armor_class = random.randint(3,5) + self.race.agility_modifier
        self.health = random.randint(5,15) + self.race.constitution_modifier
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

    #World interaction
    #These are all things that a character can use to interact with the world (Ex: Picking something up (aquire) or attacking (attack))
    def printinvent(self):
                print(f"|INVENTORY|{self.name}|")
                if self.equiped_weapon:
                    print("|~~~~~~~~~~~~~~~~~~~")
                    print(f"|EQUIPED: {self.equiped_weapon.name}")
                print("|~~~~~~~~~~~~~~~~~~~")
                total_weight = sum(item.weight for item in self.inventory) #This adds up all of the items weights in the inventory.
                print(f"|WEIGHT: {total_weight}/{self.max_weight}lbs")
                print("|~~~~~~~~~~~~~~~~~~~")
                for item in self.inventory:
                    print(f"|{round(item.weight,2):>4}|{item.name}") #Prints weight | name. Round weight to a maximum of 2 decimal places, ensures that | will always be alligned using the :>4
                print("|~~~~~~~~~~~~~~~~~~~")
                print()
    def equip_weapon(self,weapon,from_invent = False): #Equip a weapon to the weapon slot. Attack will only reference an equiped weapon. IF YOU WANT TO EQUIP A WEAPON FROM THE INVENTORY, MAKE SURE YOU SET from_invent TO TRUE. This will not remove the weapon from the inventory, it simply references it in the equiped_weapon variable
        """equips a weapon. Only equiped weapons can do damage.\n
        -----
        to equip a weapon from the inventory, set from_invent to true. \n
        For more info, see utils/components.py character.equip_weapon()"""
        if isinstance(weapon,items.weapon):
            if from_invent:
                if weapon in self.inventory:
                    self.equiped_weapon = weapon
                    print(f"EQUIPED {weapon.name}")
                else:
                    raise itemNotFoundError("Item not found in inventory even though from_invent is set to True")
            else:
                self.equiped_weapon = weapon
                print(f"EQUIPED {weapon.name}")
        else:
            raise TypeError(f"Expected type 'weapon' but got '{type(weapon.__name__)}' instead")#Raises an error if a weapon object is not in the paramaters. This is because the script will need to reference properties of a weapon object later on, and we dont want having bread equiped as your weapon to raise errors far down the line.
    def attack(self,target):
        """attack target. Rolls to hit, on hit deals damage.\n
        -----
        See comments for more info on damage delt. Still under heavy development"""
        if isinstance(target,character): #Check if the target has the proper capabilities to be attacked. We do this because non character objects may not have an armor_class or health.
            roll = random.randint(1,20)#roll for hit
            if roll > target.armor_class:
                print("Hit!")
                if self.equiped_weapon:
                    target.health -= self.equiped_weapon.attack_role()
                else:
                    target.health -= 1 #Perform a punch
            else:
                print("Miss!")
        else:
            raise TypeError(f"Expected type 'character' but got '{type(target.__name__)}' instead") #Raise type error if target is not a character object
    def aquire(self,target): #This allows a character to pick something up
        """'Pick up' target, put in inventory. target must have the property 'is_pickable'\n
        --------  
        see comments in utils/components for more"""
        if hasattr(target,"is_pickable"): #Check if the target is able to be picked up, basically making sure its an item. See utils/items and you will find that each item has an is_pickable property
            print(f"YOU HAVE AQUIRED: {target.name} TYPE: {target.item_type}")
            self.inventory.append(target)
        else:
            #raise is a way to show an error message. Its not necessary, but makes alot of code handling nicer because you can have a custom error rather than what python thinks could be an error.
            raise TypeError(f"Expected type 'item' but got '{type(target).__name__}' instead") 
            #If you are allowing the player to call aquire on whatever they want, I would reccomend using a try except block and checking for type errors, and then returning something like "Sorry, but you cannot pick that up"
class shop():
    def __init__(self,item_value_pairs:dict,linked_character:character = None):
        self.item_value_pairs = item_value_pairs
        self.linked_character = linked_character
        print(self.item_value_pairs)
