'''
C-5.22 Develop an experiment to compare the relative efficiency of the extend
method of Python’s list class versus using repeated calls to append to
accomplish the equivalent task.
'''

# list.append(item) adds an object to the end of a list; if given a list it will add the list itself as an item
# list.extend([items]) similarly adds objects to the end of a list but when passed an list unpacks it and adds each one 

import matplotlib.pyplot as plt

import random
import timeit

# Items that will be added to empty list
to_add = [None for _ in range(1000)]

a = []
e = []

append_times = []
extend_times = []

def run():
    start = timeit.default_timer()
    for val in to_add:
        a.append(val)
    append_times.append(timeit.default_timer() - start)

    start = timeit.default_timer()
    e.extend(to_add)
    extend_times.append(timeit.default_timer() - start)


for _ in range(500):
    print("Run")
    run()

plt.plot(append_times, color = 'orange', label = 'Append')
plt.plot(extend_times, color = 'purple', label = 'Extend')
plt.ylabel('Time')
plt.xlabel('Run #')

plt.legend()
plt.show()

'''
Extend clear performs much better than appending each item individually.
'''