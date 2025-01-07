#All the custom error messages

class itemNotFoundError(Exception): #Used when an item is referenced but not found. For example, an item is equiped from the inventory, but the item referenced does not exist within the inventory.
    pass