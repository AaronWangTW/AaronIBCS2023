import random


def sequentialSearch(value: int, array: list) -> int:
    for idx, val in enumerate(array):
        if val == value:
            return idx
    return None


def binarySearch(value: int, array: list, start: int, end: int) -> int:
    if end is None:
        end = len(array) - 1
    mid = start + (end-start) // 2
    if end >= start:
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            return binarySearch(value, array, start=mid+1, end=end)
        else:
            return binarySearch(value, array, start=start, end=mid-1)


def createRandomList(min: int = 0, max: int = 100, size: int = 50):
    data = []
    for i in range(size):
        data.append(random.randint(min, max))
    return data


def testSequentialSearch(value: int, array: list):
    idx = sequentialSearch(value, array)
    if idx == None:
        print(f"Did not find {value}")
    else:
        print(f"{value} found at index {idx}")

def testBinarySearch(value:int,array:list):
    array.sort()
    idx = binarySearch(value, array,0,len(array)-1)
    if idx == None:
        print(f"Did not find {value}")
    else:
        print(f"{value} found at index {idx} of sorted array")

def main():
    data = createRandomList(55, 110, 50)
    value = 73
    #data.sort()
    print(data)
    testSequentialSearch(value, data)
    testBinarySearch(value,data)


if __name__ == "__main__":
    main()
