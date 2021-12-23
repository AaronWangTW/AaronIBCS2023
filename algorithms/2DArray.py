import sys


def minDiff(matrix: list[list[int]]) -> tuple:
    min = sys.maxsize
    index1 = (0, 0)
    index2 = (0, 0)
    for i in range(len(matrix)):  # range exclude last number, so actually just from 0 to 1
        for j in range(len(matrix[i])):
            if (i<len(matrix)-1):
                diff = abs(matrix[i+1][j]-matrix[i][j])  # Verticle Difference
                if diff < min:
                    min = diff
                    index1 = (i, j)
                    index2 = (i+1, j)
            if (j<len(matrix)-1):
                diff = abs(matrix[i][j+1]-matrix[i][j])
                if diff < min:
                    min = diff
                    index1 = (i, j)
                    index2 = (i, j+1)
    return (index1, index2)

def printResult(index1: tuple, index2:tuple, matrix:list[list[int]]) ->None:
    print(f"{index1}: {matrix[index1[0]][index1[1]]}")
    print(f"{index2}: {matrix[index2[0]][index2[1]]}")
    print(f"Difference: {abs(matrix[index1[0]][index1[1]]-matrix[index2[0]][index2[1]])}")

def main():
    data = [
        [-22, 12, -33],
        [33, 62, 21],
        [54, 22, 42]
    ]
    result = minDiff(data)
    printResult(result[0],result[1],data)


if __name__ == "__main__":
    main()
