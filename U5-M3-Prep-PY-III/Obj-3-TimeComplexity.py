  """
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""
def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps



"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""
def sorted_squares(A):
    N = len(A)
    j = 0
    while j < N and A[j] < 0:
        j += 1
    i = j - 1

    ans = []
    while 0 <= i and j < N:
        if A[i]**2 < A[j]**2:
            ans.append(A[i]**2)
            i -= 1
        else:
            ans.append(A[j]**2)
            j += 1

    while i >= 0:
        ans.append(A[i]**2)
        i -= 1
    while j < N:
        ans.append(A[j]**2)
        j += 1

    return ans



"""
Classify the runtime complexity of the insertion_sort function below using Big O notation.
"""
def insertion_sort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key
