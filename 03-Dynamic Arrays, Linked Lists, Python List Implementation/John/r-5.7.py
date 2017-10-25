#from problem r-5.7 in goodrich
#algorithm to find repeated integer

from random import randint

#generate array of integers from 1 on
def generateArray(length):
    array = []
    for i in range(1,length):
        array.append(i)
    return array

def insertRepeatedDigit(array):
    index = randint(0,len(array)-1)
    array.insert(index,array[index])

array = generateArray(10)
print(str(array))
insertRepeatedDigit(array)
print(str(array))


#my algorithm sums the array and subtracts the sum of the original array without a repeated digit
for i in range(2,10):
    array = generateArray(i)
    originalSum = sum(array)
    print(str(array))
    insertRepeatedDigit(array)
    newSum = sum(array)
    print(str(array))
    repeatedDigit = newSum - originalSum
    print(str(repeatedDigit))
