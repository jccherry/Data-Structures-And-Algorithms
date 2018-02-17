import time

def factorial_recursive(n):

    if n < 0:
        return 'ERROR'
    elif n == 1 or n == 0:
        return 1
    else:
        return n*factorial_recursive(n-1)

def factorial_iterative(n):

    if n < 0:
        return 'ERROR'
    if n == 0:
        return 1
    else:
        for i in range(1,n):
            n = n*i
        return n

#998 is the max recursion depth in python 3 that ive been able to test


start_time_recursive = time.time()

for i in range(0,998):
    factorial_recursive(998)

end_time_recursive = time.time()
print('Recursive: ' + str(end_time_recursive - start_time_recursive) + ' sec')



start_time_iterative = time.time()

for i in range(0,998):
    factorial_iterative(998)

end_time_iterative = time.time()
print('Iterative: ' + str(end_time_iterative - start_time_iterative) + ' sec')

print(factorial_iterative(20))
print(factorial_recursive(20))
