### Solution for C-1.14

def productOdd(input):
    answer = False
    for number in input:
        if number % 2 == 1:
            return True
            break
    return answer

#print(productOdd([1, 2, 3, 4]))
#print(productOdd([2, 4]))
#print(productOdd([5, 2]))
