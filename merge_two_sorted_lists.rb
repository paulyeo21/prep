# 21. Merge Two Sorted Lists
#
# Merge two sorted linked lists and return it as a new list. The new list 
# should be made by splicing together the nodes of the first two lists.
#
# Example:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# Have a new pointer that is appended to as you walk through the
# two input linked lists one by one and checking val is < or >.
# T: O(n+m)
# S: O(n+m)

class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

def merge_two_lists(l1, l2)
  output = ListNode.new(0)
  head = output
  while l1 and l2
    puts output.inspect
    puts "#{l1.val} #{l2.val}"
    if l1.val > l2.val
      output.next = ListNode.new(l2.val)
      l2 = l2.next
    else
      output.next = ListNode.new(l1.val)
      l1 = l1.next
    end
    output = output.next
  end
  while l1
    output.next = ListNode.new(l1.val)
    output = output.next
    l1 = l1.next
  end
  while l2
    output.next = ListNode.new(l2.val)
    output = output.next
    l2 = l2.next
  end
  return head.next
end

l1 = ListNode.new(1)
two = ListNode.new(2)
four = ListNode.new(4)
l1.next = two
two.next = four

l2 = ListNode.new(1)
three = ListNode.new(3)
four = ListNode.new(4)
l2.next = three
three.next = four

puts merge_two_lists(l1, l2).inspect #1->1->2->3->4->4 

l1 = ListNode.new(-9)
l1.next = ListNode.new(3)

l2 = ListNode.new(5)
l2.next = ListNode.new(7)

puts merge_two_lists(l1, l2).inspect #-9->3->5->7
