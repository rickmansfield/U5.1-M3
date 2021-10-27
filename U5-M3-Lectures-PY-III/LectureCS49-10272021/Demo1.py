"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.
Examples:
- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)
Notes:
- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.

i = 0, 1
j = i + 1, 2, 2
nums[i] + nums[j] ?? target?
3 + 5 == 8?
nums = [2,5,9,13], [4,3,5]

[i, j]
[1, 2]

iterate over nums extracting i starting at zero
  iterate over the nums extracting j starting at i + 1
    if nums at index of i plus nums at index of j are equal to target
      return a list of i, j

return an empty list to the caller

"""
from time import time


def two_sum(nums, target):  # O(n^2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# get the complement (target = nums[??])
# check if the mapping contains the complement
#   return a list with the mapping[the complement], index

# set mapping[nums[index]] equal to the index
# 100000
def two_sum_d(nums, target):  # O(n)
    mapping = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in mapping:
            return [mapping[complement], i]

        mapping[nums[i]] = i

    return []


start = time()
# -> [0,1] (nums[0] + nums[1] == 7)
print(two_sum(nums=[2, 5, 9, 13], target=7))
print(two_sum(nums=[4, 3, 5], target=8))  # -> [1,2] (nums[1] + nums[2] == 8)
end = time()

print("O(n2)", end - start)

start = time()
# -> [0,1] (nums[0] + nums[1] == 7)
print(two_sum_d(nums=[2, 5, 9, 13], target=7))
print(two_sum_d(nums=[4, 3, 5], target=8))  # -> [1,2] (nums[1] + nums[2] == 8)
end = time()

print("O(n)", end - start)
