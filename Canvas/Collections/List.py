# Step 1: Create a list with at least five items
items = ["apple", "banana", "cherry", "date", "elderberry"]

# Step 2: Change the value of one item in the list
items[1] = "blueberry"  # changing "banana" to "blueberry"

# Step 3: Change the value of at least three items in the list in one statement
items[2:5] = ["cranberry", "dragonfruit", "fig"]  # changing "cherry", "date", "elderberry"

# Step 4: Add an additional item to the list
items.append("grape")

# Step 5: Remove an item from the list
items.remove("apple")

# Display the final list
print(items)
