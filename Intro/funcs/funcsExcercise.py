# 1. Calculate Factorial
def factorial(num: int) -> int:
    result = num
    if num > 0:
        for i in range(1, num):
            result *= i
        return result
    elif num == 0:
        return 1
    return -1 


print(factorial(5))

# 2. Calculate Permutation
# n! / (n-r)!
# nPr(10,10) -> 3628800


def nPr(n: int, r: int) -> int:
    return int(factorial(n) / factorial(n-r))


print(nPr(3, 2))

# 3. Calculate Combination
# n! / (r!(n-r)!)
# nCr(10,10) -> 1


def nCr(n: int, r: int) -> int:
    return int(factorial(n)/(factorial(r)*factorial(n-r)))


print(nCr(10, 10))

# pascalsTriangle(rows)
# pascalsTriangle(3) -> [[1],[1,1][1,2,1]]


def pascalsTriangle(row: int) -> list:
    layer = [1]
    result = [[1]]
    for _ in range(row):
        temp = []
        for j in range(len(layer)):
            if j == 0:
                temp += [1]
            else:
                temp += [layer[j]+layer[j-1]]
        temp += [1]
        layer = temp.copy()
        result.append(temp)
    return result


print(pascalsTriangle(3))


# Generator func with star
# starGen()
# *
# **
# ***
def starGen():
    i = 1
    while True:
        yield i*"*"
        i += 1


stars = starGen()
collect = []
for i in range(5):
    collect += [next(stars)]
print(collect)


# PrimeNumberGenerator
# Seive of eratosthenes
def primeNumGen():
    past = []
    i = 2
    while True:
        isPrime = True
        for j in past:
            if i % j == 0:
                isPrime = False
        if isPrime:
            past += [i]
            yield i
        i += 1


prime = primeNumGen()
collect = []
for i in range(5):
    collect += [next(prime)]
print(collect)


# Pascal Triangle, but Generator, returns next row each time
def pascalTriangleGen(row: int) -> list:
    layer = [1]
    yield layer
    for _ in range(row):
        temp = []
        for j in range(len(layer)):
            if j == 0:
                temp += [1]
            else:
                temp += [layer[j]+layer[j-1]]
        temp += [1]
        layer = temp.copy()
        yield temp


triangle = pascalTriangleGen(5)
collect = []
for i in range(5):
    collect.append(next(triangle))
print(collect)
