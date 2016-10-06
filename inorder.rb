require "../data-structures/binary_tree_node.rb"

def inorder(root)
  if root
    inorder(root.left)
    puts root.value
    inorder(root.right)
  end
end

def main
  root = BinaryTreeNode.new(1)
  a = BinaryTreeNode.new(2)
  b = BinaryTreeNode.new(3)
  root.left = a
  root.right = b

  inorder(root)
end

main
