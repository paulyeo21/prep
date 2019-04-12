# 25. Reverse Nodes in k-Group
#
# Given a linked list, reverse the nodes of a linked list k at a time and return 
# its modified list. k is a positive integer and is less than or equal to the length 
# of the linked list. If the number of nodes is not a multiple of k then left-out 
# nodes in the end should remain as it is.
#
# Example:
# Given this linked list: 1->2->3->4->5
# For k = 2, you should return: 2->1->4->3->5
# For k = 3, you should return: 3->2->1->4->5
#
# Note:
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# First to reverse a linked list we need to set a head and as we traverse
# the linked list attach the head to the current node while setting the head's
# next node as the current node's next.
def reverse(head)
  _head, a, b = ListNode.new(nil), head, head.next
  _head.next = a
  while b
    # remove b from tail
    a.next = b.next
    # set new tail
    tail = _head.next
    _head.next = b
    b.next = tail
    # a is where b was before
    b = a.next
  end
  return _head.next
end

# Given k, we want to reverse every kth node. For instance if k = 2 and we have 1->2->3->4->5,
# then we reverse 1->2 which yields 2->1->3->4->5, then reverse 3->4, 2->1->4->3->5. 
# T: O(n)
# S: O(n)
def reverse_k_group(head, k)
  return nil if not head
  return head if k == 1
  # find number of reverses to do by length / k
  copy = head
  length = 0
  while copy
    copy = copy.next
    length += 1
  end
  num_reverses = length / k
  # reverse num_reverses times for k nodes at a time
  _head, a, b = ListNode.new(nil), head, head.next
  _head.next = a
  output = _head
  while num_reverses > 0
    copy = k
    while copy - 1 > 0
      # reverse
      a.next = b.next
      tail = _head.next
      _head.next = b
      b.next = tail
      b = a.next
      copy -= 1
    end
    if b
      _head = a
      a = a.next
      b = b.next
    else
      break
    end
    num_reverses -= 1
  end
  return output.next
end

head = ListNode.new(1)
two = ListNode.new(2)
three = ListNode.new(3)
four = ListNode.new(4)
five = ListNode.new(5)
head.next = two
two.next = three
three.next = four
four.next = five

b = ListNode.new(1)
two = ListNode.new(2)
b.next = two

# puts reverse_k_group(head, 2).inspect
# puts reverse_k_group(head, 1).inspect
puts reverse_k_group(b, 2).inspect
