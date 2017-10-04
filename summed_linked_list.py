class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def summedLinkedList(self, list1, list2):
        if list1 and list2:
            new_list = Node(list1.value + list2.value)
            output = new_list
            current1, current2 = list1.next, list2.next
            while current1 and current2:
                new_list.next = Node(current1.value + current2.value)
                new_list = new_list.next
                current1, current2 = current1.next, current2.next
            return output

solution = Solution()
one = Node(1)
two = Node(2)
three = Node(3)
one.next = two
two.next = three

four = Node(4)
five = Node(5)
six = Node(6)
four.next = five
five.next = six

print(solution.summedLinkedList(one, four))

