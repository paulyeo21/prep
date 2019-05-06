class BinarySearchTree
  attr_reader :nodes

  def initialize(nodes=[0])
    @nodes = nodes
    @size = nodes.length-1
  end

  def to_s
    @nodes.inspect
  end

  def get
    # Exchange first and last
    max = @nodes[1]
    @nodes[1] = @nodes.pop

    # Reorder the root node after exchanging
    percolate_down(1)

    # Return max
    max
  end

  private

  def percolate_down(i=1)
    # if value at i is greater than left or less than right, 
  end
end

bst = BinarySearchTree.new([0, 3, 2, 4, 1])
bst.get
