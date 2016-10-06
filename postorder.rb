require "../data-structures/binary_tree_node.rb"

def postorder(root)
  if root
    postorder(root.left)
    postorder(root.right)
    puts root.value
  end
end

def main
  root = BinaryTreeNode.new(1)
  a = BinaryTreeNode.new(2)
  b = BinaryTreeNode.new(3)
  root.left = a
  root.right = b

  postorder(root)
end

main
