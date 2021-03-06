"""
Demonstration #2
Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.
Examples:
- single_number([3,3,2]) -> 2
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""

def single_number(nums):
    no_dupes = []

    for numb in nums:
        if numb not in no_dupes:
            no_dupes.append(numb)
        else:
            no_dupes.remove(numb)
        print(no_dupes)

    return no_dupes.pop() # same as no_dupes[0]

    # Solution 2
    my_dict = {num: 0 for num in nums}

    for i in nums:
        my_dict[i] += 1

    for key, val in my_dict.items():
        if val == 1:
            return key


print(single_number([3, 3, 2]))  # -> 2
print(single_number([5, 2, 3, 2, 3]))  # -> 5
print(single_number([10]))  # -> 10
