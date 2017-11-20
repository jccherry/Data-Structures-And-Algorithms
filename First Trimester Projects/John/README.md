# John's First Trimester Project

## Introdution
I decided, because I lack the background in recursion (as of now. I will study recursion first thing in the second trimester) necessary to implement trees effectively, that I would undertake a problem from Chapter 6, but I modified the prompt slightly to experiment.  The Original Prompt states:


"The introduction of Section 6.1 notes that stacks are often used to provide “undo” support in applications like a Web browser or text editor. While support for undo can be implemented with an unbounded stack, many applications provide only limited support for such an undo history, with a fixed-capacity stack. When push is invoked with the stack at full capacity, rather than throwing a Full exception (as described in Exercise C-6.16), a more typical semantic is to accept the pushed element at the top while “leaking” the oldest element from the bottom of the stack to make room. Give an implementation of such a LeakyStack abstraction, using a circular array with appropriate storage capacity."


I found myself questioning the efficiency of the 'circular' design of the array in the prompt, so I decided to build two classes for the LeakyStack abstraction and test their efficiency against one another. One is designed linearly,```LeakyStackLinear```, where instead of going back to the beginning of the list, the first entry is popped off and the new entry is appended to the end when pushing.  The other is designed circularly,```LeakyStackCircular```, where the size and position in memory of the data list is not changed, but entries are changed and there is a changing `bottom` value to indicate what index of the data list to pop and push to.

Each class has a series of functions indicative of a stack, but the only added difference is the 'Leaky' functionality due to the fixed size of the data stack:

```python
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

## Testing and Methodology
For testing the efficiency of the ```push``` function, I first populated a stack fully to take away the error caused from filling an empty stack.  Next, i crafted two identical loops to push an identical object ```n``` times, each time increasing ```n``` to a total of 1000 timed trials.  I also tested the time it takes to fill an entire empty stack, and the following pushes after the stack is full

<img src="https://raw.githubusercontent.com/jccherry/Data-Structures-And-Algorithms/master/First%20Trimester%20Projects/John/Pictures/time_vs_push.png" width="45%"><img src="https://raw.githubusercontent.com/jccherry/Data-Structures-And-Algorithms/master/First%20Trimester%20Projects/John/Pictures/time_vs_push_zoomed.png" width="45%"><img src="https://raw.githubusercontent.com/jccherry/Data-Structures-And-Algorithms/master/First%20Trimester%20Projects/John/Pictures/full_push.png" width="45%">

For testing the efficiency of the ```pop``` function, I proceeded a bit differently.  First, I pushed to the stacks to 1.5x their length, so that they would have to 'loop back around.'  Next, I crafted two identical loops to ```pop``` the entirety of the stack, recording the time between each ```pop``` for a total number of 'trials' equal to that of the length of the stack.

<img src="https://raw.githubusercontent.com/jccherry/Data-Structures-And-Algorithms/master/First%20Trimester%20Projects/John/Pictures/time_vs_pop.png" width="45%"><img src="https://raw.githubusercontent.com/jccherry/Data-Structures-And-Algorithms/master/First%20Trimester%20Projects/John/Pictures/time_vs_pop_100.png" width="45%">

For testing the efficiency of the ```top``` function, I knew that it should theoretically be the same every time, so i proceeded to run the exact same trial of ```stack.top()``` for a total of 1000 trials to observe any possible differences.

<img src="https://raw.githubusercontent.com/jccherry/Data-Structures-And-Algorithms/master/First%20Trimester%20Projects/John/Pictures/time_vs_top_trials.png" width="65%">

## Discussion
My prediction for pushing to the stack was accurate, showing that there is a linear relationship between number of pushes (which should be a constant value) and time.  While there is obvious noise in the two graphs, the linear "bottom" is evident, and it can be seen that the slope of the circular implementation is lower than the slope of the linear implementation, showing that it will always be more efficient when pushing data to the stack.  The graph that depicts filling of an empty stack, with Push number vs Time, shows an always constant value for the circular implementation, but a high slope value for the linear implementation up until the stack is full, because the linear implementation always calls this lock of code if the stack is not full:
```python
for index in range(self.length):
	if self.data[index] == None:
        	self.data[index] = element
        	break
```
Even though the Linear Implementation is less efficient, a perhaps more efficient way to get around this behaviour would be to implement some sort of index variable instead of looping through each entry.

The prediction for the efficiency of the ```top``` function was mostly correct, but the Circular implementation was suprisingly more than twice as efficient than the linear implementation.  This is, of course, in fractions of fractions of fractions of seconds to the point where it is wholly insignificant.


