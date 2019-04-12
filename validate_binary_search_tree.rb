# 98. Validate Binary Search Tree
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

def is_valid_bst_helper(node, max, min)
  if node
    if node.val >= max or node.val <= min
      return false
    else
      return is_valid_bst_helper(node.left, node.val, min) &&
        is_valid_bst_helper(node.right, max, node.val)
    end
  else
    return true
  end
end

def is_valid_bst(root)
  max = 2**31 - 1 + 1
  min = -2**31 - 1
  return is_valid_bst_helper(root, max, min)
end

five = TreeNode.new(5)
one = TreeNode.new(1)
four = TreeNode.new(4)
three = TreeNode.new(3)
six = TreeNode.new(6)
five.left = one
five.right = four
four.left = three
four.right = six

puts is_valid_bst(five) #false

two = TreeNode.new(2)
one = TreeNode.new(1)
three = TreeNode.new(3)
two.left = one
two.right = three

puts is_valid_bst(two) #true

a = TreeNode.new(1)
one = TreeNode.new(1)
a.left = one

puts is_valid_bst(a) #false

b = TreeNode.new(2147483647)
puts is_valid_bst(b) #true

c = TreeNode.new(-2147483648)
puts is_valid_bst(c) #true
