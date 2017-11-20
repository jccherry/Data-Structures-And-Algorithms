# John's First Trimester Project

## Introdution
I decided, because I lack the background in recursion (as of now. I will study recursion first thing in the second trimester) necessary to implement trees effectively, that I would undertake a problem from Chapter 6, but I modified the prompt slightly to experiment.  The Original Prompt states:

```
The introduction of Section 6.1 notes that stacks are often used to provide “undo” support in applications like a Web browser or text editor. While support for undo can be implemented with an unbounded stack, many applications provide only limited support for such an undo history, with a fixed-capacity stack. When push is invoked with the stack at full capacity, rather than throwing a Full exception (as described in Exercise C-6.16), a more typical semantic is to accept the pushed element at the top while “leaking” the oldest element from the bottom of the stack to make room. Give an implementation of such a LeakyStack abstraction, using a circular array with appropriate storage capacity.
```

I found myself questioning the efficiency of the 'circular' design of the array in the prompt, so I decided to build two classes for the LeakyStack abstraction and test their efficiency against one another. One is designed linearly,```LeakyStackLinear```, where instead of going back to the beginning of the list, the first entry is popped off and the new entry is appended to the end when pushing.  The other is designed circularly,```LeakyStackCircular```, where the size and position in memory of the data list is not changed, but entries are changed and there is a changing `bottom` value to indicate what index of the data list to pop and push to.

Each class has a series of functions indicative of a stack, but the only added difference is the 'Leaky' functionality due to the fixed size of the data stack:

```
	push(self, element):
		#pushes a new element to the top of the stack, and if the stack is full, 'Leaks' the oldest data
	top(self):
		#returns the most recent push to the stack without removing it from the stack
    pop(self):
    	#returns the most recent push to the stack and removes it from the stack
```
I want to test the efficiency of these three functions for each of the class and compare them to one another


## Hypothesis
Pushing to the linear array will be far less efficient overall, because any push to the stack when it is full invokes the line ```self.data.pop(0)```, which takes O(n) time (where n is the length of the data list in the stack) whereas the circular design will take O(2) time because it only has to reassign the value at the top of the stack and change the index variable ```bottom```

Because finding the 'top' value of the data list should be theoretically done in O(1) time, this should be either equal and constant for both classes, or more efficient for the circular design because the linear design needs to account for the ```None``` objects if the stack is not full and loops in O(n-1) worst case time (where n is the length of the data list in the stack).

Popping the top value of the stack should again be more efficient with the circular design, taking O(3) time where the linear algorithm takes O(n-1) worst-case time when the stack is one away from being full and O(n-k) on average, where k is the amount of ```None``` objects in the data list.  If both stacks are full, they should each take the same amount of time, O(3)

## Testing Methodology
Because of the nature of the 'Undo' as presented in the prompt, it is most applicable to test a fixed, reasonable length.  I chose 30 (except where longer lengths are explicitly stated)