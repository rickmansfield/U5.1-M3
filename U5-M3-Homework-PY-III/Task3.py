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
- initiate empty list set it to a variable name to capture each letter "one time". 
- iterate over first string compared to newList
    - if char not in list newList.append(char)
- iterate over second string compare to newList
    - if char not in list newlist.appen(char)
- convert list to string using .join() & set to variable finalString
- return finalstring


"""
str1 = "aabbbcccdef"
str2 = "xxyyzzz"
def csLongestPossible(str_1, str_2):
    eachLetterOnce = []
    for char in str_1:
        if char not in eachLetterOnce:
            eachLetterOnce.append(char)
    for char in str_2:
        if char not in eachLetterOnce:
            eachLetterOnce.append(char)
    sortedList = sorted(eachLetterOnce)
    finalString = ''.join(sortedList)
    return finalString


print(csLongestPossible("aabbbcccdef", "xxyyzzz"))  # -> "abcdefxyz"
print(csLongestPossible("abc", "abc")) # -> "abc"
print(csLongestPossible("aretheyhere", "yestheyarehere"))