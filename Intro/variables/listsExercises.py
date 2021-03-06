# Create a list with the numbers 10 to 50
myList = [i for i in range(10, 51)]

# 01. Sum all of the elements in the list
sum = sum(myList)
print(sum)
# 02. Write a program that removes all duplicates from a list
myList = myList*2


def removeDup(dupList):
    for i in dupList:
        if dupList.count(i) > 1:
            dupList.remove(i)
            removeDup(dupList)
    return dupList

# [x for i,x in enumerate(myList) if myList.index(x)==i]


print(removeDup(myList))
# 03. Write a program that finds the intersection of two lists
testList1 = [1, 2, 3, 4, 3, 2, 1, 3, 4, 5]
testList2 = [1, 2, 2, 2, 2, 1]


def findInter(list1: list, list2: list, result=[]) -> list:
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result

# [x for i,x in enumerate(list1) if x in list2 and list1.index(x) == i]


print(findInter(testList1, testList2))
# 04. Write a program that finds the  union of two lists, omitting duplicates


def union(list1: list, list2: list) -> list:
    result = removeDup(list1+list2)
    result.sort()
    return result

# result =  list(set(list1+list2))


print(union(testList1, testList2))
# 05. Write a program that finds the differences of two lists
'''Method 1: works but kinda dumb
diff = []
    for i in list1:
        if i not in list2:
            diff.append(i)
    for j in list2:
        if j not in list1:
            diff.append(j)
    return removeDup(diff)
'''


def findDiff(list1: list, list2: list) -> list:
    result = union(list1, list2)
    inter = findInter(list1, list2, [])
    for i in inter:
        result.remove(i)
    return result


# list(set([x for x in (list1 + list2) if ((x not in list1) != (x not in list2))]))
# *!= is xor*
# or alternatively:
lista = testList1
listb = testList2
result = [x for i, x in enumerate(
    lista+listb) if ((x not in lista) != (x not in listb)) and (lista+listb).index(x) == i]

print(findDiff(testList1, testList2))
# 06. Write a program that creates a list containing the frequencies of elements in a list


def elementLister(list: list) -> dict:
    temp = list.copy()
    result = {}
    compare = removeDup(list)
    for i in compare:
        result[i] = temp.count(i)
    return result


print(elementLister(testList2))
# [(x,list1.count(x)) for i,x in enumerate(list1) if list1.index(x) == i]
