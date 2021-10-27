"""
- i = loop/iterate over the list extracting each digit start at index zero
- j = /loop/iterate over the list again extract second digit starting a i+1
- Conditional = if (digit at list[i]) + (digit at list[j]) = target
    - print newList populated with digits for i & j i.e. [i, j]
"""


# def csSortedTwoSum(numbers, target):
#     for indexA in range(len(numbers)):
#         for indexB in range(indexA + 1, len(numbers)):
#             if numbers[indexA] + numbers[indexB] == target:
#                 return[indexA, indexB]
#     return[]

def csSortedTwoSum_2(numbers, target):
    dictionary1 = {}
    
    for index in range(len(numbers)):
        LHS = numbers[index] # this is the left hand number
        RHSKey = target - LHS # this is the right hand number
        if RHSKey in dictionary1:
            return[dictionary1[RHSKey], index] # returns value of dictionary1[RSHKey] 
        dictionary1[numbers[index]] = index # assigns the value of numbers[index]
        print(dictionary1)
    return[]
        

# print("---[2, 5, 9, 13], 7---")
# print(csSortedTwoSum([2, 5, 9, 13], 7)) # [0,1]

# print("----([4, 3, 5], 8)----")
# print(csSortedTwoSum([4, 3, 5], 8)) # [1,2]


print("---[2, 5, 9, 13], 7---")
print(csSortedTwoSum_2([2, 5, 9, 13], 7)) # [0,1]

print("----([4, 3, 5], 8)----")
print(csSortedTwoSum_2([4, 3, 5], 8)) # [1,2]

# # -> [0,1] (nums[0] + nums[1] == 7)
# print(csSortedTwoSum(numbers=[2, 5, 9, 13], target=7))

# # -> [1,2] (nums[1] + nums[2] == 8)
# print(csSortedTwoSum(numbers=[4, 3, 5], target=8))
