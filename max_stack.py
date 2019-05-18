class MaxStack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.maxes = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)
        if not self.maxes or \
                self.maxes[len(self.maxes)-1] <= item:
            self.maxes.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        popped = self.items.pop()

        if self.maxes[len(self.maxes)-1] == popped:
            self.maxes.pop()

        return popped

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
        """Return the largest element in the stack without removing it"""
        if not self.maxes:
            return None

        return self.maxes[len(self.maxes)-1]

stack = MaxStack()
stack.push(5)
print stack.get_max() #5
stack.pop()
stack.push(4)
print stack.get_max() #4
stack.push(6)
print stack.get_max() #6
stack.push(6)
stack.pop()
print stack.get_max() #6
stack.pop()
print stack.get_max() #4
