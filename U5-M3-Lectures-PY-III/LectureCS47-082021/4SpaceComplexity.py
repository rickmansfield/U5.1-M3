"""
Constant Space O(1)
"""
def print_lambda_n_times(n):
    for i in range(n):
        print("lambda")

def get_the_max(items_list):
    maximum = float("-inf")
    for item in items_list:
        if item > maximum:
            maximum = item

    return maximum

"""
Linear Space O(n)
"""
def append_to_list_n_times(n):
    my_list = [] # O(1)

    for _ in range(n): # O(n)
        my_list.append("lambda") # O(1)

    return my_list

"""
Use Big O notation to classify the space complexity of the function below.
"""
def fibonacci(n): # O(n)
    lst = [0, 1] # O(2)
    for i in range(2, n): # O(n)
        lst.append(lst[i-2] + lst[i-1]) # O(2)

    return lst[n-1] # O(1)



"""
Use Big O notation to classify the space complexity of the function below.
"""
def fibonacci_two(n): # O(1)
    x, y, z = 0, 1, None # O(3)

    if n == 0:
        return x
    if n == 1:
        return y

    for i in range(2, n):
        z = x + y
        x, y = y, z

    return z

"""
Use Big O notation to classify the space complexity of the function below.
"""
def do_something(n): # O(n^2)
    lst = [] # O(1)
    for i in range(n): # O(n)
        for j in range(n): # O(n)
            lst.append(i + j) # O(n^2 * 2)

    return lst