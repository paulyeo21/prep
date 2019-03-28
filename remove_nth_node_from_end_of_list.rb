# 19. Remove Nth Node From End of List
#
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
# Could you do this in one pass?

class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# Have two pointers traverse the linked list one following another
# n places behind the other. When the first pointer reaches the end,
# then the second pointer will be at n-th node from end. Remove that node
# and return the head. Note: need to place fast pointer n+1 in front so that
# slow pointer can remove the n-th node by doing a node.next = node.next.next.
# T: O(n)
# S: O(n)
def remove_nth_from_end(head, n)
  fast = slow = head
  # traverse p n spots forward from trailing_p
  (1..n).each {|i| fast = fast.next}
  # traverse p and trailing_p until p reaches end 
  return slow.next if not fast
  while fast.next
    fast = fast.next
    slow = slow.next
  end
  # when p reaches end remove node that trailing_p is at
  slow.next = slow.next.next
  return head
end

one = ListNode.new(1)
two = ListNode.new(2)
three = ListNode.new(3)
four = ListNode.new(4)
five = ListNode.new(5)
one.next = two
two.next = three
three.next = four
four.next = five

puts remove_nth_from_end(one, 2).inspect # [1,2,3,5]
puts remove_nth_from_end(ListNode.new(1), 1).inspect # []
