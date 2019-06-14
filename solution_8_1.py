""" A stack with a max API """

class Stack:
    def __init__(self):
        self._stack = []
        self._max_stack = []
    
    def push(self, item):
        self._stack.append(item)
        if self._max_stack:
            self._max_stack.append(max(self._max_stack[-1], item))
        else:
            self._max_stack.append(item)

    def pop(self):
        self._max_stack.pop()
        return self._stack.pop()
    
    def max(self):
        return self._max_stack[-1]
