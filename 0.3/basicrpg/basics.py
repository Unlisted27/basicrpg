#All of the VERY basic functions. there should be no imports in this code except for random
import random, os

def roll(dice_amount,dice_value):
    result = sum(random.randint(1,dice_value) for _ in range(dice_amount))
    return(result)

def menu(name:str,options:list,horizontal_sign="_",vertical_sign="|"):
    '''Displays a menu of the paramater options.
    -
    Selected option returned as string
    -
    ex: menu("Choose",["a","b","c"]) 
    --> choice (say the player chose [1] (a), "a" would be returned)'''
    length = 1
    i=1
    items = []
    for item in options:
        if type(item) != str:
            raise TypeError("Items in list must be type str")
        else:
            items.append(f"{vertical_sign}[{i}]{item}")
            i+=1
    for thing in items:
        if len(thing) > length:
            length = len(thing)
    print(horizontal_sign*length)
    print(name + " "*(length - 1 - len(name)))
    #print(f"|\033[4m{name + " "*(length - 1 - len(name))}\033[0m")#The funny characters are the underlined escape sequence in python
    for thing in items:
        print(thing)
    while True:
        try:
            answer = input(f"{vertical_sign}:")
            selected = options[int(answer)-1]
            return(selected)
        except Exception as e:
            #print(e) #Uncomment this line to show error message when the user enters an invalid option
            print("Invalid selection, try again")

def clear_screen():
    """Clears the terminal, does not work on every operating system, should work on most tho"""
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')