
#function that determines whether list contains the given value
def does_list_contain(list, value):
    does_contain = False
    for item in list:
        if item == value:
            does_contain = True
            break

#leaky stack of fixed length that "leaks" any data when it is pushed over its fixed length
class LeakyStackLinear:

    def __init__(self, length):
        self.data = [None] * length
        self.length = length

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.data == ([None] * self.length)

    def push(self, element):
        if self.data[self.length-1] == None: #if the stack is not full
            for index in range(self.length):
                if self.data[index] == None:
                    self.data[index] = element
                    break
        else: #if the stack is full, leak the bottom of the stack and add to the top
            self.data.pop(0)
            self.data.append(element)


    def top(self):
        top_value = None
        if self.is_empty():
            print('Stack is empty')
        elif self.data[self.length-1] == None: #if stack is not full
            for index in range(self.length):
                if self.data[index] == None:
                    top_value = self.data[index-1]
                    break
        else:
            top_value = self.data[self.length-1]
        return top_value


    def pop(self):
        popped_value = None
        #if self.is_empty():
            #print("stack is empty")
        if self.data[self.length-1] == None:
            for index in range(self.length):
                if self.data[index] == None:
                    popped_value = self.data[index-1]
                    self.data[index-1] = None
        else:
            popped_value = self.data[self.length-1]
            self.data[self.length-1] = None
        return popped_value

class LeakyStackCircular:

    def __init__(self, length):
        self.data = [None] * length
        self.length = length
        self._bottom = 0
        self._next = 0

    def __len__(self):
        return self.length

    def is_empty(self):
        return self.data == ([None] * self.length)

    def bottom(self):
        return self._bottom

    #pushes to the stack and leakes extra data
    def push(self, element):
        '''
        #if there is a None element, then you must fill in that None element and set the bottom to that
        if does_list_contain(self.data, None): #IDEA this is the line causing problems
            for index in range(self.length):
                if self.data[index] == None:
                    self.data[index] = element
                    break
        elif self._bottom != self.length-1:
            self.data[self._bottom] = element
            self._bottom += 1

        #resets the bottom back to the beginning of the circular list
        else:
            self.data[self._bottom] = element
            self._bottom = 0
        '''
        #print('next' + str(self._next))
        #print(str(self._next + 1) + ' % ' + str(len(self.data)) + ' = ' + str((self._next+1) % len(self.data)))
        self.data[self._next] = element
        self._next = (self._next+1) % len(self.data)
        #print(self._next)


    #returns the top element of the stack
    def top(self):
        return self.data[(self._next-1) % len(self.data)]

    #
    def pop(self):
        popped_value = self.top()
        self.data[(self._bottom-1) % len(self.data)] = None
        #readjust the bottom value to the right so that data pushes correctly
        self._bottom = (self._bottom-1) % len(self.data)
        return popped_value

print("Importing Libaries...")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import timeit
print("Libaries Imported")

#TESTING ZONE
stack_length = 100

circular_30_stack = LeakyStackCircular(stack_length)
linear_30_stack = LeakyStackLinear(stack_length)
testing_operations = 1000

times_linear = []
times_circular = []

'''
#testing push times
#populating stacks
for i in range(stack_length):
    circular_30_stack.push('Populating')
    linear_30_stack.push('Populating')


for i in range(testing_operations):
    start_time = timeit.default_timer()
    for j in range(i):
        linear_30_stack.push('Test Value')
    times_linear.append(timeit.default_timer() - start_time)
    #number_of_pushes_linear.append(i+1)

for i in range(testing_operations):
    start_time = timeit.default_timer()
    for j in range(i):
        circular_30_stack.push('Test Value')
    times_circular.append(timeit.default_timer() - start_time)

'''
'''
#testing top times
#populating stacks
for i in range(stack_length):
    circular_30_stack.push('Populating')
    linear_30_stack.push('Populating')

for i in range(testing_operations):
    start_time = timeit.default_timer()
    circular_30_stack.top()
    times_circular.append(timeit.default_timer() - start_time)

for i in range(testing_operations):
    start_time = timeit.default_timer()
    linear_30_stack.top()
    times_linear.append(timeit.default_timer() - start_time)
'''
'''
#testing pop times
#populating stacks 1.5x their length so that popping forces it to 'wrap around'
for i in range(stack_length + stack_length // 2 ):
    circular_30_stack.push('Populating')
    linear_30_stack.push('Populating')

for i in range(stack_length):
    start_time = timeit.default_timer()
    linear_30_stack.pop()
    times_linear.append(timeit.default_timer() - start_time)

for i in range(stack_length):
    start_time = timeit.default_timer()
    circular_30_stack.pop()
    times_circular.append(timeit.default_timer() - start_time)
'''

#testing push to fill an empty stack
for i in range(stack_length +  10 * stack_length //2):
    start_time = timeit.default_timer()
    linear_30_stack.push('Test Data')
    times_linear.append(timeit.default_timer() - start_time)

for i in range(stack_length + 10 *stack_length //2):
    start_time = timeit.default_timer()
    circular_30_stack.push('Test Data')
    times_circular.append(timeit.default_timer() - start_time)

plt.plot(times_linear, color = 'orange', label = 'Linear Implementation')
plt.plot(times_circular, color = 'purple', label = 'Circular Implementation')
linear_patch = mpatches.Patch(color='orange', label='Linear Implementation')
circular_patch = mpatches.Patch(color='purple', label='Circular Implementation')
plt.legend(handles=[linear_patch, circular_patch])
plt.ylabel('Time(s)')
plt.xlabel('Push Number')
plt.title('Time vs. Push Number | Stack Length = ' + str(stack_length))
plt.show()
