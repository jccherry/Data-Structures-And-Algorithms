#binary tree implementation
#stores integers and compares against one another to see where they should be stored most efficiently

#some code from https://www.youtube.com/watch?v=jJO0MbwF5OI but modified to fit my needs

#simple node that stores an integer
class Node:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def is_full(self):
        if self.left_node != None and self.right_node != None:
            return True
        else:
            return False

    def height(self):
        if not is_full(self):
            return 0
        else:
            return max(height(self.left_node),height(self.right_node)) + 1

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)


    def _add(self, val, node):
        if(val < node.value):
            if(node.left_node != None):

                self._add(val, node.left_node)
            else:
                node.left_node = Node(val)

        else:
            if(node.right_node != None):
                self._add(val, node.right_node)
            else:
                node.right_node = Node(val)

    def PrintTree(self):
        if(self.root != None):
            self._PrintTree(self.root)

    def _PrintTree(self, node):
        if(node != None):
            self._PrintTree(node.left_node)
            print(str(node.value) + ' ')
            self._PrintTree(node.right_node)

    def DeleteTree(self):
        self.root = None



#-----------------------------------------------------------------
tree = BinaryTree()
for i in range(0,20):
    if i % 2 == 0:
        tree.add(i*i)
    else:
        tree.add(i)

tree.PrintTree()
tree.DeleteTree()
print('deleted')
tree.PrintTree()
