import random
from basicrpg.components import name_parts

def genname(args="first"):
    length = random.randint(2,3)
    if args == "first":
        if length == 2:
            name = name_parts.name_start_parts[random.randint(0,len(name_parts.name_start_parts)-1)] + name_parts.name_end_parts[random.randint(0,len(name_parts.name_end_parts)-1)]
        if length == 3:
            name = name_parts.name_start_parts[random.randint(0,len(name_parts.name_start_parts)-1)] + name_parts.name_middle_parts[random.randint(0,len(name_parts.name_middle_parts)-1)] + name_parts.name_end_parts[random.randint(0,len(name_parts.name_end_parts)-1)]
        return(name)