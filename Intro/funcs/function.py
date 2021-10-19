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

    def f(x:float, r:int,g:float):
        return (g ** r - x)/(r * g ** (r-1))
    # initial guess at an answer, there's more advanced way to choose this
    guess = 1
    prev = 0
    
    while abs(guess - prev) > precision:
        prev = guess
        guess -= f(num,root,guess)
    return guess

print(nthRoot(81,2))