# Creating a dictionary
productRange = {"item1": 32.99, "item2": 45.99, "item3": 22.99}
print("Initial dictionary:", productRange)

# Accessing an item in the dictionary
print("Price of item2:", productRange["item2"])

# Amending or modifying an item in the dictionary
productRange["item2"] = 35.99
print("Dictionary after modifying item2:", productRange)

# Adding a new item to the dictionary
productRange["item4"] = 50.99
print("Dictionary after adding item4:", productRange)

# Deleting an item from the dictionary
del productRange["item3"]
print("Dictionary after deleting item3:", productRange)


'''
Creating a Dictionary: The dictionary productRange is defined with three items, where each item has a unique key (e.g., "item1") and an associated value (e.g., 32.99).
Accessing an Item: To get the value associated with a key, use productRange["item2"].
Modifying an Item: To change the value of an existing key, assign a new value, like productRange["item2"] = 35.99.
Adding a New Item: Adding a new key-value pair is as simple as assigning a value to a new key, e.g., productRange["item4"] = 50.99.
Deleting an Item: The del keyword removes a key-value pair, for example, del productRange["item3"].
'''