def myFunc():
    print("I, func")


myFunc()


def area(w: float, h: float) -> float:
    """this function returns the area of a rectangle based on inputted height and width
    
    Attributes
        w: width of the rectangle
        h: height of he rectangle
    """
    return w*h


print(area(3, 5))


def increment(x: int) -> None:
    x += 1


x = 5
increment(x)
print(x)
# x didn't change
# passed by value


def incrementList(x: list) -> None:
    x[0] += 1


x = [5]
incrementList(x)
print(x)
# x increased
# passed by reference


def nthRoot(num: float, root: int, precision: float = 1e-20) -> float:
    if (num < 0 and root % 2 == 0):
        raise ValueError(f"No even roots of negative numbers: number={num}")
    if root < 0:
        raise ValueError(f"No negative roots: root={root}")
    if num == 0:
        return 0
    if root == 0:
        return 1
    if root == 1:
        return num

    def f(x: float, r: int, g: float):
        return (g ** r - x)/(r * g ** (r-1))
    # initial guess at an answer, there's more advanced way to choose this
    guess = 1
    prev = 0

    while abs(guess - prev) > precision:
        prev = guess
        guess -= f(num, root, guess)
    return guess


print(nthRoot(81, 2))
print(nthRoot(root=2, num=4))

# In python, functions are first-class members
myvar = nthRoot
print(myvar(64, 2))

#Call back functions, functions that accept function as input


def evenHandler(val: int) -> bool:
    print(f"{val} is divisible by 2")


def oddHandler(val: int) -> bool:
    val = val+1
    print(f"Value is now {val}. Much better.")


def doThing(evenCallback, oddCallback) -> None:
    for i in range(20):
        if i % 2 == 0:
            evenCallback(i)
        else:
            oddCallback(i)

#doThing(evenHandler,oddHandler)

# Generator
# yield, basically return but iterable and temporarily stopped. Without iterating on it, it won't return value
# use next() to get value from it since it returns a generator object


def squares():
    n = 1
    while True:
        yield n ** 2
        n += 1


val = squares()
collect = []
print(type(val))
for i in range(5):
    collect += [next(val)]

for i in range(7):
    collect += [next(val)]
print(collect)
# the iteration continues


def fibonacciNumberse(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x


numberse1 = fibonacciNumberse(10)
collect = []
for i in range(10):
    collect += [next(numberse1)]
print(collect)
# generator is memory efficient because it doesn't store all of the variables and used variable