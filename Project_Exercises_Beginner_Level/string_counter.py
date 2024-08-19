# takes the inputted string
string = input('Please input string: ')
# creates a variable named 'words' , puts them all in lower case, then splits each of them via the spaces:
# The separator used to split the string.
# Definition: "When set to None (the default value), will split on any whitespace character
# (including n r t f and spaces) and will discard empty strings from the result."
words = string.lower().split()
# creates an empty dictionary called 'word_count'
word_count = {}

# iterates word in words (now split into separate words) ...just say word one more time, I don't think
# it was mentioned enough... mehehe ANYWAY! and for every word in the string it adds the word to the empty dictionary
# and counts the frequency that it occurs.
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# the program then prints the frequency that each individual word occurs
print("Word frequencies: ", word_count)