counter = 0

def increment_counter():
    global counter
    counter += 1
    print('Counter:', counter)

# Modify the global counter
increment_counter()
increment_counter()
