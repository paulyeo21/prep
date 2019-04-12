# 23. Merge k Sorted Lists
#
# Merge k sorted linked lists and return it as one sorted list. 
# Analyze and describe its complexity.

# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

class ListNode
  attr_accessor :val, :next
  def initialize(val)
    @val = val
    @next = nil
  end
end

# Brute force put all elements into an array. Sort the array and compile into
# linked list. Return head of linked list.
# T: O(n + nlogn + n)
# S: O(n)
def merge_k_lists(lists)
  # O(n)
  output_arr = []
  lists.each do |list|
    while list
      output_arr.push(list.val)
      list = list.next
    end
  end
  # O(n log n)
  output_arr.sort!

  # O(n)
  output_ll = ListNode.new(1)
  head = output_ll
  output_arr.each do |v|
    output_ll.next = ListNode.new(v)
    output_ll = output_ll.next
  end
  return head.next.inspect
end

# Use merge sort to compare head of lists one by one and return fully sorted linked list.
# T: O(k*N) k is number of lists, N is sum of lengths of all lists
# S: O(1)
def merge_k_lists(lists)
  return lists if lists.empty?
  return lists[0] if lists.length == 1
  left = merge_k_lists(lists[0..lists.length/2-1])
  right = merge_k_lists(lists[lists.length/2..-1])
  # merge
  merged = ListNode.new(0)
  head = merged
  while left and right
    if left.val < right.val
      merged.next = ListNode.new(left.val)
      left = left.next
    else
      merged.next = ListNode.new(right.val)
      right = right.next
    end
    merged = merged.next
  end
  while left
    merged.next = ListNode.new(left.val)
    left = left.next
    merged = merged.next
  end
  while right
    merged.next = ListNode.new(right.val)
    right = right.next
    merged = merged.next
  end
  return head.next
end

# Use a priority queue to pop sorted value. Insert heads of each linked list into pq,
# and until pq is nil pop pq. When popping it will return the linked list with lowest
# value. Add that to output and put next value of the popped linked list. 
# T: O(n * log(k)) N is the sum of lengths of all linked lists, k is the number of lists.
# S: O(k)
require_relative "priority_queue\(1\)"

def merge_k_lists(lists)
  head = ListNode.new(0)
  output = head
  pq = PriorityQueue.new
  lists.each do |list|
    pq.insert(list)
  end
  while not pq.empty?
    popped = pq.pop
    output.next = ListNode.new(popped)
    output = output.next
    pq.insert(popped.next)
  end
  return output
end

a = ListNode.new(1)
four = ListNode.new(4)
five = ListNode.new(5)
a.next = four
four.next = five

b = ListNode.new(1)
three = ListNode.new(3)
four = ListNode.new(4)
b.next = three
three.next = four

c = ListNode.new(2)
six = ListNode.new(6)
c.next = six

puts merge_k_lists([a, b, c]).inspect # 1->1->2->3->4->4->5->6
puts merge_k_lists([]).inspect
