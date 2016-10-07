class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sum = l1.val + l2.val
        i = 1
        while l1.next:
            l1 = l1.next
            l2 = l2.next
            sum += (l1.val + l2.val) * (10**i)
            i += 1

        # length = len(sum) - 1
        # head = ListNode(sum[length])
        # current = head
        # length -= 1
        # while length >= 0:
        #     digit = sum[length]
        #     current.next = ListNode(digit)
        #     current = current.next

        # return head

solution = Solution()

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(solution.addTwoNumbers(l1, l2))
