
---  
# Change Log  
---
## Version 0.1.0 Pre Alpha

### Major changes

### Minor changes and fixes
- Stopped importing the map object in components as it is non-functional
- Stopped importing the item object as it is non-functional

---
## Version 0.0.10 Pre Alpha  
- Kinda forgot everything I added, but i'll try to remember  
### Basics
- all of the most basic functions such as dice rolling. This should use ZERO internal imports in order to avoid feedback loops of other things needing a function here which requires that things code to work.
#### - roll
    - Added roll function
    - Takes imputs of the number of dice to be rolled and their maximum value
    - randomizes number pertaining to those inputs, and outputs the result

### Components  
- all of the main objects in basic RPG aside from items. This is what everything needs to run
#### - name_parts  
    - Added name_parts  
    - Name parts is 3 lists containing the start pieces, middle pieces, and end pieces of old names  
    - NOTE: This list was generated with chat GPT. ain't no way i'm wasting time making that, bite me  
#### - race  
    - Added race object  
    - properties: name, strength_modifier, constitution_modifier, intelligence_modifier, agility_modifier  
    - modifiers being derived from race is likely to change completly in the future  
    - race objects can be created, and are required to create any character object.  
#### - profession  
    - Added profession object  
    - properties: name
    - does very little right now, expect LOTS more soon  
#### - map
    - CURRENTLY UNUSED  
    - Hasnt been developed since extremly early days of the project  
    - I doubt it even works  
    - No plan for future development of this object, but in much later stages, I do plan to add a map system of some kind  
#### - character
    - Added character object  
    - By far the most complex object in basicRPG  
    - Has the following variables
        race
        profession
        name
        initiative
        - stats
        strength
        constitution
        intelligence
        agility
        armor_class
        max_health
        health
        - inventory
        inventory
        max_weight
        current_weight
        equiped_weapon
    - every character in the game (including the player) should be a character object for compatibility  
    - Functions  
        - create_random
        Randomizes the base character stats. This means that a programmer does not need to manually input all of the stats values
        Currently works by randomizing values in a range plus a race stat modifier, and will surely be updated in the future to create values based on more direct elements.  
    - printstats
        -Displays the character stats in a nicely formatted manner. Kind of like a simple character sheet  

    - printinvent
        - Displays the character inventory in a nicely formatted manner. Displays the equiped weapon, the total inventory weight / the total carying capacity, and the weight of each item
    - equip_weapon
        - Equips a weapon object to the equiped_weapon variable, i.e the 'weapon slot'
        - Weapons MUST be equiped for their effects to work in combat
        - If the from_invent property is set to True, than the function will return an error if the specefied weapon is not in the character inventory.
    - attack
        - Attacks a target
        - Requires as character object as the paramaters
        - steps
            - roll for hit
            - reduce target.health by the attack role of the equiped weapon, if no weapon is equiped, reduces by 1
    - aquire
        - Causes the character to pick up an item
        - the item must have the property is_pickable  

### errors
- All of the custom error messages for this project
#### - itemNotFoundError
    - added itemNotFoundError
    - used when an item is called from a location where it does not exist

### generators
- All of the randomizers (or generators) of the project
#### - genname
    - Generates a name using the name_parts in components

### items
- All of the different item objects, basically anything a character can obtain
- Formatting for creating item objects provided unter utils/items.py
- All item objects should have a use function (even if it is just pass)
- 
#### - item
    - Unused, just a demo for the minimum requirements of an item object
#### - food
    - food objects can be carried and consumed by a character
    - will add health to the character
#### - weapon
    - It's a weapon.
    - Can be equiped to the character weapon slot (equiped_weapon)
    - functions
        - attack_role()
            - performs an attack role, outputs a damage value (int)
        - use()
            - Standard item use function. This one just displays a nice message

### Starter pack (NO LONGER WITHIN THIS REPO)
    - This is a collection of premade objects all centered around a fantasy theme. I encourage you to look at how these were created, maybe experiments a little, and then go make your own! 
    - Curent assets:
        - races
            - human
            - goblin
        - professions
            - commoner
        - items
            - weapons
                - short_sword
            - foods
                - bread
            - characters
                - player
                - goblin1
    - For more, see starter_pack/README.md

## Version 0.1.0 Pre Alpha
Oops, stopped development for like 2 weeks and forgot the improvements, but heres what I remember
-Changes to weapons: added equiped weapon slot in inventory, improved weapon damage calculations?

## Version 0.2.0 Pre Alpha
-Added menu function under basics
-Added character name to the inventory header
-Changed the URL in setup.py to link to the basicrpglib github
-brought back item objects. I think these will be most used in trade

--Things I tried--
-Began work on shop system, not in development for now tho

# Verson 0.2.1 Pre Alpha
-Added room objects
    -room(name:str,description:str = None,function = None)
        -name: a string name of the room, will display at the top when the room is executed
        -description: The room text, string, will display below name when room is executed
        -function: (UNTESTED) function will be called when room is executed, None by default cause not needed.
    -Room objects have 2 functions
        -set_exits(exits:dict{"exit_name" : exit:basicrpg.room})
            -Sets the exit or doorway options of the room
            -Will display options for exiting the room, each option is the exit_name, and the destination is the probided room object
        -execute()
            -Will execute the code of the room. This function should only be run on the first room in a sequence of rooms, as travel between rooms should be done with set_exits, which will automatically call execute() on the destination room object that the user has selected. Execute could be neat for teleporting, for example, you could have an event which teleports the player to a new "dungeon" that was not connected to the originating set of rooms by calling exit() on the teleport destination of the "dungeon", maybe the entrance chamber for example.

## Version 0.3.0
-Changed the room.set_exit function to room.set_doors, and changed all references to exit/exits into door/doors.This was done to avoid conflict with the builtin python exit() method.

-Added the room.set_contents({"item_name":item:basicrpg.item}) function. This now allows the room to have contents that the character can interact with.

-Added art folder and cover art ASCII image.

## Version 0.3.1
-Made the gap between rooms more evident. Now when you enter a new room, it should be easier to tell
-Added clear_screen function in basics
-Added option to clear screen when entering a new room

## Version 0.3.2
-Added the basicrpg.room.set_actions(actions:dict) function
    -Added custom actions (functions) within rooms
    -These actions, as well as the default "Inspect" and "Leave" actions will be displayed when the player enters the room
-Added the nevermind option within default room actions
-Fixed bug where the itemNotFound error would be called when imported.
-removed testrpg.py in prep for pypi release

## Version 0.3.3
-menu function now returns the number selected instead of the string selected, by default
-Added the return_tuple flag to the menu function to return the string and number in a tuple should the flag be set to true
-Updated type hints on character objects