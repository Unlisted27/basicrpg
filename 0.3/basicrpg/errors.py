#All the custom error messages

class itemNotFoundError(Exception): #Used when an item is referenced but not found. For example, an item is equiped from the inventory, but the item referenced does not exist within the inventory.
    print("Hint: item is refernced but not found, ensure the referenced item exists where is it being referenced, in the inventory for example.")