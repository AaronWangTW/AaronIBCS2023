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


def addSeperator(string: str, divider:int=3, seperator:str=","):
    result = ""
    for c, i in enumerate(reversed(string)):
        if (c+1) % divider == 0:
            result = seperator+i+result
        else:
            result = i+result
    if result[0] == seperator:
        result = result[1:]
    return result


print(addSeperator("222222342343411022",3,"."))
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


def brackletCheck(string: str):
    result = ""
    for i in string:
        if i == "(":
            result += "("
        if i == ")":
            result += ")"
        result = result.replace("()", "")
    if len(result) == 0:
        return True
    return False


print(brackletCheck(")((aaaaaaaaaaaaaaaaa))(asdflkasjdofjaosdjfo)()"))
