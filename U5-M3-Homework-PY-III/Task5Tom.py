def csFindAddedLetter(str_1, str_2):
    counter1 = {}
    counter2 = {}
# ----counter1 = {}-------------
    for letter in "abcdefghijklmnopqrstuvwxyz":
        counter1[letter] = 0
        counter2[letter] = 0

    for char in str_1:
        counter1[char] += 1

    for char in str_2:
        counter2[char] += 1

    for char in str_2:
        if counter1[char] != counter2[char]:
            return char  
        
# -------counter2 = {}-------------

    # for letter in "abcdefghijklmnopqrstuvwxyz":
    #     counter1[letter] = 0
    #     counter2[letter] = 0

    # for char in str_1:
    #     counter1[char] += 1

    # for char in str_2:
    #     counter2[char] += 1

    # for char in str_2:
    #     if counter1[char] != counter2[char]:
    #         return char

print(csFindAddedLetter(str_1 = "bcde", str_2 = "bdcef")) # "f"
print(csFindAddedLetter(str_1 = "", str_2 = "z")) # "z"
print(csFindAddedLetter(str_1 = "b", str_2 = "bb")) # "b"
print(csFindAddedLetter(str_1 = "bf", str_2 = "bfb")) # "b"