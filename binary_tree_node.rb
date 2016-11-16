class BinaryTreeNode
  attr_accessor :left, :right, :value

  def initialize value
    @left = nil
    @right = nil
    @value = value
  end

  def to_s
    self.inspect
  end
end

def main
  a = BinaryTreeNode.new(1)
  b = BinaryTreeNode.new(2)
  c = BinaryTreeNode.new(3)

  a.left = c
  a.right = b
  puts a
end

# main
