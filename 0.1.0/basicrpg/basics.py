#All of the VERY basic functions. there should be no imports in this code except for random
import random

def roll(dice_amount,dice_value):
    result = sum(random.randint(1,dice_value) for _ in range(dice_amount))
    return(result)