'''
C-5.14 The shuffle method, supported by the random module, takes a Python
list and rearranges it so that every possible ordering is equally likely.
Implement your own version of such a function. You may rely on the
randrange(n) function of the random module, which returns a random
number between 0 and n − 1 inclusive.
'''
import random

my_list = [random.randrange(1, 100) for _ in range(10)] # _ denotes a temporary, unused variable
print("Original list:", my_list)

# random.shuffle(my_list)
# print(my_list)

# Recursively find a random index of the shuffled list that is None
def get_none_index(shuffled, exlcude_indices=[]):
    rand_index = random.randrange(len(shuffled))
    return rand_index if shuffled[rand_index] is None else get_none_index(shuffled, exlcude_indices+[rand_index])

def my_shuffle(l):
    shuffled = [None for _ in range(len(l))]

    # Loop through given list and assign each value to a random place in shuffled
    for val in l:
        index = get_none_index(shuffled)
        shuffled[index] = val

    return shuffled

print("Shuffled list:", my_shuffle(my_list))
