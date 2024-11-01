# Syntax for iterating with numbers
sequence = range(5)

for number in sequence:

    print(number)

# Controlling for loops
sequence = range(5)

for number in sequence:

    if number == 3:

        break

    print(number)


# You can also use a condition and the continue statement to skip an iteration in the same way as you can for while loops:

sequence = range(5)

for number in sequence:

    if number == 3:

        continue

    print(number)

# Iterating across a range with a start and stop point
sequence = range(5,10)

for number in sequence:

    print(number)

# Iterating across a range in given increments
sequence = range(10,50,5)

for number in sequence:

    print(number)

# Demo

number=9
salaries=[20000,300,5000,567,789,899,677,899]

print(len(salaries))
print("total:",sum(salaries))
print("Biggest:",max(salaries))
print("Smallest:",min(salaries))

'''print(salaries[0])
print(salaries[1])
'''

for item in salaries:
    print(item)

for item in salaries:
    print(item, "-" ,item*2)



# while loop
'''
You Don’t Know the Exact Number of Iterations: If the number of loop executions isn’t determined in advance but depends on a condition,
use a while loop. For example, you might not know how many times to prompt a user until they enter a valid input.

You Want to Repeat Until a Condition Changes: When you need the loop to keep running as long as a specific condition is True,
a while loop is ideal. For instance, monitoring a variable that changes during the loop.
'''
num = 0

while num < 100:

    num = num + 10

    print(num)

# for loop
'''
You Know the Number of Iterations: If you know in advance how many times the loop should run, 
a for loop is typically the best choice. For example, iterating over a range of numbers, a list, 
or any collection with a specific number of elements.

You’re Iterating Over a Collection: If you're looping through items in a list, tuple, dictionary, 
set, or any iterable, for is more straightforward and readable.
'''
for num in range(10, 101, 10):
    print(num)


'''
Use for loops for iterating a known number of times or directly over items in a collection.
Use while loops when the loop should continue until a specific condition is met, especially if the number of iterations is unknown.
'''

for word in "Hello world".split():

    print(word)



# Ask the user for a word
word = input("Enter a word: ")

# Print each character of the word on a separate line
for char in word:
    print(char)



'''
On the first iteration, fruit will take "Apple" as its value, and will print the result of fruit.upper(). 
It will then continue to the next iteration, until there are no elements left in the list.
'''
my_fruit = ["Apple", "Banana", "Orange"]

for fruit in my_fruit:

    print(fruit.upper())

# Iterating with dictionaries

productRange = {"item1":32.99,"item2":45.99, "item":25.99}

for price in productRange:

    print(f"{price} x 3 = {productRange[price]*3}")

'''
The Python interpreter will iterate dictionary in the same order that the values were created, 
there is no other underlying logic to the sequence.

When you iterate with a dictionary, the Python will interpret the for variable as the key, 
unless you place it within square brackets, in which case Python will interpret it as the value in the pair:
'''
productRange = {"item1":32.99,"item2":45.99, "item3":25.99}

for price in productRange:

    print(f"The price of {price} is £{productRange[price]}.")