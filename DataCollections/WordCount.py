# Create a list of words
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'kiwi', 'apple']
# Create an empty dictionary to store word frequency
word_count = {}
# Count the frequency of each word
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
# Print the dictionary
print(word_count)
