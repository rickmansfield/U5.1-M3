# Perfrom basic dictionary operations

# Declaing a dictionairy 
phonebook = {
    "Rick": 2626434190,
    "Sara": 2623523965,
    "Joshua": 1234567102,
    "Elizabeth": 3216549878
}

# addung to existing dictionary
phonebook["Max"] = 2621324567
# print(phonebook)

# iterating throug an dictionary 
# for key, value, in dictionary.items():
for key, value in phonebook.items():
    print("Key Name: %s, Value Phone Number: %d" % (key, value))
    
# removing items from a dictionary using del
del phonebook["Joshua"]

print(phonebook.pop("Elizabeth"))
print(phonebook)