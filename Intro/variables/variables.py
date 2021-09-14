# Python is dynamically typed

# int
myvar = 7
print(myvar, type(myvar))

# float
myvar = 7.3
print(myvar, type(myvar))

# String
myvar = "Text"
print(myvar, type(myvar))

myvar = "I\'m another string"
print(myvar)

myvar = """
very long stuff
be aware
new lines and spaces are perserved
"""
print(myvar)

a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b)

# Some OPERATORS are overloaded
# e.g. this is int addition cuz it recognizes it
a, b = 4, 6
result = a+b
print(result)

# this will be float addition
a, b = 4, 6.8
result = a + b
print(result)

# python doesn't allow string + other type
a, b = "number", str(5)
result = a+b
print(result)
result = f"{a}{b}"
print(result)

a, b = 4, 3
print(float(a)+b)
