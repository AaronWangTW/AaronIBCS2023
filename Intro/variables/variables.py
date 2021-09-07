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
