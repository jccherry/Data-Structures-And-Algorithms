#!/usr/bin/env python3

'''
P-7.44 Write a simple text editor that stores and displays a string of characters
using the positional list ADT, together with a cursor object that highlights
a position in this string. A simple interface is to print the string and then
to use a second line of output to underline the position of the cursor. Your
editor should support the following operations:
• left: Move cursor left one character (do nothing if at beginning).
• right: Move cursor right one character (do nothing if at end).
• insert c: Insert the character c just after the cursor.
• delete: Delete the character just after the cursor (do nothing at end).
'''

class TextEditor:
    # Doubly Linked List
    class PositionalList:

        class _Node:
            __slots__ = '_element', '_prev', '_next'

            def __init__(self, element, prev, next):
                self._element = element
                self._prev = prev
                self._next = next
        # -----------------------------

        class Position:
            def __init__(self, container, node):
                self._container = container # To know what list it belongs to
                self._node = node

            def element(self):
                return self._node._element

            def __eq__(self, other): # Used when doing == 
                return type(other) is type(self) and other._node is self._node

            def __ne__(self, other):
                return not (self == other) # Refers to above
        # -----------------------------

        def __init__(self):
            self._head = self._Node(None, None, None) # _head and _end are always empty placeholders
            self._end = self._Node(None, None, None)

            self._head._next = self._end
            self._end._prev = self._head

            self._length = 0

            # Print controls
            print("[SIMPLE TEXT EDITOR]")
            print("Commands:")
            print(":left")
            print(":right")
            print(":insert c")
            print(":delete")
            print()

        # DOUBLY LINKED LIST METHODS
        def _insert_between(self, e, prev, next):
            new = self._Node(e, prev, next)
            prev._next = new
            next._prev = new

            self._length += 1
            return self._make_position(new)

        def _delete_node(self, node):
            prev = node._prev
            next = node._next

            prev._next = next
            next._prev = prev

            self._length -= 1

            element = node._element
            node._prev = node._next = node._element = None # Removes all references
            return element
        # --------------------------

        def _make_position(self, node):
            if node is self._head or node is self._end:
                return None
            else:
                return self.Position(self, node)
        
        # Make sure position is a valid one
        def _validate(self, p):
            if not isinstance(p, self.Position):
                raise TypeError("Must pass position type.")
            if p._container is not self:
                raise ValueError("Position must belong to this list.")
            if p._node._next is None:
                raise ValueError("Position is not valid.")
            return p._node

        def first(self):
            return self._make_position(self._head._next)

        def last(self):
            return self._make_position(self._end._prev)

        def before(self, p):
            node = self._validate(p)
            return self._make_position(node._prev)

        def after(self, p):
            node = self._validate(p)
            return self._make_position(node._next)

        # Adding an element makes it the new head
        def add_first(self, e):
            return self._insert_between(e, self._head, self._head._next)

        def add_last(self, e):
            return self._insert_between(e, self._end._prev, self._end)

        def add_before(self, p, e):
            original = self._validate(p)
            return self._insert_between(e, original._prev, original)

        def add_after(self, p, e):
            original = self._validate(p)
            return self._insert_between(e, original, original._next)

        # Delete a node by removing references next to it on both sides
        def delete(self, p):
            original = self._validate(p)
            self._delete_node(original)

        def replace(self, p, e):
            original = self._validate(p)
            old_value = original._element
            original._element = e
            return old_value

        def is_empty(self):
            return self._length == 0 # This uses self.__len__

        def __len__(self):
            return self._length

        def __iter__(self):
            cursor = self.first()
            while cursor is not None:
                yield cursor
                cursor = self.after(cursor)

    # TEXT EDITOR COMMANDS

    def __init__(self):
        self._list = self.PositionalList()
        self.cursor = self._list.first()

    def left(self):
        if self.cursor == self._list.first():
            return
        self.cursor = self._list.before(self.cursor)

    def right(self):
        if self.cursor == self._list.last():
            return
        self.cursor = self._list.after(self.cursor)

    def insert(self, c):
        if self._list.is_empty():
            self.cursor = self._list.add_first(c)
        else:
            self._list.add_after(self.cursor, c)

    def delete(self):
        if self.cursor == self._list.first():
            self._list.delete(self.cursor)
            self.cursor = self._list.first()
        elif self.cursor == self._list.last():
            return
        else:
            self._list.delete(self.cursor)

    def print(self):
        # If empty, just skip
        if self._list.is_empty():
            return
            
        # First print characters
        for p in self._list:
            print(p.element(), end='')
        print()

        # Then print where cursor is
        for p in self._list:
            print('^' if p == self.cursor else ' ', end='')
        print()

# TESTING
if __name__ == '__main__':
    t = TextEditor()
    while True:
        parts = input(':').split(' ')
        command = parts[0].lower()

        if command == 'left':
            t.left()
        elif command == 'right':
            t.right()
        elif command == 'insert':
            arg = parts[1]
            t.insert(arg[0])
        elif command == 'delete':
            t.delete()
        t.print()
