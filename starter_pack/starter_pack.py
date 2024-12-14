from utils import components
from utils import generators
from utils import items as item #We import items as item so that we can reference item in this script (item.weapon()). This allows people using the starter pack to reference items (items.foods.bread). Just makes it nicer to use

#Game objects. These are preset objects for you to use! They all fit around a medieval/fantasy theme.
#THIS REQUIRES THE REST OF THE PROGRAM TO BE INSTALLED (NEEDS THE THINGS IN utils TO WORK)
#Having issues with first try? Consider cloning the entire repo from github so you can make sure everything is there
class races():
    human = components.race("human",0,0,0,0)
    goblin = components.race("goblin",-1,-1,-1,0)
class professions():
    commoner=components.profession("commoner")
class items():
    class weapons():
        #Note, i have provided variables (name=, etc) just for your understanding. They are not required.
        short_sword = item.weapon(name="short sword",weight=2,description="A short blade, powerful none the less",attack_dice=(1,6),base_damage=2) #Creates a short sword that does 1d6 damage. Meaning that on hit, the game will 'roll' 1, 6 sided 'dice', basicaly generating 1 random number between 1-6. 
    class foods():
        bread = item.food("Bread",0.2,"It's just bread",1)
class characters():
    player = components.character(races.human,professions.commoner,generators.genname())#Basic character creation. To see behind the screens of what goes into a character object, check out utils/components.py character
    goblin1 = components.character(races.goblin,professions.commoner,generators.genname())#Sane as top, but race is set as goblin