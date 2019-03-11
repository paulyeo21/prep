# Construct Binary Search Tree from Preorder Traversal
#
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

# Definition for a binary tree node.
class TreeNode
  attr_accessor :val, :left, :right
  def initialize(val)
    @val = val
    @left, @right = nil, nil
  end
end

# @param {Integer[]} preorder
# @return {TreeNode}
def bst_from_preorder(preorder)
  return TreeNode.new(preorder[0]) if preorder.length == 1
  root = TreeNode.new(preorder[0])
  prev, stack = root, []
  preorder[1..-1].each do |node|
    current = TreeNode.new(node)
    if current.val > prev.val
      # edge cases
      # 1. current is greater than some parent of parent
      # 2. current is less than parent of parent
      
      # 1
      # continue to check grandparent nodes until current.val < or stack is empty
      while not stack.empty? and current.val > stack.last.val
        prev = stack.pop
      end

      # 2
      prev.right = current
    elsif current.val < prev.val
      prev.left = current
      stack.push(prev)
    end

    prev = current
  end
  root
end

root = bst_from_preorder([8,5,1,7,10,12])
# root = bst_from_preorder([1,2,3])

def preorder_traversal(node)
  if node
    puts node.val
    preorder_traversal(node.left)
    preorder_traversal(node.right)
  end
end

preorder_traversal(root)
