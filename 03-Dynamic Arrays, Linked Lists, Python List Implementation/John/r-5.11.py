#problem r-5.11 in goodrich
from random import randint


def generateNXNMatrix(n):
    matrix = []
    for i in range(n):
        matrix.append([])
    for row in matrix:
        for i in range(n):
            row.append(randint(0,9))
    return matrix

def nXnMatrixSum(matrix):
    sumVal = 0
    for row in matrix:
        sumVal += sum(row)
    return sumVal


for i in range(0,10):
    matrix = generateNXNMatrix(i)
    print(str(matrix))
    print(str(nXnMatrixSum(matrix)))

#confirmed working
