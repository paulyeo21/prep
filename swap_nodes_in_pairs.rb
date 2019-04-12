# 24. Swap Nodes in Pairs
#
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example:
# Given 1->2->3->4, you should return the list as 2->1->4->3.

class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

def swap_pairs(head)
  return nil if not head
  return head if not head.next

  a = ListNode.new(nil)
  b = head
  c = head.next
  output = a
  while a and b and c
    temp = c.next
    a.next = c
    c.next = b
    b.next = temp
    if b.next and b.next.next
      a = b
      b = b.next
      c = b.next
    else
      break
    end
  end
  return output.next
end

a = ListNode.new(1)
two = ListNode.new(2)
three = ListNode.new(3)
four = ListNode.new(4)
a.next = two
two.next = three
three.next = four

puts swap_pairs(a).inspect # 2->1->4->3
