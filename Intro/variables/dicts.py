myDict = {
    "Name": "Aaron Wang",
    "Class": 1101,
    "Age": 16
}

age = myDict["Age"]
print(age)

# dict doesn't store keys in any particular order
dictItems = myDict.items()
print(dictItems)

# interating over dict
for k, v in myDict.items():
    print(f"Key: {k}\tValue: {v}")

for k in myDict.keys():
    print(k, end=" ")

print()
for v in myDict.values():
    print(v, end=" ")
print()

print("Name" in myDict)
print("DNA" in myDict)

#Interests = myDict["Interests"]
#Not safe cuz things might not be there

name = myDict.get("Name")
print(name)
interests = myDict.get("Interests")
print(interests)

Class = myDict.pop("Class")
print(Class)
print(myDict)

something = myDict.popitem()
# pop out "some item" at the end of the stack, running the same thing on different COM may result in different stack order
print(something)
print(myDict)

myDict.clear()
print(myDict)

myDict["one"] = 1
myDict["two"] = 2
print(myDict)

del myDict["one"]
print(myDict)

myDict["method"] = lambda x: x*x
print(myDict.get("method")(10))


def myFunc(x):
    return x-5


myDict["method2"] = myFunc
print(myDict["method2"](10))
