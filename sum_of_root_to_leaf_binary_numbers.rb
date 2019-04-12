# 1022. Sum of Root To Leaf Binary Numbers
#
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents 
# a binary number starting with the most significant bit.  For example, if the path 
# is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
#
# For all leaves in the tree, consider the numbers represented by the path from the 
# root to that leaf.
#
# Return the sum of these numbers.

class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

# Depth first search and keep sum while multiple sum by 2 and adding node value. This 
# works because as we traverse down a height we need to convert from base 2 to base 10.
# T: O(n)
# S: O(1)
def sum_root_to_leaf(root, value=0)
  return 0 if not root
  value = 2 * value + root.val
  return value if root.left == root.right
  return sum_root_to_leaf(root.left, value) + sum_root_to_leaf(root.right, value)
end

a = TreeNode.new(1)
b = TreeNode.new(0)
c = TreeNode.new(1)
d = TreeNode.new(0)
e = TreeNode.new(1)
f = TreeNode.new(0)
g = TreeNode.new(1)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

puts sum_root_to_leaf(a) #22
