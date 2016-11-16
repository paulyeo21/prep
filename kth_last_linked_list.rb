require "../data-structures/linked_list.rb"

def kth_last_linked_list(k, node)
  previous = node
  current = node.next
  length = 1
  while current
    temp = current
    previous = current
    current = temp.next 
    length += 1
  end 

  current = node
  while length - k > 0
    current = current.next  
    length -= 1
  end

  current.value
end

a = LinkedListNode.new(1)
b = LinkedListNode.new(4)
c = LinkedListNode.new(5)

a.next = b
b.next = c

puts kth_last_linked_list(3, a)
