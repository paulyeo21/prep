class LinkedListNode
  attr_accessor :value, :next

  def initialize value
    @value = value
    @next = nil
  end

  def to_s
    self.inspect
  end
end

# a = LinkedListNode.new(1)
# b = LinkedListNode.new(4)
# c = LinkedListNode.new(5)

# a.next = b
# b.next = c
