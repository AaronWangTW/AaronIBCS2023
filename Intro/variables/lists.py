mylist = [5, 10, 20, 30]
print(mylist[3], type(mylist))

# array index is actually start address + size of one data element * offset
# e.g. list[1] is the list address +1

# normal for loops
for val in mylist:
    print(val)

for val, idx in enumerate(mylist):
    print(f"{idx}: {val}")

# The following should be used only if needed
i = 0
while i < len(mylist):
    print(mylist[i])
    i = i+1

for i in range(len(mylist)):
    print(mylist[i])

mylist.append(25)
print(mylist, len(mylist))
# if an object has object.__len__, then it can be used by len()

mylist = [1, 2.5, "3.5", [4, 5], (6, 9)]
print(mylist, f"length:{len(mylist)}")

# special list initialization
mylist = [0]*15
print(mylist)
mylist = [1, 2, 3]*5
print(mylist)

# concat lists
lista = [1, 2, 3]
listb = [4, 5, 6]
print(lista+listb)
print([lista, listb])
lista.append(listb)
print(lista)

# find out if element in list
mylist = [1, 2, 3, 4, 5]
print(1 in mylist)
print(mylist.index(2))
print(mylist.index(3, 2, 4))  # (target, start idx, end id)

# insert into list
mylist.insert(4, "henlo")
print(mylist)
# remove element from list
mylist.remove("henlo")
print(mylist)

# pop, or remove
stuff = mylist.pop()
print(mylist, stuff)
stuff = mylist.pop(2)
print(mylist, stuff)

# counter
cnt = mylist.count(1)
print(cnt)
randomList = [5]*5
print(randomList.count(5))

# sort
randomList = ["sfd", "adf", "uty", "qpr", "bwdf"]
randomList.sort()
print(randomList)
randomList.sort(reverse=True)
print(randomList)

# !!! List Comprehensions !!!
mylist = []
for i in range(10):
    mylist.append(i)
print(mylist)

print([i for i in range(5)])  # lambda
print([x for x in range(10) if x % 2 == 0])
print([x for x in range(5, 30, 3) if x % 2 == 0])
print([(x*2) for x in range(10)])
print(f"filtered:{[x for x in mylist if x % 2 == 0]}")
print(max(mylist))
print(f"mapped:{[(max(mylist))-x for x in mylist if x>5 and x<25]}")

# slicing
mylist = [x for x in range(20)]
# slicing start:end:step, end is exclusive
print(mylist[3:6])
print(mylist[3:15:2])
print(mylist[15:3:-2])
print(mylist[7:])
print(mylist[7::3])
print(mylist[:3])
