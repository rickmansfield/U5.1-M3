"""
Using Big O notation, what is the correct 
classification of space complexity for the fuction below

My Answer is O(2n) which evaluates to O(n)
"""
    
def do_a_couple_things(n): ## my guess hence is O(2n)
    my_list = [] ## my guess O(1)
    my_second_list = [0] * 26 ## my guess O(1)
    
    for _ in range(n):
        my_list.append("lambda") 
        print(my_second_list[n % 25])
        
    return my_list

print(do_a_couple_things())