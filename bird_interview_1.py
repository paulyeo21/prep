# Stack class
# methods: push, pop, isEmpty, using a linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

# one = Node(1)
# two = Node(2)
# three = Node(3)

# one.next = two
# two.next = three

# one -> two -> three

class Stack:
    def __init__(self):
        self.current = None
        self.length = 0

    def push(self, value):
        element = self.toElement(value)

        if not self.current:
            self.current = element
        else:
            element.next = self.current
            self.current = element
        self.length += 1

    def pop(self):
        if not self.current:
            raise Exception('No elements in stack')
        output = self.current
        self.current = self.current.next
        self.length -= 1
        return self.toValue(output)

    def isEmpty(self):
        return self.length == 0

    def toElement(self, value):
        return Node(value)

    def toValue(self, elementObj):
        return elementObj.value

    def d_reversed(self):
        newStack = Stack()
        while not self.isEmpty():
            newStack.push(self.pop())
        return newStack

    def reversed(self):
        og_pointer = self.current
        new_pointer = self.current
        i = 0
        while og_pointer.next:
            if i == 3:
                break
            print('old')
            print(og_pointer)
            print('new')
            print(new_pointer)
            new_current = og_pointer.next
            new_current.next = new_pointer
            # move along stack
            og_pointer = og_pointer.next
            # move along new stack
            new_pointer = new_current
            i += 1

# stack = Stack()
# stack.push(1)
# stack.push(2)
# assert(stack.current.value == 2)
# assert(stack.pop() == 2)
# assert(stack.isEmpty() == False)
# assert(stack.pop() == 1)
# assert(stack.isEmpty() == True)
# stack.pop() # should raise exception when no elements

# should return stack obj but with reversed order elements, if stack is 1->2->3, then 3->2->1
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
# d_reversed = stack.d_reversed()
# assert(d_reversed.current.value == 1)
assert(stack.current.value == 3)
reversedStack = stack.reversed()
assert(reversedStack.current.value == 1)

