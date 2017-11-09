# Array Pitfalls

arr = ['a', 'b', 'c', 'd']
print('Array 1', arr)

arr2 = arr
print('Array 2', arr2)

print('Deleting first item of arr1')
del arr[0]
print('Array 2', arr2)


# ^^^^
# arrays by reference
# arr and arr2 point hold references to the same values so deleting items in one array will effect the other