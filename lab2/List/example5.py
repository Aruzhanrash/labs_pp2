#Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


#Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

