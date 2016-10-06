require "../data-structures/linked_list.rb"

def reverse_linked_list(head)
  previous = nil
  current = head

  while current
    _next = current.next
    current.next = previous
    previous = current
    current = _next
  end

  previous
end

a = LinkedListNode.new(10)
b = LinkedListNode.new(100)
c = LinkedListNode.new(4)

a.next = b
b.next = c

puts reverse_linked_list(a)
