# 99. Recover Binary Search Tree
#
# Two elements of a binary search tree (BST) are swapped by mistake. Recover the 
# tree without changing its structure.

class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

def recover_tree(bst)
  if bst
    puts bst.val
    recover_tree(bst.left)
    recover_tree(bst.right)
  end
end

three = TreeNode.new(3)
one = TreeNode.new(1)
four = TreeNode.new(4)
two = TreeNode.new(2)
three.left = one
three.right = four
four.left = two

puts recover_tree(three)
