import timeit

# This is an abitrary method that will take a long time
def take_time():
  return map(lambda n: n^20, range(100)) # Using anonymous functions (lambdas) for clarity

# timeit.timeit(func) will return the number of seconds a function takes to run
print('Starting...')
time = timeit.timeit(take_time) # This could also be written as timeit.timeit('map(lambda x: x^2, range(10))')


print('The take_time() method took', time, 'seconds to run.')

# We can use this to test our own algorithms in terms of speed to compare them to each other

# More info can be found at http://pythoncentral.io/time-a-python-function/ where I got the examples I used
