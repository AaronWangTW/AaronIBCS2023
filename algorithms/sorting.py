from typing import Counter
from searching import createRandomList


def bubbleSort(array: list) -> None:
    swapped = True
    count = 1
    while swapped:
        swapped = False
        for i in range(len(array)-count):
            if array[i+1] < array[i]:
                array[i+1], array[i] = array[i], array[i+1]
                swapped = True
        count += 1


def selectionSort(array: list) -> None:
    for i in range(len(array)-1):
        min = i
        for j in range(i, len(array)):
            if array[j] < array[min]:
                min = j
        if min != i:
            array[min], array[i] = array[i], array[min]

def insertionSort(array: list) -> None:
    pass


def mergeSort(array: list) -> None:
    pass


def main() -> None:
    data = createRandomList()
    print("original data:\n", data)
    print("correctly sorted data:\n", sorted(data))
    #bubbleSort(data)
    #print("bubble sort:\n",data)
    selectionSort(data)
    print("selection sort:\n", data)


if __name__ == "__main__":
    main()
