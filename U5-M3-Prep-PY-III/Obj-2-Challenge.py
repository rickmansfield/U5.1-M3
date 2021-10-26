"""
Use built-in Python methods to print the identity, type, and value of `example_object`.
"""
example_object = "I have an identity, type, and value."
print(id(example_object))
print(type(example_object))
print(example_object)


"""
Use a built-in Python operator to determine if `a` and `b` have the same identity.
"""
a = 1
b = a
print(id(a), id(b)) # hence they have the same identity