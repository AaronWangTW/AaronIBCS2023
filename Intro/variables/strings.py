import sys
from typing import Text

text1 = "I\'m String"
text2 = 'I, String'
text3 = """I am also a string but 
very wordy and long"""

#""" preserves spaces and linebreaks

print(text1, text2, text3)

text = "I'm a string. \nThis is a new line \n\tI am indented"
print(text)

text = "\"I\'m a quoted string\""
print(text)
print(""" ' "" ' """)  # not always necessary to use escape

# No escaping text
text = r"Special characters do nothing here\n\nSee? I do not change line"
print(text)

print(sys.getdefaultencoding())
# utf-8, international

# Unicode characters
text = "The circumference of a circle is 2 \u03c0r"
print(text)
print("\u265E,\N{GREEK CAPITAL LETTER DELTA}")

text = "I'm a long sentence that is unprecise and lack content, as well as being wordy and bs"
# Strings are immutable and treated like list
sub = text[10:]
print(sub)

text = "42"
number = text.isdigit()
letter = text.isalpha()  # if all alphabetical
print(f"is a number? {number}, is alphabetical? {letter}")
text = "測試"
letter = text.isalpha()
print(f"Is the letter alphabetic (or only characters?) ? {letter}")
text = "Hello"
startWithCapital = text.istitle()
print(f"Starts with a capital letter? {startWithCapital}")
text = "        \n\n\t\t\r\r"
space = text.isspace()
print(f"All white space ? {space}")

text = "blahblahblah why am I here"
length = len(text)
print(length)
countL = text.count("l")
print(countL)
print(text.title())
print(text.capitalize())
print(text.lower())
print(text.upper())
print(text.swapcase())

text = "I'm a bit shorter"
newText = text.center(30)
print(newText)
newText = text.rjust(30)
print(newText)

text = "The big blue bird is breaking the branch"
newText = text.replace("b", "r")
print(newText)
newText = text.replace("b", "r", 1)
print(newText)

words = text.split(" ")
print(words)
words = text.split("b")
print(words)

start = text.startswith("T")
print(start)
start = text.startswith("T", 5)
print(start)
start = text.startswith("T", 5, 10)
print(start)
end = text.endswith("h")
print(end)
loc = text.find("b")
print(loc)
loc = text.find("b", loc+1)
print(loc)
loc = text.rfind("b")
print(loc)
loc = text.find("z")
print(loc)

loc = text.find("b")
index = text.index("b")
print(loc,index)
loc = text.find("z")
try:
    index = text.index("z")
except ValueError:
    print("error")
print(loc)
# when not found, find return -1 but index return error

words = ["one","two","three"]
text = " ".join(words)
print(text)
print("\u265E".join(words))
print("\t".join(words))
print(" student ".join(words))