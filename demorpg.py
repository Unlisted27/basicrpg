#Demo script to show how basicrpg can be used
#imports
from utils import components #Imports the main juicy of this thing. Components are all of the custom objects that I've made
from utils import generators #Generators. This is a bunch of generator functions for different things. They will be pretty self descriptive
from starter_pack import starter_pack
import random

#Example of a how you can use the starter_pack and some of my basic functions
#Don't just use my boring starter pack, to learn how to create your own basicrpg objects, see starter_pack/starter_pack.py, and if you want to see what goes on behind the scenes of a basicrpg object, check out utils/components.py
print("welcome, player!")
starter_pack.characters.player.create_random() #randomizes the atributes of the pre made player character provided in the starter pack. For lots more on character creation, see starter_pack/starter_pack.py characters.player
starter_pack.characters.player.printstats() #calls the printstats function. This function can be called on any character object. For more see utils/components.py character.
input()
starter_pack.characters.player.aquire(starter_pack.items.foods.bread) #uses the aquire function of the premade player character to pick up the premade bread. Both player and bread located in starter_pack. For more creating items and characters, see starter_pack/starter_pack.py characters and items. For more behind the scenes, check out utils/components character and item.
starter_pack.characters.player.aquire(starter_pack.items.weapons.short_sword)
starter_pack.characters.player.equip_weapon(starter_pack.items.weapons.short_sword,True)
input()
starter_pack.characters.player.printinvent() #Prints the player inventory. printinvent can be called on any character object. See utils/components.py charater for more.
input()
starter_pack.characters.gnarwl.create_random()
starter_pack.characters.gnarwl.printstats()
input("ATTACK THE GOBLIN")
starter_pack.characters.player.attack(starter_pack.characters.gnarwl)
starter_pack.characters.gnarwl.printstats()

