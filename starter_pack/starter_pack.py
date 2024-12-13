from utils import components
from utils import generators
from utils import items as item

#Game objects. These are preset objects for you to use! They all fit around a medieval/fantasy theme.
#THIS REQUIRES THE REST OF THE PROGRAM TO BE INSTALLED (NEEDS THE THINGSIN utils TO WORK)
#Having issues with first try? Consider cloning the entire repo from github so you can make sure everything is there
class races():
    human = components.race("human",0,0,0,0)
    goblin = components.race("goblin",-1,-1,-1,0)
class professions():
    commoner=components.profession("commoner")
class items():
    class foods():
        bread = item.food("Bread",0.2,"It's just bread",1)
class characters():
    player = components.character(races.human,professions.commoner,generators.genname())#Basic character creation. To see behind the screens of what goes into a character object, check out utils/components.py character
    goblin = components.character(races.goblin,professions.commoner,generators.genname())#Sane as top, but race is set as goblin