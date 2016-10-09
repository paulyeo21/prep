class DoublyLinkedListNode
  attr_accessor :value, :next, :previous

  def initialize value
    @value = value
    @next = nil
    @previous = nil
  end

  def to_s
    self.inspect
  end
end

def main
  a = DoublyLinkedListNode.new(10)
  b = DoublyLinkedListNode.new(1)
  c = DoublyLinkedListNode.new(6)

  a.next = b
  b.previous = a

  b.next = c
  c.previous = b
  
  puts a
end

# main()
