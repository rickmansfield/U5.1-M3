"""
Using Big O Notation, what is the correct classification of time complexity for the fucntion below

My Answer is "O(n)"
because each portion looks linear to me. No matter how many items 
are in the list the time has to grow linearly to accomodate that list size. 
"""

def do_lots_of_things(items):
    last = len(items) - 1
    print(items[last]) ## my guess O(n)
    
    middle = len(items) / 2 
    i = 0
    while i < middle: ## my guess O(n)
        print(items[i]) 
        i += 1
    for num in range (100): ## my guess O(n)
        print(num)
        
alphaGroups = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
beta = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
delta = beta = ["a", "b", "c", "d", "e"]
print(do_lots_of_things(delta))

