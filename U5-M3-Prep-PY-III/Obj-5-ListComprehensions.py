"""
[<map expression> for <name> in <sequence expression> if <filter expression>]
"""
    
sentence = "Every moment is a fresh beginning."
words = sentence.split() # converts the string to a list
print(words)        # ['Every', 'moment', 'is', 'a', 'fresh', 'beginning.']
word_lengths = []

# Using a for loop
for word in words:
    word_lengths.append(len(word))

print(word_lengths) # [5, 6, 2, 1, 5, 10]

# Using a list comprehension i.e. remove the loop
word_lengths = [len(word) for word in words]

print(word_lengths) # [5, 6, 2, 1, 5, 10]


"""---------------------- -----------------------------"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

# Using a for loop
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers) # [2, 4, 6, 8, 10]

# Using a list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers) # [2, 4, 6, 8, 10]