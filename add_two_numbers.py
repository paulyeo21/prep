class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum = 0
        i = 0
        while l1:
            sum += l1.val * (10 ** i)
            l1 = l1.next
            i += 1

        i = 0
        while l2:
            sum += l2.val * (10 ** i)
            l2 = l2.next
            i += 1

        sum = str(sum)
        length = len(sum) - 1
        output = []
        while length >= 0:
            output.append(int(sum[length]))
            length -= 1
        
        return output
                    

solution = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(solution.addTwoNumbers(l1, l2))

l1 = ListNode(1)
l1.next = ListNode(8)

l2 = ListNode(0)

print(solution.addTwoNumbers(l1, l2))
