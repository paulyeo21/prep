class BinarySearchTreeNode
  attr_accessor :value, :left, :right

  def initialize(value)
    @value = value
    @left = nil
    @right = nil
  end

  def insert(node)
    if value < node.value
      if @right
        @right.insert(node)
      else
        @right = node
      end
    elsif value > node.value
      if @left
        @left.insert(node)
      else
        @left = node
      end
    end
  end

  def to_s
    self.inspect
  end
end

class EmptyNode
  def insert(*)
    false
  end
end

def main
  a = BinarySearchTreeNode.new(1)
  b = BinarySearchTreeNode.new(2)
  c = BinarySearchTreeNode.new(3)

  a.insert(b)
  a.insert(c)

  puts a
end

# main
