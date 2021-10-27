"""
- initialize a dicionary for count
- iterate over input_str
    -if letter not in dictionary assign that letter a count of 1
    -if letter already in dictionary add +1 to exiting count
- iterate over indcies of range of input_str
    -if value at any index (letter) has a count of just 1 retun the index of that letter 
- cover the edge case (no unique letter) with an additional return as -1
"""

def csFirstUniqueChar(input_str):
    count = {} # dictionary of Count:Letters i.e. key:value
    for letter in input_str:
        # print(letter)
        if letter not in count:
            count[letter] = 1 # assigns the letter(value) a key of 1
        else:
            count[letter] +=1 # amends the key by +1 for that letter(value) in Key:value pair
    print(count)
    for index in range(len(input_str)):
        if count[input_str[index]] == 1:
            return index
    return -1

print(csFirstUniqueChar(input_str = "lambdaschool")) # 2
print(csFirstUniqueChar(input_str = "ilovelambdaschool")) #  0
print(csFirstUniqueChar(input_str = "vvv")) # -1