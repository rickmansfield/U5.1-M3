import builtins
import math
# print(dir(builtins))
# print("-------------")
# print(help(slice))
# print("-------------")
# print(help(map))
# print("-------------")
# print(help(any))
# print("-------------")
# print(help(chr))
# print("-------------")
# print(help(iter))
# print("-------------")
# print(help(list))
# print(dir(count))
# print(list("aabbbcccdef"))
"""
- initiate empty string/list set it to a variable name to capture each letter "one time" (from either list)
- initiate a counter to track duplicate matches
- iterate over first string/list with characters from second string/list to find duplicates
- count number of times char in str1 fourn in str2
- write a conditional if str1 char in str2 count += 1
- if counter <2 append char to newList[]
-
- return final newString


"""
str1 = "aabbbcccdef"
str2 = "xxyyzzz"
def csLongestPossible(str_1, str_2):
    eachLetterOnce = []
    matchCounter = 0
    # list1 = str_1.split()
    # list2 = str_2.split()
    # print(list1)
    for char in str_2:
        if char in str_1:
            matchCounter += 1
        else:
            matchCounter = 1
        if matchCounter <=1:
            foundOnce.append(char)
    return foundOnce


print(csLongestPossible("aabbbcccdef", "xxyyzzz"))  # -> "abcdefxyz"
print(csLongestPossible("abc", "abc")) # -> "abc"