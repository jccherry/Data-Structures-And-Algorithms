#an implementation of Stacks in python using lists
#class slightly modified from page 233 of goodrich
class Stack:
    #LIFO Stack implementation using a Python list as underlying storage.”””
    def __init__ (self):

    #Create an empty stack.”””
        self.data = []
    # nonpublic list instance ”””Return the number of elements in the stack.”””

    def __len__(self):
        return len(self. data)

    def is_empty(self):
        #Return True if the stack is empty.”””
        return len(self. data) == 0

    def push(self, e):
        #Add element e to the top of the stack.”””
        self.data.append(e) # new item stored at end of list

    def top(self):
        #Return (but do not remove) the element at the top of the stack.
        #Raise Empty exception if the stack is empty. ”””
        if self.is_empty():
            raise Empty( Stack is empty )
        return self.data[len(self)-1]
# the last item in the list
    def pop(self):
       #Remove and return the element from the top of the stack (i.e., LIFO).
       #Raise Empty exception if the stack is empty. ”””
        if self.is_empty():
            raise Empty( Stack is empty )
        return self. data.pop( ) # remove last item from list


#using stacks to reverse a list
test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
stack = Stack()
stack.data = test_list
new_list = []
for i in range(len(stack)):
    new_list.append(stack.pop())
print(str(new_list))
