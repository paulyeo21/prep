# 2. Add Two Numbers
#
# You are given two non-empty linked lists representing two non-negative integers. The digits 
# are stored in reverse order and each of their nodes contain a single digit. Add the two numbers 
# and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Get the numbers from the linked list and get their sum. Create a linked list using the sum.
# T: O(n)
# S: O(n)
def add_two_numbers(l1, l2)
  first = 0
  i = 1
  while l1
    first = first + l1.val * i
    l1 = l1.next
    i *= 10
  end
  second = 0
  i = 1
  while l2
    second = second + l2.val * i
    l2 = l2.next
    i *= 10
  end
  sum = first + second

  # create linked list from sum
  previous = ListNode.new(sum % 10)
  head = previous
  sum = sum / 10
  while sum != 0
    current = ListNode.new(sum % 10)
    previous.next = current
    sum = sum / 10
    previous = current
  end
  return head
end
