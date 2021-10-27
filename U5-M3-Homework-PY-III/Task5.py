"""
"""

def csFindAddedLetter(str_1, str_2):
    s1 = sorted(str_1)
    print(s1)
    s2 = sorted(str_2)
    print(s2)
    # this for loop accounts for differneces in the "middle" of both lists
    for i in range(len(str_1)):
        if s1[i] != s2[i]:
            return s2[i] # if this return is reached the fuction is done otherwise it drops to the next return
    return s2[-1] # for the edge case if the difference in letters in not before the end

print(csFindAddedLetter(str_1 = "bcde", str_2 = "bdcef")) # "f"
# print(csFindAddedLetter(str_1 = "", str_2 = "z")) # "z"
# print(csFindAddedLetter(str_1 = "b", str_2 = "bb")) # "b"
# print(csFindAddedLetter(str_1 = "bf", str_2 = "bfb")) # "b"

