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
    # start at [1]
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        # while we find values greater than key, swap j and j+!
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


def merge(array: list, left: int, mid: int, right: int):
    i = left
    j = mid+1
    k = 0
    temp = [0]*(right-left+1)
    while i <= mid and j <= right:
        if array[i] < array[j]:
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = array[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = array[j]
        j += 1
        k += 1
    # copy temp to original array
    k=0
    while left+k <=right:
        array[left+k]=temp[k]
        k+=1


def mergeSort(array: list, left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(array)-1
    if right <= left:
        return
    mid = (right+left)//2
    mergeSort(array, left, mid)
    mergeSort(array, mid+1, right)
    merge(array, left, mid, right)


def main() -> None:
    data = createRandomList()
    print("original data:\n", data)
    print("correctly sorted data:\n", sorted(data))
    # bubbleSort(data)
    # print("bubble sort:\n",data)
    # selectionSort(data)
    # print("selection sort:\n", data)
    # insertionSort(data)
    # print("insertion sort:\n", data)
    mergeSort(data)
    print("merge sort:\n", data)


if __name__ == "__main__":
    main()
