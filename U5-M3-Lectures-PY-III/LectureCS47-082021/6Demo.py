"""
Demonstration
Given a non-empty array of integers `nums`, 
every element appears twice except except for one. 
Write a function that finds the element that only appears once.
Examples:
- create a list
- sort the list in place
- create a for loop to go through it
- check if the index at i is not eq to the index of i - 1
 - keep the item
- otherwise
  - remove the item from the list


- create a singles list

- iterate over all numbers
  - if the number is not in our singles list
    - append it to our singles list
  - otherwise
    - remove it from the singles list

- create a dictionary
- fill the dictionary with each number as a key, and a value of zero
- iterate over the numbers extracting num
  - increment the dictionary at key of num 

- iterate over the items in the dictionary `.items()` extracting key, val
  # check if the val is equal to 1
    # return the key to the caller

- return the last item in the singles list
- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""


def single_number(nums):
    singles = []

    for num in nums:
        if num not in singles:
            singles.append(num)
        else:
            singles.remove(num)

    return singles.pop()


print(single_number([3, 3, 2]))  # -> 2
print(single_number([5, 2, 3, 2, 3]))  # -> 5
print(single_number([10]))  # -> 10
