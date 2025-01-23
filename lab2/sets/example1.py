#Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)

#Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

#What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))