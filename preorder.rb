require "../data-structures/binary_tree_node.rb"

def preorder(root)
  if root
    puts root.value
    preorder(root.left)
    preorder(root.right)
  end
end

def main
  root = BinaryTreeNode.new(1)
  a = BinaryTreeNode.new(2)
  b = BinaryTreeNode.new(3)
  root.left = a
  root.right = b

  preorder(root)
end

main

