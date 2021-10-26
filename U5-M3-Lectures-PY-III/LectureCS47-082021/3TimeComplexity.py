"""
Constant Time O(1)
"""
def print_one_item(items):
    print(items[0])

"""
Linear Time O(n)
"""
def print_every_item(items):
    for item in items:
        print(item)

"""
Quadratic Time O(n^2)
"""
def print_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)
"""
What about constants?
"""
def do_a_bunch_of_stuff(items): # O(1 + n/2 + 2000) -> O(n)
    last_idx = len(items) - 1
    print(items[last_idx]) # O(1)

    middle_idx = len(items) / 2
    idx = 0
    while idx < middle_idx: # O(n/2)
        print(items[idx])
        idx = idx + 1

    for num in range(2000): # O(2000)
        print(num)

"""
Most significant term
"""
def do_different_things(items): # O(n + n^2) -> O(n^2)
    for item in items: # O(n)
        print(item)

    for item_one in items: # O(n * n) = O(n^2)
        for item_two in items:
            print(item_one, item_two)

"""
Big O is the worst case
"""
def search_for_thing(items, thing): # O(n)
    for item in items:
        if item == thing:
            return True

    return False

"""
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""

def number_of_steps(num): # O(log(n))
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps

# print(number_of_steps(10))
print(number_of_steps(10000))