'''
R-6.5 Implement a function that reverses a list of elements by pushing them onto
a stack in one order, and writing them back to the list in reversed order.
'''

# STACK: LIFO

class MyStack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def top(self):
        self._data[len(self._data) - 1]

    def __len__(self):
        return len(self._data)

# -----------------------------------------

first_list = ['hello', ',', ' ', 'world', '!']
print("Starting list:", first_list)


S = MyStack()
for val in first_list:
    S.push(val)

reversed_list = [S.pop() for _ in range(len(S))]

print("Reversed list:", reversed_list)
