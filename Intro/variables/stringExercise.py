# 1 Write a Python program to count and return a dict of character frequencies in a given string\
# e.g. func("hi") -> {'h':1,'i':1}
def listChars(string: str):
    result = {}
    chars = [(x, string.count(x))
             for i, x in enumerate(string) if string.index(x) == i]
    for c, i in chars:
        result[c] = i
    return result


print(listChars("google"))
# 2 Write a Python function to insert a string in the middle of a string
# e.g.
# func("{{}}", "PHP")-> "{{PHP}}"


def insertMiddle(cover: str, content: str):
    return(cover[:len(cover)//2]+content+cover[len(cover)//2:])


print(insertMiddle("{{}}", "Python"))
print(insertMiddle("|||", "Hello"))
# 3 Write a Python program to display a number with a comma separator
# e.g. func("11023") -> "11,023"

######## UNFINISHED, HAVE PROBLEMS


def addSeperator(string: str):
    result = ""
    last = len(string)
    if string.isdigit():
        for i in range(len(string), -1, -1):
            if (i) % 3 == 0:
                result = ","+string[i:last]+result
                last = i
        return result
    return False


print(addSeperator("2342343411022"))
#4 Write a Python program to move spaces to the front of a given string
# e.g. func("hi hi hi hi")-> "   hihihihi"


def moveSpace(string: str):
    result = string
    count = result.count(" ")
    result = result.replace(" ", "")
    return((" "*count)+result)


print(moveSpace("hi hi hi hi"))
# 5 Write a Python program to compute sum of digits of a given number string


def stringNumSum(string: str):
    sum = 0
    if string.isdigit():
        for i in range(len(string)):
            sum = sum+int(string[i])
        return sum
    return False


print(stringNumSum("12345"))
# 6 Write a Python program to dtermine if a set of parenthesis are balanced, so (()), no )() or (()
